from ultralytics import YOLO
model = YOLO('yolov8s-seg-cost.pt')
model.predict(source = "031.png", show=True, save=True, conf=0.5, show_labels=True, boxes=True)