from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from py_nmb import PyNMB

# Initialize FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize PyNMB
py_nmb = PyNMB()

@app.get("/nmb/api/v1")
async def root():
    return {"message": "Welcome to the NMB API"}

@app.post("/nmb/api/v1/login")
async def login(username: str, password: str):
    response = py_nmb.login(username,password)
    return response

@app.get("/nmb/api/v1/branches")
async def getBranches():
    response = py_nmb.getBranches()
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)