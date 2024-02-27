from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from pydantic import Field

class Message(BaseModel):
    id : UUID = Field(..., description="Unique identifier for the message.")
    sender : UUID = Field(..., description="The sender of the message.")
    receiver : UUID = Field(..., description="The receiver of the message.")
    content : str = Field(..., description="The content of the message.")
    created_at : datetime = Field(..., description="The date and time the message was created.")
    updated_at : datetime = Field(..., description="The date and time the message was updated.")
