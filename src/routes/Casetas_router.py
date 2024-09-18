from fastapi import APIRouter, HTTPException
from src.services.detalle_casetas import casetas_detalles, get_caseta_detalle

router = APIRouter()

@router.get('/detalle')
def get_casetas():
    try:
        detalles = casetas_detalles()
        return detalles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get('/detalle/{caseta_id}')
def get_caseta(caseta_id: str):
    try:
        detalle = get_caseta_detalle(caseta_id)
        if detalle is None:
            raise HTTPException(status_code=404,
            detail="Caseta no encontrada")
        return detalle
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))