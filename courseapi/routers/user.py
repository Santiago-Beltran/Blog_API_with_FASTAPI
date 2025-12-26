import logging
from fastapi import APIRouter, HTTPException, status
from courseapi.models.user import UserIn
from courseapi.security import get_user
from courseapi.database import database, user_table

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/register", status_code=201)
async def register(user: UserIn):
    if await get_user(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with that email already exists"
        )
    
    # STORING PASSWORD IN PLAIN TEXT FOR TESTING PURPOSES ONLY, THIS MUST BE CHANGED!
    query = user_table.insert().values(email=user.email, password=user.password)

    logger.debug(query)
    
    await database.execute(query)

    return {"detail": "User created."}