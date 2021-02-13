import geoip2.database

import folium

import webbrowser

from pprint import pprint

from folium import FeatureGroup, LayerControl

from from_csv_gant_chartt import from_csv_to_gant_chartt

def from_ip_to_geo(filename):

    reader = geoip2.database.Reader('C://Users//mmmel//Desktop//GeoLite2-City_20201229//GeoLite2-City.mmdb')

    dict_from_csv = from_csv_to_gant_chartt(filename)

    respose = reader.city('82.61.121.164')

    map = folium.Map(location=[respose.location.latitude, respose.location.longitude], zoom_start=4)

    america = FeatureGroup(name="America")

    oceania = FeatureGroup(name="Oceania")
    
    europe = FeatureGroup(name="Europe")
    
    asia = FeatureGroup(name="Asia")

    africa = FeatureGroup(name="Africa")

    for key, value in dict_from_csv.items():

        respose = reader.city(key)

        for i in range(1):

            if respose.continent.name == 'North America' or respose.continent.name == 'South America' :

                folium.Marker(location=[respose.location.latitude, respose.location.longitude], popup=respose.subdivisions.most_specific.name, icon=folium.Icon(color="red")).add_to(america)

            if respose.continent.name == 'Asia':

                folium.Marker(location=[respose.location.latitude, respose.location.longitude], popup=respose.subdivisions.most_specific.name, icon=folium.Icon(color="darkpurple")).add_to(asia)


            if respose.continent.name == 'Europe':

                folium.Marker(location=[respose.location.latitude, respose.location.longitude], popup=respose.subdivisions.most_specific.name, icon=folium.Icon(color="darkgreen")).add_to(europe)

            if respose.continent.name == 'Oceania':

                folium.Marker(location=[respose.location.latitude, respose.location.longitude], popup=respose.subdivisions.most_specific.name, icon=folium.Icon(color="orange")).add_to(oceania)

            if respose.continent.name == "Africa":

                folium.Marker(location=[respose.location.latitude, respose.location.longitude], popup=respose.subdivisions.most_specific.name, icon=folium.Icon(color="lightgray")).add_to(africa)


    
    europe.add_to(map)

    asia.add_to(map)

    oceania.add_to(map)

    america.add_to(map)

    africa.add_to(map)
    
    LayerControl().add_to(map)

    map.save('C://Users//mmmel//Desktop//diff_by_continent.html')

    webbrowser.open('C://Users//mmmel//Desktop//diff_by_continent.html')


from_ip_to_geo("C://Users//mmmel//Desktop//nodes_disc.csv")
