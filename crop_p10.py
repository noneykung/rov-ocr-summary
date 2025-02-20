import cv2
import os

# โหลดภาพต้นฉบับ
image_path = "temp/erored_img.png"
image = cv2.imread(image_path)

# สร้างโฟลเดอร์ temp ถ้ายังไม่มี
output_folder = "temp/crop"
os.makedirs(output_folder, exist_ok=True)


# พิกัดของผู้เล่น (x1, y1, x2, y2)
player_zones = [
    (145, 560, 710, 620),  # Player 1
    (145, 710, 710, 770),  # Player 2
    (145, 850, 710, 910),  # Player 3
    (145, 995, 710, 1055),  # Player 4
    (145, 1140, 710, 1200),  # Player 5
    (1170, 560, 1735, 620),  # Player 6
    (1170, 710, 1735, 770),  # Player 7
    (1170, 850, 1735, 910),  # Player 8
    (1170, 995, 1735, 1055),  # Player 9
    (1170, 1140, 1735, 1200),  # Player 10
]
'''

player_zones = [
    (380, 560, 710, 620),  # Player 1
    (380, 710, 710, 770),  # Player 2
    (380, 850, 710, 910),  # Player 3
    (380, 995, 710, 1055),  # Player 4
    (380, 1140, 710, 1200),  # Player 5
    (1410, 560, 1735, 620),  # Player 6
    (1410, 710, 1735, 770),  # Player 7
    (1410, 850, 1735, 910),  # Player 8
    (1410, 995, 1735, 1055),  # Player 9
    (1410, 1140, 1735, 1200),  # Player 10
]
'''

# Crop และบันทึกแต่ละโซน
cropped_paths = []
for i, (x1, y1, x2, y2) in enumerate(player_zones):
    cropped_img = image[y1:y2, x1:x2]  # Crop ภาพ
    save_path = os.path.join(output_folder, f"player_{i+1}.png")
    cv2.imwrite(save_path, cropped_img)  # บันทึกภาพที่ถูก Crop
    cropped_paths.append(save_path)

print(str(cropped_paths))