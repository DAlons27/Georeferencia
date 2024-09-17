from fastapi import APIRouter, HTTPException
from src.services.camera_service import asignar_camaras_service
import os

router = APIRouter()

# Ruta para asignar las 10 camaras mas cercanas

@router.get("/asignar-camaras")
def asignar_camaras():
    data_dir = 'data'  # Carpeta donde se almacenan los archivos KML
    kml_files = [f for f in os.listdir(data_dir) if f.endswith('.kml')]

    # Verificar si hay archivos KML en la carpeta 'data/'
    if len(kml_files) == 0:
        raise HTTPException(status_code=404, detail="No se encontró ningún archivo KML en la carpeta 'data/'.")
    
    # Si hay más de un archivo KML, lanzar un error para evitar ambigüedades
    if len(kml_files) > 1:
        raise HTTPException(status_code=400, detail="Se encontraron múltiples archivos KML en la carpeta 'data/'. Por favor, deja solo uno.")

    # Obtener el primer (y único) archivo KML
    kml_file = kml_files[0]

    # Ejecutar el flujo de asignación usando el archivo encontrado
    resultado = asignar_camaras_service(kml_file)

    return resultado
