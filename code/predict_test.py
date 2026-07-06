from ultralytics import YOLO

model = YOLO(
    r"runs/detect/traffic_output/baseline_yolov5s/weights/best.pt"
)

model.predict(
    source=r"TT100K_YOLO/images/test_normal2",
    save=True,
    name="normal_result2"
)

model.predict(
    source=r"TT100K_YOLO/images/test_dark2",
    save=True,
    name="dark_result2"
)

model.predict(
    source=r"TT100K_YOLO/images/test_blur2",
    save=True,
    name="blur_result2"
)

print("全部检测完成")