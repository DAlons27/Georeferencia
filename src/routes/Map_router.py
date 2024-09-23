from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from src.services.map_service import generar_mapa

router = APIRouter()

# Definir la ubicación de los templates
templates = Jinja2Templates(directory="templates")

@router.get("/mapa")
async def mostrar_mapa(request: Request):
    mapa_html = generar_mapa()  # Generar el mapa con Folium
    return templates.TemplateResponse("mapa.html", {"request": request, "mapa_html": mapa_html})
