import folium
import geopy
from geopy.geocoders import ArcGIS

nom = ArcGIS()
n = nom.geocode('05-300 Mińsk Mazowiecki, Sienicka 57B, Poland')
print(n.longitude, n.latitude)

x = n.longitude
y = n.latitude
map = folium.Map(location=[x,y])