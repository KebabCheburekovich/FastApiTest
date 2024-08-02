from datetime import datetime

from pydantic import BaseModel, field_validator


class DogSchema(BaseModel):
    name: str
    breed: str


class OrderReadSchema(BaseModel):
    apartment_number: int
    start_at: datetime


class OrderCreateSchema(BaseModel):
    apartment_number: int
    start_at: datetime
    dog: DogSchema

    @field_validator('start_at')
    def validate_start_at_time(cls, value):
        if not (7 <= value.hour <= 23 and value.minute in [0, 30]):
            raise ValueError("Invalid start time")
        return value
