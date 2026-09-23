from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class updateStruct(BaseModel):
    name: Optional[str] = Field(default=None, title="Update your name")
    age: Optional[int] = Field(default=None, title="Update your age")
    email: Optional[EmailStr] = Field(default=None, title="Update your email")