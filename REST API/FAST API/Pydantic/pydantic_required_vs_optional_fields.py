from pydantic import BaseModel
from pydantic import ValidationError


# Here Actually we are doing class inheritance.
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


try:
    # Here you will get error because all the fields are mandatory.
    p = Person(first_name="Muhamamd")
except ValidationError as err:
    print(err)



class Person2(BaseModel):
    first_name: str
    last_name: str
    age: int=0
    
# And now if we look into fields which becomes optional and which becomes mandatory.

print(Person2.model_fields)
