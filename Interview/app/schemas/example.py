from pydantic import BaseModel

class ExampleBase(BaseModel):
    name: str

class ExampleCreate(ExampleBase):
    pass

class ExampleResponse(ExampleBase):
    id: int
