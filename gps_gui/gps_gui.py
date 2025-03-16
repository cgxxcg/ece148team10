import folium
# Open the file in a browser (Windows)
import webbrowser

# Define your latitude and longitude (Example: New York City)
latitude = 32.88107042536644
longitude = -117.23339864051708

# Create a map centered oan the given location
m = folium.Map(location=[latitude, longitude], zoom_start=14)  # Adjust zoom for ~3-mile view

folium.Circle(
    radius=300,  # 3 miles in meters (1 mile ≈ 1609 meters)
    location=[latitude, longitude],
    color="blue",
    fill=True,
    fill_color="lightblue",
    fill_opacity=0.3
).add_to(m)
m.save("gps_gui\map.html")  # Saves the map as an HTML file

webbrowser.open("map.html")
