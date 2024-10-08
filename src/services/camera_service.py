import json
import numpy as np
from scipy.spatial import KDTree
from src.kml_parser import leer_kml
import os

def asignar_camaras_service(kml_file):
    # Paso 1: Leer y generar el archivo extracted_data.json desde el archivo KML
    try:
        # Intentamos leer el archivo KML y generar extracted_data.json
        casetas, camaras = leer_kml(kml_file)
    except FileNotFoundError:
        return {"error": f"Archivo {kml_file} no encontrado."}
    except Exception as e:
        return {"error": f"Error procesando el archivo KML: {str(e)}"}

    # Paso 2: Continuamos con la asignación de cámaras usando el archivo JSON generado
    file_path = os.path.join('data', 'extracted_data.json')
    
    # Verificamos si el archivo JSON existe
    if not os.path.exists(file_path):
        return {"error": "No se encontraron datos de casetas y cámaras para asignar."}
    
    # Leer los datos de casetas y cámaras desde el archivo JSON
    with open(file_path, 'r') as f:
        data = json.load(f)

    casetas = data['casetas']
    camaras = data['camaras']

    # Convertir coordenadas a formato numpy array para usar KDTree
    camaras_coords = np.array([camara['coords'] for camara in camaras])
    camaras_names = [camara['nombre'] for camara in camaras]

    # Crear el árbol KDTree
    kdtree = KDTree(camaras_coords)

    # Asignar las 10 cámaras más cercanas a cada caseta
    for caseta in casetas:
        caseta_coords = caseta['coords']
        distances, indices = kdtree.query(caseta_coords, k=10)
        caseta['camaras_asignadas'] = [camaras_names[i] for i in indices]

    # Guardar la asignación en un archivo JSON en la carpeta /data
    asignacion_file_path = os.path.join('data', 'asignacion_camaras.json')
    with open(asignacion_file_path, 'w') as f:
        json.dump(casetas, f, indent=4)

    # Retornar el resultado de las asignaciones
    return {"Camaras asignadas correctamente"}