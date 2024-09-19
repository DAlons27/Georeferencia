from fastapi import HTTPException, status
from src.schemas.schema_login import loginModel
from src.schemas.schema_register import registerModel

#Lista temporal para almacenar usuarios
fake_users_db = {
    "DAlons27": {
        "username": "DAlons27",
        "password": "Yawen123@",  # En un entorno real, esta contraseña debería estar hasheada
    }
}

def register_user(user_data: registerModel):
    #Verificamos si el usuario ya existe en la base de datos ficticia
    if user_data.username in fake_users_db:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    #Guardar el usuario nuevo en la base de datos ficticia
    fake_users_db[user_data.username] = {
        "name": user_data.name,
        "lastname": user_data.lastname,
        "age": user_data.age,
        "email": user_data.email,
        "password": user_data.password  # En una implementación real, usarías hashing de contraseñas
    }

    return {"message": "Usuario registrado exitosamente"}

def login_user(login_data: loginModel):
    # Buscar el usuario en la base de datos ficticia
    user = fake_users_db.get(login_data.username)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    # Verificar si la contraseña es correcta
    if user["password"] != login_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña incorrecta"
        )

    return {"message": "Login exitoso"}