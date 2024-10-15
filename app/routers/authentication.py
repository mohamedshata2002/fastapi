from fastapi import HTTPException, Response ,status,APIRouter,Depends
from app.database import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from  app.schemea import *
from app.utils import *
from  app.tables import *
from app.othen import create_acess_token
router = APIRouter(tags=["authentication"])

@router.post("/login",response_model=Token_response)
def login(cred:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user =  db.query(User).filter(User.email==cred.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")
    if not vertify(cred.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")
    access_token = create_acess_token(data={"user_id":user.id})
    token ={"token":access_token,"token_type":"bearer"}
    
    return token