from fastapi import FastAPI # FastAPI是用來創建Web應用程式的核心類別
# from fastapi : 表示從fastapi這個Python套件庫中匯入內容
# import FastAPI : 這是將FastAPI類別引入到程式碼中

import uvicorn # 匯入uvicorn，這是用來啟動FastAPI應用程式的ASGI伺服器

app = FastAPI() # app是變數名稱，FastAPI()是創建FastAPI類別的實例。實例是指基於某個類別創建的具體物件，用來實際操作

@app.get("/") # 這是裝飾器(decorator)，用來標註一個函數是處理指定路由的HTTP請求。這裡是HTTP GET請求
# @在Python中用來表示裝飾器，本質上是一種函數，能在不修改函數本身的情況下，增加額外的功能
# get表示這個函數處理的是GET請求。GET是HTTP協議中的一個方法，通常用來獲取資源或數據
# "/"這是指定路徑。/ 代表根路徑，意味著當用戶訪問網站的主頁(ex. http://localhost/)時，會觸發這個函數

def read_root(): # def是Python中定義函數的關鍵字
    return {"message": "Hello, world!"} 
# read_root() : 函數名稱為read_root，可以隨意命名。當用戶訪問根路徑 / 時，FastAPI 會調用這個函數來處理該請求。

if __name__ == "__main__": # 這是一個Python標準的檢查方法，確保只有當這個檔案被"直接執行"時，才會運行下面的程式碼。
    # __name__是一個特殊變數，在直接運行這個檔案時，__name__ 的值會是 "__main__"
    uvicorn.run(app, host="0.0.0.0", port=8001)
# uvicorn.run()函數用來啟動ASGI伺服器，Uvicorn是一個高效能的Python 伺服器，它支持非同步操作
# 這裡run()函數會啟動伺服器來運行FastAPI應用app
# app是傳入的FastAPI實例，告訴Uvicorn這個伺服器要運行的應用程式是app
# host="0.0.0.0"這個參數設定伺服器的主機地址，0.0.0.0代表這個伺服器會接受來自任何IP地址的請求
# port=8001這個參數設定伺服器監聽的端口為8001

# 檔案目的 : 負責創建和啟動FastAPI應用程式，並處理外部的HTTP請求