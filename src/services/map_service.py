import json
import folium
  
# Cargar datos desde extracted_data.json
def generar_mapa():

    try:
        with open('data/extracted_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError as e:
        print("Error: Archivo 'extracted_data.json' no encontrado.")
        # Puedes simplemente devolver un valor vacío o un mapa sin datos
        return "Error: No se encontró el archivo requerido para generar el mapa."
    
    # Inicializar listas para las coordenadas de casetas y cámaras
    todas_coordenadas = []

    # Añadir las coordenadas de las casetas
    for caseta in data["casetas"]:
        todas_coordenadas.append(caseta["coords"])
    
    # Añadir las coordenadas de las cámaras
    for camara in data["camaras"]:
        todas_coordenadas.append(camara["coords"])
    
    # Calcular el centro promedio de todas las coordenadas
    latitudes = [coord[0] for coord in todas_coordenadas]
    longitudes = [coord[1] for coord in todas_coordenadas]
    
    centro_mapa = [sum(latitudes) / len(latitudes), sum(longitudes) / len(longitudes)]
    
    # Crear el mapa centrado en el promedio calculado
    mapa = folium.Map(location=centro_mapa, zoom_start=13)

    # Tipo de mapa base
    folium.TileLayer('Stamen Terrain', attr='Map data © OpenStreetMap contributors').add_to(mapa)
    folium.TileLayer('CartoDB positron', attr='&copy; <a href="https://carto.com/attributions">CARTO</a>').add_to(mapa)

    folium.LayerControl().add_to(mapa)
    
    # Añadir las casetas al mapa
    for caseta in data["casetas"]:
        folium.Marker(
            location=caseta["coords"],
            popup=caseta["nombre"],
            icon=folium.Icon(color='green', icon='home'),
        ).add_to(mapa)
    
    # Añadir las cámaras al mapa
    for camara in data["camaras"]:
        folium.Marker(
            location=camara["coords"],
            popup=camara["nombre"],
            icon=folium.Icon(color='blue'),
        ).add_to(mapa)
    
    # Guardar el mapa en un HTML string
    return mapa._repr_html_()  # Devuelve el HTML del mapa como string

