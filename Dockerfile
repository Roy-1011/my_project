# 使用 Python 3.9 作為基底映像檔
FROM python:3.9

# 設置工作目錄
WORKDIR /app

# 複製 requirements.txt 到容器中
COPY requirements.txt .

# 安裝必要的套件
RUN pip install --no-cache-dir -r requirements.txt

# 複製當前目錄的所有檔案到容器中
COPY . .

# 開放 8001 埠
EXPOSE 8001

# 設置容器啟動時執行的指令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
