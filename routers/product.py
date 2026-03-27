from fastapi import APIRouter
from fastapi import status,Response,HTTPException
from sqlalchemy.orm import Session # This represents a database transaction/session
from fastapi.params import Depends# It allows you to automatically provide things like DB sessions to your endpoints
import models,schemas
from database import get_db
from .login import get_current_user

router = APIRouter(
    tags=["Products"],
    prefix="/product"
)

@router.post('/',status_code=status.HTTP_201_CREATED) 
# return 201 status in case of successfull req execution
# Tags helps to categorize or group the API
# add data into the table
def add_product(request:schemas.Product,db:Session = Depends(get_db)):
    # db:Session = Depends(get_db) - FastAPI will Call get_db() and Inject db automatically
    new_product = models.Product(
        name = request.name,
        description = request.description,
        price = request.price,
        seller_id = 1
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product) # Reloads object from DB
    return request

@router.get('/{id}',response_model=schemas.DisplayProduct) #response_model parameter is used to display only required details
# display all data from the table
def get_product(id: int, response:Response ,db:Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException( # raising exception in case details not found
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@router.delete('/{id}')
# display all data from the table
def delete_product(id: int, db:Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return f"Product Deleted ID: {id}"

@router.put('/{id}',tags=["Products"])
# perform update operation, Note we use request as parameter
def update_product(id: int,request:schemas.Product, db:Session = Depends(get_db)):
     product = db.query(models.Product).filter(models.Product.id == id)
     if not product:
         pass
     product.update(request.dict())
     db.commit()
     return f"Product Updates Id {id}"


@router.get('/')
# display all data from the table
def get_products(db:Session = Depends(get_db),current_user:schemas.Seller = Depends(get_current_user)):
    products = db.query(models.Product).all()
    return products
