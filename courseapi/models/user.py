from pydantic import BaseModel


class User(BaseModel):
    id: int | None = None
    email: str


# We don't want to return the password when returning a user,
# that is why UserIn inherits from User and not the other way 
# around.

class UserIn(User): 
    password: str