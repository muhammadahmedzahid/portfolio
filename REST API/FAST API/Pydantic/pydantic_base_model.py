from pydantic import BaseModel

# Here Actually we are doing class inheritance.
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


person = Person(first_name="Muhammad", last_name="Ahmed", age=24)
print(person)


from pydantic import ValidationError

try:
    person = Person(first_name="Muhammad", last_name="25", age="42")
    # Below is the issue as it will ignore the type present in the base class be aware of it.
    person.age = "Ahmed"
    print(person)
except ValidationError as err:
    print(err)
