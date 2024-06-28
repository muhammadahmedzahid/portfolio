from pydantic import BaseModel
from pydantic import ValidationError
from pydantic import Field


# Here Actually we are doing class inheritance.
class Person(BaseModel):
    first_name: str = Field(alias="First Name")
    last_name: str = Field(alias="Last Name")
    age: int = Field(alias="Age")


data = {
    "First Name": "Muhammad",
    "Last Name": "Ahmed",
    "Age": 15
}
p = Person.model_validate(data)
print(p)



