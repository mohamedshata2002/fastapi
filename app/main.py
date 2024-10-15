from fastapi import FastAPI 
from app.routers import items ,user ,authentication,vote
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# while True:
  
#     try:
#         con= db.connect(host="localhost",database="fastapi",user="postgres",password="master mas",cursor_factory=RealDictCursor)
#         print("The database is connected")
#         cursor = con.cursor()
#         break
#     except Exception as error:
#         print("Failed to connect \n")
#         print("The error is ",error)
#         time.sleep(2)
@app.get("/test")
def test():
    return "Hello world"
app.include_router(items.router)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(vote.router)


