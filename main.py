#uvicorn main:app --reload

from fastapi import FastAPI
from enum import Enum
from typing import Optional
from fastapi import Body, Query, Path
from fastapi.datastructures import Default
from pydantic import BaseModel
from pydantic import Field


app = FastAPI()

#models

class HairColor(Enum):
    white = "white"
    brown = "Brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class Location(BaseModel):
    city: str
    state: str
    country: str




class Person(BaseModel):
    frist_name: str = Field(..., min_length=1, max_length=50, example="Miguel")
    last_name: str = Field(..., min_length=1, max_length=50, example= "Torres")
    age: int = Field(..., gt=0, le=115, example = 25)
    hair_color: Optional[str] = Field(default = None, example = HairColor.black)
    is_marred: Optional[bool] = Field(default = None, example = False)

#    class Config:
#        schema_extra = {
#            "example": {
#                "firs_name": "Facundo",
#                "last_name": "Garcia Martoni",
#                "age": 21,
#                "hair_color": "blonde",
#                "is_married": False
#            }
#        }

@app.get("/")
def home():
    return {"Hello" : "world"}


@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

@app.get("/person/detail")
def Show_person(
    name: Optional[str] = Query(
        ..., 
        min_length = 1, 
        max_length = 50,
        title = "Person Name",
        description = "This is the person name. It's between 1 and 50 characters",
        example = "Rocio"
        
        
        
        ),
    age: str = Query(
        ...,
        title = "Person Age",
        description = "This is the person age. It's required",
        example = 21
        
        
        
    )

):
    return {name: age}

@app.get("/person/detail/{person_id}")

def show_person(
    person_id: int = Path(..., gt = 0, example = 123)


):
    return {person_id: "It exists!"}


@app.put("/person/{person_id}")
def update_person (
    person_id: int = Path(
        ...,
        title = "Person ID",
        description = "This is the person ID",
        gt = 0,
        example = 123
        ),

        person: Person = Body(...),
        #Location: Location = Body(...)


):
    #results = person.dict()
    #results.update(Location.dict())
    #return results
    return person