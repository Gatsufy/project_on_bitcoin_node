import geoip2.database

import folium

from folium import FeatureGroup, LayerControl

import webbrowser

from pprint import pprint

from from_csv_gant_chartt import from_csv_to_gant_chartt

def from_ip_to_geo(filename):

    reader = geoip2.database.Reader('C://Users//mmmel//Desktop//GeoLite2-City_20201229//GeoLite2-City.mmdb')

    dict_from_csv = from_csv_to_gant_chartt(filename)

    respose = reader.city('82.61.121.164')

    map = folium.Map(location=[respose.location.latitude, respose.location.longitude], zoom_start=4)

    inbound_node = FeatureGroup(name="inbound")

    outbound_node = FeatureGroup(name="outbound")


    for key, value in dict_from_csv.items():

        respose=reader.city(key)

        for i in range(1):

            if value[i][3] is False:
                
                folium.Marker(location=[respose.location.latitude, respose.location.longitude], popup=respose.subdivisions.most_specific.name, icon=folium.Icon(color="red")).add_to(outbound_node)

            else:

                folium.Marker(location=[respose.location.latitude, respose.location.longitude], popup=respose.subdivisions.most_specific.name, icon=folium.Icon(color="blue")).add_to(inbound_node)
    


    inbound_node.add_to(map)

    outbound_node.add_to(map)

    LayerControl().add_to(map)
    
    map.save('C://Users//mmmel//Desktop//index.html')

    webbrowser.open('C://Users//mmmel//Desktop//index.html')

    
from_ip_to_geo("C://Users//mmmel//Desktop//nodes_disc.csv")
