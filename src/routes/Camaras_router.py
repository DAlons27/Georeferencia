from fastapi import APIRouter, HTTPException
from src.services.detalle_camaras import camaras_detalles

router = APIRouter()

@router.get('/detalle-camaras')
def get_camaras_detalles():
    try:
        detalles = camaras_detalles()
        return detalles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Ruta para obtener el detalle de una cámara específica
# Aquí usamos path parameters
@router.get('/detalle-camaras/{camara_id}')
def get_camara_detalle(camara_id: int):  
    try:
        detalle = get_camara_detalle(camara_id)
        if detalle is None:
            raise HTTPException(status_code=404, detail="Cámara no encontrada")
        return detalle
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))