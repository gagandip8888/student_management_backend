from pydantic import BaseModel, Field, EmailStr
from typing import Annotated

class StudentStruct(BaseModel):
    roll: Annotated[int, Field(title="Enter student roll number")]
    name: Annotated[str, Field(title="Enter student name")]
    age: Annotated[int, Field(title="Enter student age")] 
    email: Annotated[EmailStr, Field(title="Enter student email")]
