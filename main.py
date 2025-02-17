from fastapi import FastAPI 
# from auth import router as auth_router
from fastapi import HTTPException
from pydantic import BaseModel # BaseModel是用來定義資料驗證模型的基礎類別
import pymysql
import jwt
import datetime
from database import get_connection  # 取得MySQL連線
from fastapi import APIRouter
import uvicorn 

# JWT設定
SECRET_KEY = "secretkey"
ALGORITHM = "HS256"

app = FastAPI() 

# app.include_router(auth_router)

@app.get("/") 

def read_root(): 
    return {"message": "Hello, world!"} 
if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=8001)

router = APIRouter()

class LoginRequest(BaseModel): # 定義一個Pydantic模型LoginRequest，檢查從使用者端發送過來的資料結構
    email: str
    password: str # 資料型別設定為字串str

# 產生 JWT Token 的函式
def create_jwt_token(email: str):
    expire = datetime.datetime.utcnow() + datetime.timedelta(days=30)  # 設定Token 30天後過期
    not_before = datetime.datetime.utcnow()  # Token 立即生效
    payload = {
        "sub": email,  
        "iss": "my_app",  # 發行者
        "exp": expire,  # 過期時間
        "nbf": not_before  # 不早於此時間生效
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/login") # 這個函式處理HTTP POST請求到/login路徑的端點

# 處理使用者登入
def login(request: LoginRequest): # 定義名為login的函示，他接收一個參數request，冒號後面是參數型別
    connection = get_connection()  # 取得資料庫連線
    print("資料庫連線成功:", connection)
    with connection.cursor() as cursor:
        cursor.execute("SELECT email, password FROM account WHERE email = %s", (request.email,))
        user = cursor.fetchone()  # 取得資料庫的使用者資料

    connection.close()

    # 如果沒有找到該email或密碼錯誤，回傳錯誤訊息
    if not user or request.password != user[1]:
        raise HTTPException(status_code=400, detail="Email 或密碼錯誤")

    # 產生JWT Token
    token = create_jwt_token(user["email"])
    return {"token" : token} # 當login函是被呼叫時，會返回一個字典
    