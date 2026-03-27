from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy DB data
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 20000}
]

@app.get("/products")
def get_products():
    return products

@app.post("/trigger-bot")
def trigger_bot():
    # Here you trigger your bot logic
    return {"status": "Bot triggered successfully"}
