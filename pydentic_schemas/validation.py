from pydantic import BaseModel
from pydantic import ValidationError
from typing import Optional
from typing import List

from main import User


class PydantUsers(BaseModel):
    ID: 'int'
    FirstName: 'str'
    LastName: 'str'
    Phone: 'int'
    Email: 'str'


input_json = User
try:
    user = User.external_data(input_json)
except ValidationError as e:
    print(e.json())
