from fastapi import APIRouter
from src.schemas.schema_register import registerModel
from src.schemas.schema_login import loginModel
#En la ultima importacion tuve que usar "as" ya que compartia el mismo nombre mis funciones de mi controlador con las de ruta, pude cambiarlas en las rutas para no tener problemas pero personalmente no lo entendria
from src.controllers.auth_controller import register_user as register_service, login_user as login_service

router = APIRouter()

#Rutas para registrar y loguear un usuario

@router.post("/register")
def register_user(user:registerModel):
    return register_service(user)

@router.post("/login")
def login_user(user:loginModel):
    return login_service(user)