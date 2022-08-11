# FastAPI

* **How to run**
    * **Step 1: Install Python Packages**
        * > pip install -r requirements.txt
    * **Step 2: Run by uvicorn (Localhost)**
        * > uvicorn main:app --reload
        * Default host = 127.0.0.1, port = 8000
    * **Step 3: Test your API using Swagger UI**
        * http://127.0.0.1:8000/docs

## Indtroduction
TIOBE編程社區指數是一種衡量程式語言流行度的標準。
- `/random`
  - 顯示任一TIOBE指標
- `/top5`
  - 顯示前五TIOBE指標
- `/show-all`
  - 顯示前二十TIOBE指標
- `/add-student`
  - 新增學生資料
    - name
    - gender
    - birth
    - programming language (可選)
  - 儲存至 `student.json`
- `/show-students`
  - 顯示所有學生資料
  - 讀取 `student.json`
- `/upload`
  - 上傳檔案