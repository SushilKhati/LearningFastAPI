from fastapi import FastAPI
from routers import product,seller,login
import models
from database import engine
import os
from fastapi.middleware.cors import CORSMiddleware
os.system('cls')

#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# below line Initializes API and All routes (@app.get, @app.post) attach to this
app = FastAPI(
        # Meta data About API
        title="Products API", # Set title in the api docs
        description="An API to interact with Products and Sell",
        version="0.1",
        terms_of_service="http://google.com",
        contact={
            "Developer Name":"Sushil Khati",
            "website":"http://google.com",
            "email":"dummy@gmail.com"
        },
        license_info={
            "name":"Xyz",
            "url":"http://google.com"
        },
        docs_url="/apidocs", # this provide the link of api docs after local url
        redoc_url=None, # redoc url get disabled
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine) # “Create all tables defined in models if they don’t exist”
app.include_router(product.router)
app.include_router(seller.router)
app.include_router(login.router)