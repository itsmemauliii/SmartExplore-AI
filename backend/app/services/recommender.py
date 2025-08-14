from typing import List

class Recommender:
    def __init__(self, fs_client):
        self.fs = fs_client
        # register agents
        from app.services.agents.weather_agent import WeatherAgent
        from app.services.agents.preference_agent import PreferenceAgent
        self.agents = [WeatherAgent(), PreferenceAgent()]

    async def suggest(self, ctx: dict) -> List[dict]:
        lat, lon = ctx['lat'], ctx['lon']
        radius = ctx.get('radius_m', 1000)
        raw = await self.fs.search(lat, lon, radius)
        items = raw.get('results', [])

        # apply simple scoring pipeline
        suggestions = []
        for it in items:
            score = 0
            # base score: popularity or rating if present
            if it.get('rating'):
                score += float(it['rating'])

            # query agents for adjustments
            for agent in self.agents:
                adj = await getattr(agent, 'score')(ctx)
                # sample adjustment: if prefer_indoor and item category is outdoor, penalize
                # (you'll want to refine category checks in real app)
                if adj.get('prefer_indoor') and 'park' in it.get('categories', [{}])[0].get('name','').lower():
                    score -= 2

            suggestions.append({
                'fs_id': it.get('fsq_id'),
                'name': it.get('name'),
                'category': it.get('categories', [{}])[0].get('name'),
                'score': score,
            })

        # sort and return top 10
        suggestions.sort(key=lambda x: x['score'], reverse=True)
        return suggestions[:10]
