'''from fastapi import FastAPI
from pydantic import BaseModel # BaseModel是用來定義資料驗證模型的基礎類別
import pymysql
import jwt
import datetime
from database import get_connection  # 取得MySQL連線
from fastapi import APIRouter
from fastapi import HTTPException


# JWT設定
SECRET_KEY = "secretkey"
ALGORITHM = "HS256"

app = FastAPI()

router = APIRouter()

class LoginRequest(BaseModel): # 定義一個Pydantic模型LoginRequest，檢查從使用者端發送過來的資料結構
    email: str
    password: str # 資料型別設定為字串str

# 產生 JWT Token 的函式
def create_jwt_token(email: str):
    expire = datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # 設定 Token 1 小時後過期
    return jwt.encode({"sub": email, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/login") # 這個函式處理HTTP POST請求到/login路徑的端點

# 處理使用者登入
def login(request: LoginRequest): # 定義名為login的函示，他接收一個參數request，冒號後面是參數型別
    connection = get_connection()  # 取得資料庫連線
    print("資料庫連線成功:", connection)
    with connection.cursor() as cursor:
        cursor.execute("SELECT email, password FROM users WHERE email = %s", (request.email,))
        user = cursor.fetchone()  # 取得資料庫的使用者資料

    connection.close()

    # 如果沒有找到該email或密碼錯誤，回傳錯誤訊息
    if not user or request.password != user[1]:
        raise HTTPException(status_code=400, detail="Email 或密碼錯誤")

    # 產生JWT Token
    token = create_jwt_token(user["email"])
    return {"message" : "這則訊息會出現在哪裡呢ouo"} # 當login函是被呼叫時，會返回一個字典

# 負責驗證用戶(登入)並產生JWT   '''