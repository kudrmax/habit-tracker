from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class UserUpdate(BaseModel):
    username: str | None = None


class UserDelete(UserBase):
    id: int
