from pydantic import BaseModel
from pydantic import ValidationError
from main import User


class PydantUsers(BaseModel):
    ID: 'int'
    FirstName: 'str'
    LastName: 'str'
    Phone: 'int'
    Email: 'str'

input_json = User
try:
    user = User.parse_raw(input_json)
except ValidationError as e:
    print(e.json())