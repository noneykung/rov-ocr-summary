import os
import re
from PIL import Image
import pytesseract

# ตั้งค่า path ของ Tesseract OCR (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# โฟลเดอร์ที่เก็บภาพที่ Crop แล้ว
crop_folder = "temp/crop"

# ตรวจสอบว่ามีไฟล์ในโฟลเดอร์หรือไม่
if not os.path.exists(crop_folder):
    print(f"❌ Error: ไม่พบโฟลเดอร์ '{crop_folder}'")
    exit()

# ฟังก์ชัน OCR และจัดรูปแบบข้อมูล
def extract_numbers_from_ocr(text):
    # รวมข้อความหลายบรรทัดให้อยู่ในบรรทัดเดียว
    text = re.sub(r"\s+", " ", text).strip()

    # กรองเฉพาะตัวเลขและอักขระที่เกี่ยวข้อง
    text = re.sub(r"[^0-9/.]", " ", text)  # ลบตัวอักษรที่ไม่ใช่ตัวเลขหรือ `.` หรือ `/`

    # ลบช่องว่างเกินมา
    text = re.sub(r"\s+", " ", text).strip()

    return text

# Loop อ่านภาพ 10 ไฟล์ (player_1.png -> player_10.png)
ocr_results = []
for i in range(1, 11):  # อ่าน player_1.png ถึง player_10.png
    img_path = os.path.join(crop_folder, f"player_{i}.png")
    
    # ตรวจสอบว่าไฟล์มีอยู่จริงหรือไม่
    if not os.path.exists(img_path):
        print(f"⚠️ Warning: ไม่พบไฟล์ '{img_path}', ข้ามไป...")
        ocr_results.append((f"Player {i}", "ไม่มีข้อมูล"))  # เพิ่มค่าเริ่มต้น
        continue
    
    # เปิดภาพ
    img = Image.open(img_path)

    # OCR อ่านข้อความ (กำหนดค่าเริ่มต้นก่อน OCR)
    ocr_text = ""  # ป้องกันตัวแปรไม่ได้ถูกกำหนด
    try:
        ocr_text = pytesseract.image_to_string(img, lang="eng+tha")  # รองรับภาษาไทย
    except Exception as e:
        print(f"❌ Error: OCR ล้มเหลวที่ '{img_path}' - {e}")

    # บันทึกผลลัพธ์
    ocr_results.append((f"Player {i}", ocr_text.strip() if ocr_text else "OCR อ่านไม่สำเร็จ"))

# แสดงผล OCR
for player, text in ocr_results:
    print(f"📌 {player}:\n{text}\n{'-'*50}")
