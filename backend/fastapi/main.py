from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.user import User
from pydantic import BaseModel

app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue.js vite default server port
    allow_credentials=True,  # allow cookies
    allow_methods=["*"],  # allow all methods
    allow_headers=["*"],  # allow all headers
)


# request validation
class UserInput(BaseModel):
    name: str
    height: int
    weight: int
    age: int
    gender: str


@app.post("/login") # register/login
async def calculate_bmi(user_input: UserInput):
    # Create User instance
    user = User(
        name = user_input.name,
        height = user_input.height,
        weight = user_input.weight,
        age = user_input.age,
        gender = user_input.gender
    )

    # Calculate BMI and body fat percentage
    user.calculate_bmi()
    user.calculate_body_fat_percentage()

    return {
        "name": user.name if user.name else None,
        "bmi": round(user.bmi, 1) if user.bmi else None,
        "body_fat_percentage": round(user.body_fat_percentage, 2) if user.body_fat_percentage else None
        }


@app.get("/home") # dashboard page
async def root():
    return {
        "message": {
        "message_1": "Hello World",
        "message_2": "nikhil nugra"
    }
    }
