FROM python:3.9 

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

# 檔案目的 : 構建鏡像，構建的指令則是docker-compose.yml裡的build
# 參考網址 : https://hjy-dev.github.io/2020/02/23/Dockerfile%E8%AF%AD%E6%B3%95%E6%A2%B3%E7%90%86%E5%8F%8A%E5%AE%9E%E8%B7%B5/#%E4%BD%A0%E5%BF%85%E9%A1%BB%E7%9F%A5%E9%81%93%E7%9A%84Dockerfile