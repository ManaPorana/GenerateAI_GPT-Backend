
## สิ่งที่ควรเช็คก่อนใช้

ก่อนที่จะรัน API ให้เช็คก่อนว่ามีโปรแกรมต่อไปนี้หรือยัง:

- Python (>= 3.6)
- Flask (`pip install flask`)
- Flask-CORS (`pip install flask-cors`)
- ไลบรารี `dotenv` ของ Python (`pip install python-dotenv`)
- Gemini (`pip install google-generativeai`)

 สร้าง virtual environment (ไม่จำเป็น แต่แนะนำ):

```bash
python -m venv venv
```

 เปิดใช้งาน virtual environment:

   - บน Windows:

```bash
venv\Scripts\activate
```

   - บน macOS และ Linux:

```bash
source venv/bin/activate
```

 ติดตั้ง dependencies ที่จำเป็น:

```bash
pip install -r requirements.txt
```


แทนที่ `your_api_key_here` ด้วย OpenAI API key ของคุณ

## วิธีใช้

1. เริ่มต้นเซิร์ฟเวอร์ Flask:

```bash
python app.py
```

2. แอปพลิเคชันจะสามารถเข้าถึงได้ที่ `http://localhost:5000`.

