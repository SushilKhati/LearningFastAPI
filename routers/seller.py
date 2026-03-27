from fastapi import APIRouter
from sqlalchemy.orm import Session  # This represents a database transaction/session
from fastapi.params import Depends # It allows you to automatically provide things like DB sessions to your endpoints
import models,schemas
from fastapi import status,Response,HTTPException
from database import get_db

router = APIRouter(
    tags=["Sellers"],
    prefix="/seller"
)

@router.post('/',status_code=status.HTTP_201_CREATED)
# insert  data into the table
def add_seller(request:schemas.Seller,db : Session = Depends(get_db)):
    #hashpwd = pwd_context.hash(request.password)

    new_seller = models.Seller(
        name = request.name,
        email = request.email,
        password = request.password
    )
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return "Seller Details Added successfully"

@router.get('/{id}',response_model=schemas.DisplaySeller)
# update data into the table
def get_seller(id,response:Response,db: Session = Depends(get_db)):
    seller = db.query(models.Seller).filter(models.Seller.id == id).first()
    if not seller:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f"Seller with id {id} Not Found"
        )
    return seller

@router.get('/')
# update data into the table
def get_seller(db: Session = Depends(get_db)):
    sellers = db.query(models.Seller).all()
    return sellers