""" 
=> Data Flow Design 

   -> It shows how data moves through entire system

   -> Where does the data come from , what happens to it , and where does it go next 

---------------------------------------------------------------------------------------

=> Example Person Detecting System 
  
    -> Suppose we have CCTV and want to detect people

     Camera -> Frame Capture Device -> Preprocessing -> Object Detection Model -> Post Processing 

     -> Alert / Database / API -> Dashboard


   Step 1. Data Source 

      -> Data enter the system 

      1. CCTV camera 
      2. Mobile camera 
      3. Drone camera 
      4. Uploaded Image 

     Ouput -> Raw Image / Video Frame

   Step 2.  Frame Capture

     1. Video is converted into frames 


        30 FPS Video , Frame 1 -> Frame 2 --> Frame 3 --> Frame 4


        -> Process every frame , Every 5Th frame , Every 1 second   

        Decision affect cost and latency

   Step 3. Preprocessing 

         -> Prepare iamge 
         -> Normalize pixels 
         -> Convert color formats 
         -> Remove noise 


        1920 *  1080  ==> 640 * 640  Yolo accept this

    Step 4. Run AI Model 

        Image -> Yolo / DETR -> Predictions 


        This is the most expensive step 

    Step 5. Post Processing 

         -> Model Processing and cleanup


         Example -> Confidence threshold 
         NMS (Non-max supression)
         Tracking 

    Step 6. Busniess Logic 

       Now use CV result 

       Person detected -> Yes -> alert 

    Step 7. Storage 

        Store     

        -> Images 
        -> clip 
        -> detection result

        -> Logs 

    Step 8. Dashboard / API


       -> show result to user 

         Person count = 25                                          


         

"""