from fastapi import APIRouter,HTTPException,status,Depends
from fastapi.routing import request_response
from pydantic import schema
import schemas,models
from database import get_db
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags=["Authentication"],
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "4af32ccb6344090f30027cdfe113a1bfe5b2f722eecf48fd955db730f5416445"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20

def generate_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt


@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db: Session=Depends(get_db)):
    user = db.query(models.Seller).filter(models.Seller.name == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect username"
        )
    if user.password != request.password:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect Password"
        )  
    # Generate JWT  
    access_token = generate_token(
        data = {"sub":request.username}
    ) 
    return {"access_token":access_token,"token_type":"Bearer"}

def get_current_user(token:str = Depends(oauth2_scheme)):
    cred_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unauthorize user",
        headers = {"WWW-Authenticate":"Bearer"},
    )
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise cred_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise cred_exception


