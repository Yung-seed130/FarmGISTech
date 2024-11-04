from fastapi import Depends, status, HTTPException
from jwt_token import verify_token
from fastapi.security import OAuth2PasswordBearer
# from jose import jwt
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(data,credentials_exception)