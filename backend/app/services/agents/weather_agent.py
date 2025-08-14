class WeatherAgent:
    async def score(self, ctx: dict) -> dict:
        # ctx may contain 'weather' key with classification like 'rain', 'sunny'
        # Return adjustments to scoring or filters
        weather = ctx.get('weather')
        if weather == 'rain':
            return {'prefer_indoor': True}
        return {}
