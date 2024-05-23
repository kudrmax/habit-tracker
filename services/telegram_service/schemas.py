from pydantic import BaseModel, Field


class FromTg(BaseModel):
    # id: int
    # is_bot: bool
    username: str = None
    first_name: str = None
    last_name: str = None
    # language_code: str


class Message(BaseModel):
    # message_id: int
    from_tg: FromTg = Field(alias="from")
    # chat: dict
    # date: int
    text: str


class Answer(BaseModel):
    update_id: int = None
    message: Message
