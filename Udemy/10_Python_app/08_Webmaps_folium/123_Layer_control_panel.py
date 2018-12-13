import folium
import pandas
     
def choose_color(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev <3000:
        return 'orange'
    else: return 'red'

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
     
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
     
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")

fg_v = folium.FeatureGroup(name = "Volcanos")
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg_v.add_child(folium.CircleMarker(location = [lt, ln],
                                    popup = str(el)+' m',
                                    radius = 6,
                                    fill_color = str(choose_color(el)),
                                    color = 'grey',
                                    fill = True,
                                    fill_opacity = 0.9))

fg_p = folium.FeatureGroup(name = "Population")
fg_p.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),

style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg_v)
map.add_child(fg_p)
map.add_child(folium.LayerControl())

map.save("Map_html_popup_advanced.html")