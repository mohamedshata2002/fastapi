from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.othen import get_current_user
from app.schemea import vote_response
from app.tables import Vote ,Product
router = APIRouter(tags=["Vote"],prefix="/vote")

@router.post("/",status_code=status.HTTP_201_CREATED)
def voteing(vote:vote_response,db: Session = Depends(get_db),current_user: int = Depends(get_current_user)):
    
    vote_found = db.query(Vote).filter(Vote.item_id == vote.item_id, Vote.user_id == current_user.id).first()
    data= db.query(Product).filter(Product.id == vote.item_id).first()
    if data :
        if vote.dir == 1:
            if vote_found :
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already voted on post {vote.item_id}")
            print(vote_found)
            new_vote = Vote(item_id=vote.item_id, user_id=current_user.id)
            db.add(new_vote)
            db.commit()
            return {"message": "successfully added vote"}
        elif vote.dir == 0 :
            if vote_found:
                db.delete(vote_found)
                db.commit()
                return {"message": "successfully remove vote"}
            else:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vote does not exist")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No product with that id")