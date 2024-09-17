from fastapi import APIRouter, HTTPException
from src.services.detalle_casetas import casetas_detalles

router = APIRouter()

@router.get('/detalle-casetas')
def get_casetas_detalles():
    try:
        detalles = casetas_detalles()
        return detalles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))