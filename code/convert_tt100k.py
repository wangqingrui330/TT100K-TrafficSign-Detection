import json
import os
import random
from PIL import Image

json_path = r"D:\yolovProject\TT100K\annotations.json"
img_train_dir = r"D:\yolovProject\TT100K\data\train"
img_test_dir = r"D:\yolovProject\TT100K\data\test"
save_root = r"D:\yolovProject\tt100k_yolo"



class_map = {
    # 限速 0
    "t1":0,"t2":0,"t3":0,"t4":0,"t5":0,"t6":0,"t7":0,"t8":0,"t9":0,"t10":0,"t11":0,"t12":0,
    # 禁止通行 1
    "pn":1,"pb":1,
    # 直行转弯 2
    "pl0":2,"pl1":2,"pl2":2,"pl3":2,"pl4":2,"pl5":2,
    # 人行横道 3
    "p30":3,
    # 停车让行 4
    "p12":4
}


with open(json_path,"r",encoding="utf-8") as f:
    data = json.load(f)
all_img_info = data["imgs"]


train_img_names = [i for i in os.listdir(img_train_dir) if i.endswith((".jpg",".png"))]
test_img_names = [i for i in os.listdir(img_test_dir) if i.endswith((".jpg",".png"))]


random.seed(666)
val_ratio = 0.2
val_num = int(len(train_img_names)*val_ratio)
val_img_names = random.sample(train_img_names, val_num)
train_img_names_final = [x for x in train_img_names if x not in val_img_names]

def process_one_img(img_name, img_source_dir, save_img_dir, save_label_dir):
    src_img = os.path.join(img_source_dir, img_name)
    dst_img = os.path.join(save_img_dir, img_name)

    with open(src_img,"rb") as f1, open(dst_img,"wb") as f2:
        f2.write(f1.read())


    with Image.open(src_img) as img:
        w, h = img.size

    img_id = img_name.split(".")[0]
    img_info = all_img_info[img_id]
    objects = img_info["objects"]
    label_lines = []

    for obj in objects:
        label_tag = obj["category"]
        if label_tag not in class_map:
            continue
        cls_id = class_map[label_tag]
        xmin = obj["bbox"]["xmin"]
        ymin = obj["bbox"]["ymin"]
        xmax = obj["bbox"]["xmax"]
        ymax = obj["bbox"]["ymax"]
        # 转换YOLO归一化坐标
        xc = (xmin + xmax) / 2 / w
        yc = (ymin + ymax) / 2 / h
        bw = (xmax - xmin) / w
        bh = (ymax - ymin) / h
        line = f"{cls_id} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}"
        label_lines.append(line)


    if len(label_lines) == 0:
        os.remove(dst_img)
        return

    txt_name = img_name.replace(os.path.splitext(img_name)[1], ".txt")
    txt_path = os.path.join(save_label_dir, txt_name)
    with open(txt_path,"w",encoding="utf-8") as f:
        f.write("\n".join(label_lines))


print("正在处理训练集...")
for name in train_img_names_final:
    process_one_img(name, img_train_dir, os.path.join(save_root,"images/train"), os.path.join(save_root,"labels/train"))

print("正在处理验证集...")
for name in val_img_names:
    process_one_img(name, img_train_dir, os.path.join(save_root,"images/val"), os.path.join(save_root,"labels/val"))

print("正在处理测试集...")
for name in test_img_names:
    process_one_img(name, img_test_dir, os.path.join(save_root,"images/test"), os.path.join(save_root,"labels/test"))

print("✅ 数据集转换全部完成！")