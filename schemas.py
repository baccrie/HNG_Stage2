from pydantic import BaseModel


class User(BaseModel):
    name: str

class ShowUser(User):
    id: int
    class Config():
        orm_mode = True