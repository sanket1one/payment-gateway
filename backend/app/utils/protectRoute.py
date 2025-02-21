from fastapi import Depends, Header, HTTPException , status
from sqlalchemy.orm import Session
from typing import Annotated, Union
from app.core.security.authHandler import AuthHandler
from app.services.userService import UserService
from app.core.database import get_db 
from app.db.schemas.user import UserOutput 


AUTH_PREFIX = 'Bearer '

def get_current_user(
        session: Session = Depends(get_db),
        authToken: Annotated[Union[str, None], Header()] = None
) -> UserOutput:
    print("Received authToken header:", authToken)
    auth_exception =  HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Authentication Credentials"
    )
    if not authToken:
        auth_exception.detail = "Not Authorized1"
        raise auth_exception
    
    if not authToken.startswith(AUTH_PREFIX):
        auth_exception.detail = "Bearer token missing"
        raise auth_exception

    payload = AuthHandler.decode_jwt(token=authToken[len(AUTH_PREFIX):])
    if payload and payload["user_id"]:
        try:
            user = UserService(session=session).get_user_by_id(user_id=payload["user_id"])
            return UserOutput(
                id = user.id,
                first_name = user.first_name,
                last_name = user.last_name,
                email = user.email
            )
        except Exception as error:
            raise error
    auth_exception.detail = "Authentication Failed"
    raise auth_exception
