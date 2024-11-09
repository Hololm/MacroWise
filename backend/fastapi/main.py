from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.user import User
app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue.js vite default server port
    allow_credentials=True, # allow cookies
    allow_methods=["*"], # allow all methods
    allow_headers=["*"], # allow all headers
)
@app.get("/") # tells FastAPI that this function is called when the user goes to the path /
async def root():
    print("hello world")
    return {"message": {
        "message_1": "Hello World",
        "message_2": "nikhil nugra"
        }
    } # return content as json

print("Hello World")