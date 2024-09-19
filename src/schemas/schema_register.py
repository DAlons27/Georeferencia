from pydantic import BaseModel, EmailStr, field_validator, model_validator 
import re

class registerModel(BaseModel):

    username: str
    name: str
    lastname: str
    age: int
    email: EmailStr
    password: str
    confirm_password: str

    @field_validator('username')
    def username_register(cls, value):

        if len(value) < 6 or len(value) > 15:
            raise ValueError('El username debe tener entre 6 y 15 caracteres')  
        
        # Si hay espacios en blanco
        if " " in value:
            raise ValueError('El username no debe contener espacios en blanco')
        
        # No debe haber caracteres especiales
        if not re.match("^[a-zA-Z0-9]+$", value):
            raise ValueError('El username debe ser una combinación de letras y números sin caracteres especiales')
        
        #Evaluar que la cadena contenga letras y numeros
        if not re.match("^(?=.*[a-zA-Z])(?=.*\d)", value):
            raise ValueError('El username debe contener al menos una letra y un número')

        return value
    
    @field_validator('name', 'lastname')
    @classmethod    
    def name_and_lastname(cls, v: str) -> str:

        if isinstance(v, str):
            # Comprobare si son mayores que 3 caracteres y menores que 16 caracteres
            if len(v) < 3 or len(v) > 16:
                raise ValueError('El nombre y/o apellido deben tener entre 3 y 16 caracteres')
            
            # Comprobar si el nombre y apellido contienen caracteres especiales o numeros, a excepecion del espacio entre nombres
            if not re.match("^[a-zA-Z\s]+$", v):
                raise ValueError('El nombre y/o apellido no deben contener numeros o caracteres especiales')
                                   
            return v
        
    @field_validator('age')
    def age_register(cls, value):
        
        if value > 100 or value < 10:
            raise ValueError('Ingresa una edad válida')
            
        return value

    @field_validator('password')
    def password_register(cls, value):

        if len(value) < 8 or len(value) > 15:
            raise ValueError('La contraseña debe tener entre 8 y 15 caracteres')
        
        if " " in value:
            raise ValueError('La contraseña no debe contener espacios en blanco')
        
        # Verificar que la contraseña sea segura
        if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])", value):
            raise ValueError('La contraseña debe contener al menos una letra mayúscula, una letra minúscula, un número y un caracter especial')
        
        return value
    
    @model_validator(mode='after')
    def password_check(self) -> 'registerModel':

        pw1 = self.password
        pw2 = self.confirm_password
        user = self.username

        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('Las contraseñas no coinciden')

        # El username no puede ser igual a la contraseña
        if user == pw1:
            raise ValueError('El username no puede ser igual a la contraseña')
        
        # La contraseña no puede tener una coincidencia de 5 caracteres con el username
        if pw1 in user or user in pw1:
            raise ValueError('La contraseña no puede contener el username')
        
        return self
      