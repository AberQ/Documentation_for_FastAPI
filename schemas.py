from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
