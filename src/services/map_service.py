import folium
import json
from jinja2 import Template

#Cargar datos desde extracted_data.json
def generar_mapa():
    #Cargar los datos del archivo JSON
    with open('data/extracted_data.json', 'r') as f:
        data = json.load(f)

    # Incializar el mapa centrado en la primera caseta
    coords_iniciales = data["casetas"][0]["coords"]
    mapa = folium.Map(location=coords_iniciales, zoom_start=13)

    # Añadir las casetas al mapa
    for caseta in data["casetas"]:
        folium.Marker(
            location=caseta["coords"],
            popup=caseta["nombre"],
            icon=folium.Icon(color="blue", icon="home"),
        ).add_to(mapa)

    # Guardar el mapa en un HTML string
    return mapa._repr_html_() #Devuelve el HTML del mapa como string