from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True) #ORM mode

    id: int | None = None
    email: str 


# We don't want to return the password when returning a user,
# that is why UserIn inherits from User and not the other way 
# around.

class UserIn(User): 
    password: str