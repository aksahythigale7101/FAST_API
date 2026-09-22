from pydantic import BaseModel, Field, ConfigDict


class ProductCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


#partial update
#Only changed fields #PATCH
class ProductUpdate(BaseModel):

    name: str | None = Field(default=None, min_length=3, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    price: float | None = Field(default=None, gt=0)
    quantity: int | None = Field(default=None, ge=0)





class ProductResponse(BaseModel):

    id: int
    name: str
    description: str | None
    price: float
    quantity: int
    
    model_config = ConfigDict(from_attributes=True)#allows Pydantic to convert a SQLAlchemy object into a Pydantic response.

