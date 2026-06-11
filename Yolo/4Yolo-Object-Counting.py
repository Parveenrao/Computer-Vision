""" 

=> Yolo-Object Counting 

    1. Basic Idea
       
        -> detect objects 
        -> check class
        -> count them 
        -> display count on screen

    2. Yolo Class IDs 

         yolov8  pretrained model use COCO dataset

         Person            0
         bicycle           1
         car               2
         motorbike         3



"""


from ultralytics import YOLO
import cv2


# load pre-trained model 

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("18447480-hd_1080_1920_60fps.mp4")

while True:
    ret , frame = cap.read()

    if not ret:
        break

    result = model(frame ,  imgsz=240)

    result = result[0]

    # get detections 

    boxes = result.boxes


    car_count = 0


    for box in boxes:
        cls_id = int(box.cls[0])  # class id 


        if cls_id == 2:  # car 

            car_count += 1

     # Draw result
    annotated_frame = result.plot()

    # Show count on screen
    cv2.putText(
        annotated_frame,
        f"Car Count: {car_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("YOLO Object Counting", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()        
