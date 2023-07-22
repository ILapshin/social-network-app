from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str


class PostBase(BaseModel):
    title: str
    content: str
    user_id: int


class ReactionBase(BaseModel):
    is_like: bool
    user_id: int
    post_id: int


class UserWrite(UserBase):
    password: str


class PostWrite(PostBase):
    pass


class ReactionWrite(ReactionBase):
    pass


class ReactionRead(ReactionBase):
    class Config():
        from_attributes = True


class PostRead(PostBase):
    # created_at: int
    reactions: List[ReactionRead] = []

    class Config():
        from_attributes = True


class UserRead(UserBase):
    posts: List[PostRead] = []
    reactions: List[ReactionRead] = []
    
    class Config():
        from_attributes = True