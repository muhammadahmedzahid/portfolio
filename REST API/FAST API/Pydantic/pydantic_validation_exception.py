from pydantic import BaseModel
from pydantic import ValidationError


# Here Actually we are doing class inheritance.
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


try:
    person = Person(first_name="Muhammad", last_name=25, age="42")
    # Below is the issue as it will ignore the type present in the base class be aware of it.
    person.age = "Ahmed"
    print(person)
except ValidationError as err:
    exception = err
    print(err)
    # It will give you the error into dictionary.
    print(exception.errors())
    # This will convert your exception in JSON.
    print(exception.json())

