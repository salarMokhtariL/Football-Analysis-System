from ultralytics import YOLO

model = YOLO('yolov8s')

results = model.predicts('input_video/08fd33_4.mp4', save=True)
print(results[0])
print('-------------------------')
for box in results[0].boxes:
    print(box)