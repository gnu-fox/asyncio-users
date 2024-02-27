from uuid import UUID

from pydantic import BaseModel
from pydantic import Field

class Contact(BaseModel):
    id : UUID = Field(..., description="Unique identifier for the contact.")
    name : str = Field(..., description="The name of the contact.")