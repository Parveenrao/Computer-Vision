"""" 
=> What is Computer-Vison-System-Design 

     -> A computer vision system is the entire pipeline that takes input from camera ,
        process it , make decision and delivers result to user or other system

     -> Why System Design Matters 

         Suppose yolo model achieve 95% mAP

            But 

            -> Camera discount 
            -> Network fails 
            -> GPU overload 
            -> Alert give 30 second later
            -> Database crash

       -> product fails even though the model is good 

       -> industry focus on

           1. Reliability 
           2. Scalability 
           3. Latency 
           4. Cost 
           5. Mantainability 

        not just model accuracy

=> Core Components Of Any CV System 

   1. Data sources 

      input come from 

       -> CCTV camera 
       -> IP camera 
       -> Mobile phones 
       -> Drones 
       -> Dashcam

     Example => A 1080p camera running at 30FPS
 
   2. Frame Acquisition 

      -> System Capture frame from the video stream

         Camera -- RTSP stream -- Opencv/Gs-streamer  -> Frames 

   3. Pre-processing 

       -> before inference 

          1. Resize 
          2. Normalize 
          3. Color conversion 
          4. Denoising 

   4. Inference Engine 

       YOLOv8 
       YOLOv11
       Faster R-CNN
       SSD

   5. Post-Processing       

       -> Raw prediciton are cleaned 

       -> NMS 
       -> Confidence thresholding 

       -> Co-ordinate conversion

   6. Tracking Layer

      -> Detection answer 

         What object exist now 

         Tracking answer -> Is this same person as before 

   7. Busniess Logic 

       This is where actual product lives 

       -> Shoplifting sytem 

          person picks item -> Leaves store -> no payment


          This layer create business value 

   8. Storage

      -> Store 

        Images 
        Videos 
        Events 
        Metadata

   9. API layer 

      -> Allow other application to use result

         GET/detection 

         Return recent detections 

   10. User Interface 

        -> Dashboard showing 

          1. Live video 
          2. Bounding box 
          3. Alerts
          4. Reports 

-----------------------------------------------------------------------



=> FLOW    


       Camera
         ↓
     Frame Capture
         ↓
     Preprocessing
         ↓
     YOLO Detection
         ↓
     Tracking
         ↓
     Business Rules
         ↓
      Database
         ↓
      Dashboard





"""