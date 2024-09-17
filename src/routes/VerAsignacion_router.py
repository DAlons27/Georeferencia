from fastapi import APIRouter, HTTPException
from src.services.asignacion_camaras import camaras_asignadas

router = APIRouter()

@router.get('/ver-asignacion-camaras')
def get_asignacion():
    try:
        resultado = camaras_asignadas()
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))