import xml.etree.ElementTree as ET
import os
import re
import json

#Funcion para extraer las coordenadas
def extraer_coordenadas(file_name):
    """
    Lee un archivo KML desde la carpeta data/ y extrae las coordenadas de las casetas y cámaras.
    Corrige el formato de las coordenadas invirtiendo el orden y eliminando el ",0".
    
    :param file_name: Nombre del archivo KML en la carpeta data/
    :return: Listas de diccionarios con las casetas y cámaras
    """
    file_path = os.path.join('data', file_name)
    
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

    tree = ET.parse(file_path)
    root = tree.getroot()

    ns = {'kml': 'http://www.opengis.net/kml/2.2'}
    casetas = []
    camaras = []

    for placemark in root.findall('.//kml:Placemark', ns):
        nombre_elem = placemark.find('kml:name', ns)
        coords_elem = placemark.find('.//kml:coordinates', ns)
        
        if nombre_elem is None or coords_elem is None:
            continue
        
        nombre = nombre_elem.text
        coords_text = coords_elem.text.strip() if coords_elem.text else ""
        
        if nombre is None:
            continue
        
        nombre = nombre.strip()
        coords = coords_text.split(',')[:2]
        try:
            coords = tuple(map(float, coords))
        except ValueError:
            continue
        
        coords = coords[::-1]

        # Clasificación basada en el nombre
        if nombre.startswith("PAR "):
            casetas.append({'nombre': nombre, 'coords': coords})
        elif re.match(r'^\d+.*$', nombre) and re.search(r'[a-zA-Z]', nombre):
            camaras.append({'nombre': nombre, 'coords': coords})

    # Guardar los datos en un archivo JSON
    with open('data/extracted_data.json', 'w') as json_file:
        json.dump({'casetas': casetas, 'camaras': camaras}, json_file, indent=4)

    return casetas, camaras
