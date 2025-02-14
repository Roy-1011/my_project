# 指定基礎鏡像 : 使用Python 3.9作為基底映像檔(容器內使用Python 3.9作為基礎執行環境)
# 鏡像 : 相當於容器的藍圖，定義了容器的內容和運行環境，包含應用程式、依賴項、配置文件、執行環境等所有必需的內容
# 每次啟動容器時，都能從鏡像開始，保證容器間的一致性
FROM python:3.9 

# 設置工作目錄(容器內的目錄，如果目錄不存在會自動創建)
WORKDIR /app

# 複製requirements.txt到容器中，每次執行時，如果這個檔案沒變，Docker就會直接使用快取(上一次執行儲存的結果)
COPY requirements.txt .

# 構建鏡像時運行的Shell命令(再命令前面加上RUN):安裝必要的套件 
# "--no-cache-dir"可以避免保存在構建Docker鏡像時被保存下來的文件，減少鏡像的大小。
# "-r"是從文件中讀取的意思，是pip install命令的一個選項
# 如果requirements檔案沒有變，就會直接取用快取，沒有上面的COPY的話會因為這個檔案還沒被複製進來容器找不到這個文件導致構建失敗
RUN pip install --no-cache-dir -r requirements.txt

# 複製my_project的所有檔案到容器的app目錄中(第一個.代表宿主機的當前目錄(my_project)，第二個則是WORKDIR指定的目錄)
# 這次的COPY檢查代碼是否有變化，即使有變，也不會重新安裝Python套件
# 用兩次COPY的最終目的就是為了讓這個COPY在RUN之後，讓容器不會重新安裝Python套件
COPY . .

# 聲明容器型的服務端口 : 開放 8001 埠
EXPOSE 8001

# 指定啟動容器時執行的Shell命令
# 這是JSON格式，會把命令和參數分開，比起Shell指令可以更好地指定命令和多個參數
# 第一個元素是命令，其餘都是參數，按順序依次傳遞給命令
# 意義 : 容器啟動時，執行uvicorn命令，並設定以下參數 ; main:app告訴uvicorn應用程序是main.py中的app對象
# host跟0000代表應用程序可以從任何IP地址訪問，而不只是容器內部 ; port 8001設置應用程序的端口為8001
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

# 檔案目的 : 構建鏡像，構建的指令則是docker-compose.yml裡的build
# 參考網址 : https://hjy-dev.github.io/2020/02/23/Dockerfile%E8%AF%AD%E6%B3%95%E6%A2%B3%E7%90%86%E5%8F%8A%E5%AE%9E%E8%B7%B5/#%E4%BD%A0%E5%BF%85%E9%A1%BB%E7%9F%A5%E9%81%93%E7%9A%84Dockerfile