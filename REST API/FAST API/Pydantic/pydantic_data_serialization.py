from pydantic import BaseModel
from pydantic import ValidationError


# Here Actually we are doing class inheritance.
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

data = {
    "first_name":"Muhammad",
    "last_name":"Ahmed",
    "age":45
}

# If you want to pass your object as a dictionary.
p = Person.model_validate(data)
print(p)

data = '''{
    "first_name":"Muhammad",
    "last_name":"Ahmed",
    "age":45
}'''
# If you have a JSON string and you want to put inside an object then you can do that.
p = Person.model_validate_json(data)
print(p)
