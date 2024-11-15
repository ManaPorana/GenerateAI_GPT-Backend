import google.generativeai as genai
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ตั้งค่า API Key
# genai.configure(api_key="")

# ใช้โมเดล gemini-1.5-pro
MODEL_NAME = "gemini-1.5-pro"  

@app.route("/result", methods=['POST'])
def generate_story():
    data = request.get_json()
    prompt = f"""สร้างชุดของ Test Case สำหรับกรณีทดสอบ ให้มีเอียดต่อไปนี้ (เว้นบรรทัด) 
                วัตถุประสงค์: จุดประสงค์ของการทดสอบ (เว้นบรรทัด)
                เงื่อนไขก่อนการทดสอบ: เงื่อนไขหรือการตั้งค่าที่ต้องทำก่อนการทดสอบ (เว้นบรรทัด)
                ผลลัพธ์ที่คาดหวัง: ผลลัพธ์หรือพฤติกรรมที่คาดว่าจะเกิดขึ้นหลังจากทำขั้นตอนตามที่กำหนด (เว้นบรรทัด)
                เงื่อนไขหลังการทดสอบ: การเปลี่ยนแปลงใด ๆ ที่เกิดขึ้นในระบบหลังจากการทดสอบ
                ของข้อมูลต่อไปนี้ {data['occupation']} {data['causeOfDeath']} {data['placeOfDeath']} {data['deceasedAge']}"""

    try:
        # เรียกใช้งานโมเดลผ่าน google.generativeai
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt,generation_config = genai.GenerationConfig(max_output_tokens=350))

        # ตรวจสอบผลลัพธ์
        return jsonify({"result": response.text})

    except Exception as e:
        print("Request error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
