# Run yolo on image 

from ultralytics import YOLO

# load pre-trained model 

model = YOLO("yolov8n.pt")  # nano model fastest 

# Run  inference 

result = model("istockphoto-2188332763-1024x1024.jpg")

result[0].show()