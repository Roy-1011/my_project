# FastAPI Docker 環境搭建

## 專案簡介
這是一個基於 FastAPI 的簡單後端伺服器，目前已經完成了基本的環境建置，未來會擴展為完整的 Restful API。

## 安裝項目
- **Python 3.13.2** - 主要開發語言
- **VSCode** & **Dev containers** - 開發環境與容器化開發工具
- **Docker** & **Docker Desktop** & **WSL 2** - 容器管理與 Linux 子系統(適用於 Windows )
- **FastAPI** & **Uvicorn** - Web 框架與 ASGI 伺服器
- **git 2.47.1.windows.2** - 版本控制工具

### 安裝步驟
1. **安裝 Python**  
   - 下載 Python : [Python 官方下載頁面](https://www.python.org/downloads/windows/) 
   - 根據電腦的系統類型決定要下載 Windows installer (64-bit) 或是 (32-bit)  

2. **安裝 VSCode 和 Dev Containers**  
   - 下載 VSCode : [VSCode 官方下載頁面](https://code.visualstudio.com/download)  
   - 在 VSCode 安裝 Dev Containers 擴充功能  

4. **安裝 Docker 和 WSL 2**  
   - 下載並安裝 Docker Desktop : [Docker Desktop 官網](https://www.docker.com/products/docker-desktop/)  
   - 安裝 WSL : 開啟 PowerShell(管理員模式)並輸入 wsl --install(該命令會自動下載 WSL 和 Ubuntu，
     如果想選擇其他 Linux 發行版，需要手動設置。)
   - 啟用 WSL 2 並設定為預設後端 : 在 PowerShell(管理員模式)輸入 wsl --set-default-version 2
   - 檢查 WSL 版本 : 繼續輸入 wsl --list --verbose ，這樣可以確認 Ubuntu 是不是使用 WSL 2                              

5. **安裝 FastAPI 和 Uvicorn**  
   請確定你的 requirements.txt 已經寫入 fastapi 和 uvicorn
   - 安裝 FastAPI 和 Uvicorn : 
       1. 在專案資料夾中啟動Docker容器 : 開啟 PowerShell 輸入 cd <專案資料夾名稱>，再輸入 docker-compose up --build -d
       2. 查看正在運行的容器名稱 : 輸入 docker ps 並記住 IMAGE 顯示 unicorn 那行 NAME 下面的名字(容器名稱)
       3. 進入容器 : docker exec -it <容器名稱> bash
       - 進入容器後，會處於容器的命令行，可以在這裡安裝所需的 Python 套件
       4. 在容器內安裝 FastAPI 和 Uvicorn : 輸入pip install fastapi uvicorn

6. **安裝 git**
   - 下載 git : [git 官方下載頁面](https://git-scm.com/downloads) 
   - 檢查是否下載成功 : 打開 PowerShell 輸入git --version
   - 初始化 git 儲存庫 : 輸入 git init

## 上傳專案至GitHub
   **首次上傳**
   - 建立遠端 GitHub 儲存庫，並將本地儲存庫與 GitHub 進行關聯：在專案資料夾輸入 
     git remote add origin https://github.com/GitHub上的使用者名稱/GitHub上的儲藏庫名稱.git
   - 查看當前分支名稱 : 輸入 git branch (確認有之後就不用再查看了)
   **沒有顯示任何分支的話**
   - 創建一個分支 : 輸入 git checkout -b main(這裡設分支名稱為main)
   **不是首次上傳 or 有顯示分支的話**
   1. 將文件添加到暫存區 : 在專案資料夾內輸入 git add .
   2. 針對這次上傳進行一些說明 : 輸入 git commit -m "敘述"
   3. 查看暫存區的文件 : 輸入 git status
   4. 把專案推送到 GitHub 上的 main 分支 : 輸入git push -u origin main
   - 這樣應該就能夠在你的 GitHub 上看到你上傳的專案了

## 啟動專案
1. 打開Docker Desktop
2. 在專案資料夾內輸入 docker-compose up --build -d
3. 輸入 docker ps 確認容器是否運行
4. 進入 http://localhost:8001/docs 查看API文件(其中的8001是由自己設定的端口號)

## 停止專案
- 輸入 docker-compose down

## 目錄結構
my_project/
- **devcontainer.json**  # 用來配置 VSCode 中的開發環境，讓開發者容器中進行開發
- **explaindevcontainer.txt** # 因為json文件不支持加註解，因此創了這個文字檔用來幫devcontainer.json加註解
- **docker-compose.yml** # 管理容器的設定
- **Dockerfile** # 建立 Docker 映像
- **main.py** # FastAPI 的入口點
- **readme.md** # 專案說明文件
- **requirements.txt** # Python 依賴套件

時間紀錄 : 2025/2/15 11:41