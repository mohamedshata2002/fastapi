from fastapi import HTTPException, Response ,status,APIRouter
from sqlalchemy import func
from app.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from  app.tables import *
from app.schemea import *
from app.othen import *
from typing import List
router = APIRouter(prefix="/items",tags=["Items"])


@router.get("/test")
def test( db: Session = Depends(get_db)):
    result = db.query(Product).all()
    print(result)
    return{"status":result}
@router.post("/create",status_code=status.HTTP_201_CREATED,)
def Create_item_(item:create_Item,db: Session = Depends(get_db),user_id:int = Depends(get_current_user)):
    print(user_id.id)
    result = Product(user_id=user_id.id,**item.dict())
    db.add(result)
    db.commit()
    db.refresh(result)
    # cursor.execute("""INSERT INTO products (name,price,is_sale) Values  (%s,%s,%s) returning * """,
    #                 (item.name,item.price,item.is_sale))
    # cursor.fetchone()
    # con.commit()
    return {"result":result}

# @router.get("/get/{id}",response_model=view_Item)
@router.get("/get/{id}",response_model=item_out)
def get_item(id,db: Session = Depends(get_db)):
    
    data= db.query(Product).filter(Product.id==id).first()
    result = db.query(Product,func.count(Vote.item_id).label("votes")).join(Vote,Product.id==Vote.item_id,isouter=True).group_by(Product.id).filter(Product.id==id).first()
    print(result)
    # cursor.execute(f"""SELECT * FROM PRODUCTS WHERE ID ={id}""")
    # data = cursor.fetchall()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No item there")
    return result
@router.delete("/delete/{id}")
def delete_post(id,db: Session = Depends(get_db),current_user_id:int = Depends(get_current_user)):
    # cursor.execute(f"""Delete from products where id={id} returning *""")
    # data = cursor.fetchone()
    # con.commit()
    data= db.query(Product).filter(Product.id==id)
    if data.first() ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No item with that id")
    elif data.first().user_id != current_user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized")
    data.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
@router.put("/update/{id}",response_model=view_Item)
def update_item(id:int,item:create_Item,db: Session = Depends(get_db),current_user_id:int = Depends(get_current_user)):
    # cursor.execute("""Update products set name = %s ,price =%s ,is_sale =%s where id= %s returning *""",
    #                 (item.name,item.price,item.is_sale,id))
    # data = cursor.fetchone()
    # con.commit()
    data= db.query(Product).filter(Product.id==id)
    if data.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No item with that id")
    elif data.first().user_id != current_user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized")
    result =item.dict()
    result["user_id"] = current_user_id.id
    data.update(result,synchronize_session=False)
    db.commit()
    return data.first()
