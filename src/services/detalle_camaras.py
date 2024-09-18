import json
import os

def camaras_detalles():
    file_path = os.path.join('data', 'extracted_data.json')

    # Se verifica si el archivo existe
    if not os.path.exists(file_path):
        return {"error":"No se encontro el archivo de datos."}
    
    # Leer el archivo json de datos
    with open(file_path, 'r') as f:
        data = json.load(f)

    camaras = data.get('camaras', [])
    return [{"nombre": camara['nombre'], "coords": camara['coords']} for camara in camaras]

# Función para obtener el detalle de una cámara específica
def get_camara_detalle(camara_id: int):
    file_path = os.path.join('data', 'extracted_data.json')

    # Se verifica si el archivo existe
    if not os.path.exists(file_path):
        return {"error": "No se encontró el archivo de datos."}
    
    # Leer el archivo json de datos
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Obtener la lista de cámaras
    camaras = data.get('camaras', [])

    # Buscar la cámara por el ID
    if camara_id < 1 or camara_id > len(camaras):
        return {"error": f"No se encontró la cámara con ID {camara_id}."}
    
    camara = camaras[camara_id - 1]  # Restamos 1 ya que la lista es indexada desde 0

    return {
        "id": camara_id,
        "nombre": camara['nombre'],
        "coords": camara['coords']
    }
