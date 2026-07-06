from ultralytics import YOLO
model = YOLO("yolov5s.pt")
train_result = model.train(
    data="traffic.yaml",
    epochs=100,
    batch=16,
    imgsz=640,
    pretrained=True,
    device=0,
    patience=15,
    project="traffic_output",
    name="baseline_yolov5s",
    workers=0
)
print("基线训练完成，权重路径：traffic_output/baseline_yolov5s/weights/best.pt")