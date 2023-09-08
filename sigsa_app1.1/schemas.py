from pydantic import BaseModel


class UserBase(BaseModel):
    clave: str


# Esta clase imprime las columnas de la tabla usuario
class User(UserBase):
    clave: int
    nombre: str
    jefe_directo: str
    departamento: str
    fecha_ingreso:str
    antiguedad :str
    is_active: bool


class UserCreate(UserBase):
    clave: int
    nombre: str
    jefe_directo: str
    departamento: str
    fecha_ingreso:str
    antiguedad :str
    is_active: bool
    
    
class UserBase2(BaseModel):
    nombre: str
    jefe_directo: str
    departamento: str
    fecha_ingreso: str
    antiguedad: str
    is_active: bool


class UserUpdate(UserBase2):
    pass

    
    
class User(UserBase):
    clave: int
    

