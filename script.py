import folium
map = folium.Map(location=[45.372,-121.697], zoom_start=12, tiles='Stamen Terrain')
map.simple_marker(location=[45.372,-121.697],popup='Mt. Hood Meadows', marker_color='red')
map.simple_marker(location=[45.372,-176.697],popup='Timberland Place', marker_color='green')

map.create_map(path='test.html')