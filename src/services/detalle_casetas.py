import json
import os

def casetas_detalles():
    file_path = os.path.join('data', 'extracted_data.json')

    # Se verifica si el archivo existe
    if not os.path.exists(file_path):
        return {"error":"No se encontro el archivo de datos."}
    
    # Leer el archivo json de datos
    with open(file_path, 'r') as f:
        data = json.load(f)

    casetas = data.get('casetas', [])
    return [{"nombre": caseta['nombre'], "coords": caseta['coords']} for caseta in casetas]