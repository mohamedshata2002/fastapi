from fastapi import HTTPException, Response ,status,APIRouter,Depends
from app.database import get_db
from sqlalchemy.orm import Session
from  app.tables import *
from app.schemea import *
from app.utils import Hash

router = APIRouter(prefix="/user",tags=["User"])


@router.get("/test")
def test( db: Session = Depends(get_db)):
    result = db.query(User).all()
    print(result)
    return{"status":result}
@router.post("/create",status_code=status.HTTP_201_CREATED)
def create_post(user:create_user,db: Session = Depends(get_db)):
    user.password = Hash(user.password)
    result = User(**user.dict())
    db.add(result)
    db.commit()
    db.refresh(result)
    # cursor.execute("""INSERT INTO Users (name,price,is_sale) Values  (%s,%s,%s) returning * """,
    #                 (user.name,user.price,user.is_sale))
    # cursor.fetchone()
    # con.commit()
    return {"result":result}

@router.get("/get/{id}",response_model=view_user)
def test(id,db: Session = Depends(get_db)):
    data= db.query(User).filter(User.id==id).first()
    
    # cursor.execute(f"""SELECT * FROM UserS WHERE ID ={id}""")
    # data = cursor.fetchall()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No user there")
    return data
@router.delete("/delete/{id}")
def delete_post(id,db: Session = Depends(get_db)):
    # cursor.execute(f"""Delete from Users where id={id} returning *""")
    # data = cursor.fetchone()
    # con.commit()
    
    data= db.query(User).filter(User.id==id)
    if data.first() ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No user with that id")
    data.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
@router.put("/update/{id}",response_model=view_user)
def update_user(id:int,user:create_user,db: Session = Depends(get_db)):
    # cursor.execute("""Update Users set name = %s ,price =%s ,is_sale =%s where id= %s returning *""",
    #                 (user.name,user.price,user.is_sale,id))
    # data = cursor.fetchone()
    # con.commit()
    data= db.query(User).filter(User.id==id)
    if data.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No user with that id")
    data.update(user.dict(),synchronize_session=False)
    db.commit()
    return data.first()
