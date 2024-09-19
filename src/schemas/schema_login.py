from pydantic import BaseModel, field_validator, model_validator
import re

class loginModel(BaseModel):
    """
    Represents the login model with username, password, and password_confirmation fields.
    """

    username: str
    password: str
    confirm_password: str

    # Validaciones del campo username
    @field_validator('username')
    def username_login(cls, value):
        """
        Validates the username field.

        Args:
            value (str): The value of the username field.

        Raises:
            ValueError: If the username does not meet the validation criteria.

        Returns:
            str: The validated username value.
        """

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
    
    @field_validator('password')
    def password_login(cls, value):
        """
        Validates the password field.

        Args:
            value (str): The value of the password field.

        Raises:
            ValueError: If the password does not meet the validation criteria.

        Returns:
            str: The validated password value.
        """

        if len(value) < 8 or len(value) > 15:
            raise ValueError('La contraseña debe tener entre 8 y 15 caracteres')
        
        if " " in value:
            raise ValueError('La contraseña no debe contener espacios en blanco')
        
        # Verificar que la contraseña sea segura
        if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])", value):
            raise ValueError('La contraseña debe contener al menos una letra mayúscula, una letra minúscula, un número y un caracter especial')
        
        return value
    
    @model_validator(mode='after')
    def password_check(self) -> 'loginModel':
        """
        Validates the password_confirmation field and performs additional checks.

        Raises:
            ValueError: If the passwords do not match, the username is the same as the password,
                or the password contains the username.

        Returns:
            loginModel: The validated login model instance.
        """

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
