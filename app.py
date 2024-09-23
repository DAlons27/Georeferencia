from fastapi import FastAPI
from src.routes.Asignacion_router import router as Asignacion_router
from src.routes.VerAsignacion_router import router as VerAsignacion_router
from src.routes.Camaras_router import router as Camaras_router
from src.routes.Casetas_router import router as Casetas_router
from src.routes.Auth_router import router as Auth_router
from src.routes.Map_router import router as Map_router

app = FastAPI()

# Incluir los subrouters
app.include_router(Asignacion_router, prefix="/Asignacion", tags=["Asignacion"])
app.include_router(VerAsignacion_router, prefix="/VerAsignacion", tags=["VerAsignacion"])
app.include_router(Camaras_router, prefix="/camaras", tags=["Camaras"])
app.include_router(Casetas_router, prefix="/casetas", tags=["Casetas"])
app.include_router(Auth_router, prefix="/auth", tags=["Autenticacion"])
app.include_router(Map_router, prefix="/mapa", tags=["Mapa"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)