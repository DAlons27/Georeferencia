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

# Funcion para obtner el detalle de una caseta específica
def get_caseta_detalle(caseta_id: str):
    file_path = os.path.join('data', 'extracted_data.json')

    # Se verifica si el archivo existe
    if not os.path.exists(file_path):
        return {"error": "No se encontró el archivo de datos."}
    
    # Leer el archivo json de datos
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Obtener la lista de casetas
    casetas = data.get('casetas', [])

    # Buscar la caseta ignorando el prefijo "PAR "
    for caseta in casetas:
        nombre_sin_prefijo = caseta['nombre'].replace('PAR ', '')
        if nombre_sin_prefijo == caseta_id:
            return {
                "nombre": caseta['nombre'],
                "coords": caseta['coords']
            }

    return {"error": f"No se encontró la caseta con el nombre {caseta_id}."}