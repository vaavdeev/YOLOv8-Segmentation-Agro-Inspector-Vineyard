from ultralytics import YOLO
model = YOLO('yolov8m-seg-custom-11.pt')
model.predict(source = "7.mp4", show=True, save=True, conf=0.5, show_labels=True, boxes=True)