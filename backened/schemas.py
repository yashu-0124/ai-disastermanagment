from pydantic import BaseModel


class RequestCreate(BaseModel):
    name: str
    phone: str
    request_type: str
    location: str


class RequestResponse(RequestCreate):
    id: int
    priority: str
    status: str

    class Config:
        from_attributes = True
