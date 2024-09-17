from fastapi import FastAPI
from src.routes.Asignacion_router import router as Asignacion_router
from src.routes.VerAsignacion_router import router as VerAsignacion_router
from src.routes.Camaras_router import router as Camaras_router
from src.routes.Casetas_router import router as Casetas_router

app = FastAPI()

# Incluir los subrouters
app.include_router(Asignacion_router, prefix="/Asignacion", tags=["Asignacion"])
app.include_router(VerAsignacion_router, prefix="/VerAsignacion", tags=["VerAsignacion"])
app.include_router(Camaras_router, prefix="/camaras", tags=["Camaras"])
app.include_router(Casetas_router, prefix="/casetas", tags=["Casetas"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)