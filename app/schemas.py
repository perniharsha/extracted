from pydantic import BaseModel, EmailStr, Field
from typing import List
from datetime import date

class SurveyCreate(BaseModel):
    first_name: str
    last_name: str
    street_address: str
    city: str
    state: str
    zip_code: str
    telephone: str
    email: EmailStr
    date_of_survey: date

    liked_most: List[str] = Field(..., example=["students", "campus"])
    interest_source: str  # friends, television, internet, other
    recommendation: str  # Very Likely, Likely, Unlikely
    raffle: str  # We'll validate it manually if needed
    comments: str = ""

class Survey(SurveyCreate):
    id: int

    class Config:
        orm_mode = True
