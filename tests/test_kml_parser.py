import sys
import os

# Agregar el directorio raíz al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.services.procesar_kml import leer_kml

def test_kml_parser():
    """
    Función de prueba para el archivo kml_parser.py.
    """
    casetas, camaras = leer_kml('MDLO.kml')

    print("Todas las Casetas:")
    for i, caseta in enumerate(casetas, 1):
        print(f"{i}. Nombre: {caseta['nombre']}, Coordenadas: {caseta['coords']}")
    
    print("\nTodas las Cámaras:")
    for i, camara in enumerate(camaras, 1):
        print(f"{i}. Nombre: {camara['nombre']}, Coordenadas: {camara['coords']}")

    print("\nPrueba realizada con éxito")

if __name__ == "__main__":
    test_kml_parser()