# generated by datamodel-codegen:
#   filename:  person.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Extra, Field, conint


class Fur(Enum):
    Short_hair = 'Short hair'
    Long_hair = 'Long hair'


class Noodle(Enum):
    ramen = 'ramen'
    spaghetti = 'spaghetti'


class Soup(Enum):
    bean = 'bean'
    mushroom = 'mushroom'
    tomato = 'tomato'


class Coffee(Enum):
    Black = 'Black'
    Espresso = 'Espresso'


class Tea(Enum):
    Oolong = 'Oolong'
    Green = 'Green'


class Pet(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    fur: Optional[Fur] = None


class Friend(BaseModel):
    class Config:
        extra = Extra.allow

    name: str = Field(..., example='John Doe')
    phone_number: Optional[str] = Field(None, example='(555) 555-1234')
    food: Optional[List[Union[Noodle, Soup]]] = None


class Friends(BaseModel):
    __root__: List[Friend] = Field(..., title='Friends')


class Person(BaseModel):
    first_name: str = Field(..., description="The person's first name.")
    last_name: str = Field(..., description="The person's last name.")
    age: Optional[conint(ge=0)] = Field(None, description='Age in years.')
    pets: Optional[List[Pet]] = None
    friends: Optional[Friends] = None
    robot: Optional[Robot] = None
    comment: None = None
    drink: Optional[List[Union[Coffee, Tea]]] = None
    food: Optional[List[Union[Noodle, Soup]]] = None


class Robot(Pet):
    friends: Optional[Person] = None
    drink: Optional[Coffee] = None
    food: Optional[Noodle] = None
    pet: Optional[Pet] = None


Person.update_forward_refs()
