from fastapi import APIRouter, HTTPException
from src.services.detalle_camaras import camaras_detalles, get_camara_detalle

router = APIRouter()

@router.get('/detalle')
def get_camaras():
    try:
        detalles = camaras_detalles()
        return detalles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Ruta para obtener el detalle de una cámara específica
# Aquí usamos path parameters
@router.get('/detalle/{camara_id}')
def get_camara(camara_id: int):  
    try:
        detalle = get_camara_detalle(camara_id)
        if detalle is None:
            raise HTTPException(status_code=404, detail="Cámara no encontrada")
        return detalle
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))