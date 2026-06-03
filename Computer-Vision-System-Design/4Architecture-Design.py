""" 
=> Architecture Design 

   -> It shows how different components of the system interact 

   -> For Computer Vision System 

     Camera -> Video Ingestion Service -> Alert Service -> Database / Dashboard 

-----------------------------------------------------------------------------------------

=> Graffiti Detection System 

   1. Camera layer 

       -> CCTV camera capture video
       -> Streams video continuously 

   2. Ingestion Layer 

      -> Receive video stream 
      -> Convert video into frames 

   3. Queue layer 

      -> Store frames temporarily     

      -> Common choice , Kafka , RabbitmQ

      -> Prevent overload when traffic spike

   4. Inference layer 

      -> Runs your detection model (YOLO)
      
      -> Produce 
           
          1. Bounding Box 
          2. Class labels 
          3. Confidence scores 

   5. Busniess Logic Layer 

        -> Check rules 

        -> Example 

            if grafitti detected for 3 consecutive frames -> trigger alert 

   6. Storage Layer 

       -> Store 

           Image  , Alerts , Logs , Metadata

   7. Dashboard Layer 

      -> Security team views detection 
      -> Can search alert and review evidence                                              




"""