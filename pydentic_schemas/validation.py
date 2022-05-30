from pydantic import ValidationError
from pydantic import BaseModel
from pydantic import EmailStr

from main import User


class PydantUsers(BaseModel):
    ID: 'int'
    FirstName: 'str'
    LastName: 'str'
    Phone: 'int'
    Email: 'EmailStr'


input_json = str(User)

user = PydantUsers.parse_raw(input_json)

try:
    user = User.external_data(input_json)
except ValidationError as e:
    print(e.json())
