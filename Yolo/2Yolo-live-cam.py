import cv2

import ultralytics

from ultralytics import YOLO

# load pre-trained model 

model = YOLO("yolov8n.pt")  # nano , fastest for real time 


cap = cv2.VideoCapture(0)   # (0 = default cam)


while True:

    ret , frame = cap.read()

    if not ret:
        break


    # Run yolo on frame 

    result = model(frame)


    # annotated frame 

    annotated_frame = result[0].plot()

    # show output 

    cv2.imshow("Yolo Live Detection" , annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


