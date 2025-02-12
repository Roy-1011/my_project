from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

# 在腳本中啟動 Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
