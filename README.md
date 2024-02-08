# YOLOv8-Segmentation-Agro-Inspector-Vineyard
Neural network for a mobile robot inspector in a vineyard
Neural network for a mobile robot inspector in a vineyard
Agrobot tasks:

Movement:
- detection and independent movement in the rows of the vineyard;
- detection of grape trunks - bushes;
- detection of pillars and supports;
- detection of the presence of humans and animals for security purposes;

Vineyard inspection:
- detection of grape diseases based on the condition of leaves;
- detecting vine growth and drawing up a pruning plan;

Work in the vineyard:
- independent movement along the rows and spraying;
- movement behind employees in the “follow me” mode;
- security functions;

------------------------------------------------
# Software environment for training the model - Ultralytics
https://github.com/ultralytics/ultralytics

Models trained: yolov8n-seg.pt, yolov8m-seg.pt, yolov8s-seg.pt

Model prediction results:
![Иллюстрация к проекту](https://github.com/vaavdeev/YOLOv8-Segmentation-Agro-Inspector-Vineyard/blob/main/images/Vineyard_7.jpg)

As an experiment, we did two options:
- training only in detecting the road between rows;
- training in detecting roads between rows, pillars, bushes...
