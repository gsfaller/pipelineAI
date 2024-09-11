from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    product1 = "Boots" 
    product2 = "Sandal"
    product3 = "Sneaker"


class Vendas(BaseModel):
    email = str
    dt_sale = datetime
    time_hours = datetime 
    quantity = PositiveInt
    gross_sale = PositiveFloat
    product = ProdutoEnum
    
