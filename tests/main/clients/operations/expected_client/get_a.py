from pydantic import Field

from .base_model import BaseModel


class GetA(BaseModel):
    a: "GetAA"


class GetAA(BaseModel):
    value: str
    value_b: "GetAAValueB" = Field(alias="valueB")


class GetAAValueB(BaseModel):
    value: str
