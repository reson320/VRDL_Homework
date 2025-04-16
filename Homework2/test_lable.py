import os
import json
from PIL import Image

test_dir = './test'
output_json = './test.json'

images = []
for fname in os.listdir(test_dir):
    if not fname.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue

    base_name = os.path.splitext(fname)[0]

    try:
        image_id = int(base_name)  # 假設檔名為 "1.png", "2.png"
    except ValueError:
        print(f"Warning: Skipping non-numeric filename {fname}")
        continue

    path = os.path.join(test_dir, fname)
    try:
        with Image.open(path) as img:
            width, height = img.size
    except:
        print(f"Warning: Cannot open image {fname}")
        continue

    images.append({
        "id": image_id,
        "file_name": fname,
        "width": width,
        "height": height
    })

# 按照 id 升序排序
images = sorted(images, key=lambda x: x['id'])

json_dict = {
    "images": images,
    "categories": []  # 可留空
}

with open(output_json, 'w') as f:
    json.dump(json_dict, f, indent=4)

print(f"test.json generated with {len(images)} images. Sorted by id.")
