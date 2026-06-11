""" 

=> Saving ouput Using Yolo 


"""


from ultralytics import YOLO

import cv2

# load model 

model = YOLO("yolov8n.pt")

# open webcam 

cap = cv2.VideoCapture(0)

# get video properties 

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Video writer (SAVE FILE)
out = cv2.VideoWriter(
    "yolo_output.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    20,
    (frame_width, frame_height)
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO inference
    results = model(frame)

    # Draw boxes
    annotated_frame = results[0].plot()

    # Show live
    cv2.imshow("YOLO Live", annotated_frame)

    # SAVE FRAME
    out.write(annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()