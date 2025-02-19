from fastapi import FastAPI 
from fastapi import HTTPException
from pydantic import BaseModel 
from pymysql.cursors import DictCursor
import jwt
import datetime
from database import get_connection  
from fastapi import APIRouter
import uvicorn 

# JWT設定
SECRET_KEY = "secretkey"
ALGORITHM = "HS256"

app = FastAPI() 

@app.get("/") 

def read_root(): 
    return {"message": "Hello, world!"} 
if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=8001)

router = APIRouter()

class LoginRequest(BaseModel): # 定義一個Pydantic模型LoginRequest，檢查從使用者端發送過來的資料結構
    email: str
    password: str 

# 產生 JWT Token 的函式
def create_jwt_token(email: str):
    expire = datetime.datetime.utcnow() + datetime.timedelta(days=30)  
    not_before = datetime.datetime.utcnow()  # Token 立即生效
    payload = {
        "sub": email,  
        "iss": "my_app",  
        "exp": expire,  
        "nbf": not_before  
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/login") 

def login(request: LoginRequest): 
    connection = get_connection()  
    print("資料庫連線成功:", connection)

    with connection.cursor(DictCursor) as cursor:
        cursor.execute("SELECT email, password FROM account WHERE email = %s", (request.email,))
        user = cursor.fetchone()  

    connection.close()

    if user is None or request.password != user["password"]:
        raise HTTPException(status_code=400, detail="Email 或密碼錯誤")

    # 產生JWT Token
    token = create_jwt_token(user["email"])
    return {"token" : token} 
    