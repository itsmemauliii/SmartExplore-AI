import React, {useEffect, useState} from 'react';
import { View, Text, Button, FlatList } from 'react-native';
import * as Location from 'expo-location';
import apiClient from '../services/apiClient';

export default function HomeScreen({ navigation }){
  const [loc, setLoc] = useState(null);
  const [places, setPlaces] = useState([]);

  useEffect(()=>{
    (async ()=>{
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== 'granted') return;
      let location = await Location.getCurrentPositionAsync({});
      setLoc(location.coords);
    })()
  },[])

  async function fetchSuggestions(){
    if(!loc) return;
    const res = await apiClient.post('/api/v1/suggest', {
      lat: loc.latitude, lon: loc.longitude
    });
    setPlaces(res.data.results);
    navigation.navigate('Map', { places: res.data.results });
  }

  return (
    <View style={{flex:1, padding:16}}>
      <Text style={{fontSize:24}}>SmartExplore AI</Text>
      <Button title="Find places near me" onPress={fetchSuggestions} />
      <FlatList data={places} keyExtractor={(i)=>i.fsq_id} renderItem={({item})=> <Text>{item.name}</Text>} />
    </View>
  )
}
