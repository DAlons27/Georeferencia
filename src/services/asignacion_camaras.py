import json
import os

# Funcion para leer la asignacion
def camaras_asignadas():
    asignacion_file_path = os.path.join('data', 'asignacion_camaras.json')

    # Se verifica si el archivo existe
    if not os.path.exists(asignacion_file_path):
        return {"error":"No se ha realizado ninguna asignacion de camaras"}
    
    # Leer el archivo de asignacion de camaras
    with open(asignacion_file_path, 'r') as f:
        asignacion = json.load(f)

    return asignacion