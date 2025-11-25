from pydantic import BaseModel, EmailStr

# ---------------- Post Schemas ----------------
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# ---------------- User Schemas ----------------
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    class Config:
        orm_mode = True

