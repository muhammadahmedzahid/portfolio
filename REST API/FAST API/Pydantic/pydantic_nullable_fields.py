from pydantic import BaseModel
from pydantic import ValidationError

from typing import Union, Optional


# Here Actually we are doing class inheritance.
class Person(BaseModel):
    # We can define optional parameter like this.
    first_name: str | None = None
    # This is also another option to display optional parameters.
    last_name: Union[str | None] = None
    # We make this optional but if you look into model fields it is still showing mandatory field.
    age: Optional[int]
    # Below is how you can field optional.
    lucky_number: list[int] = []


print(Person.model_fields)
