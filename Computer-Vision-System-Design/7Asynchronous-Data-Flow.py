""" 

=> Asynchronous FLow 

   -> A step does not wait for the next step to finish.


   -> Instead of directly calling the next component , it puts work into a queue and continues

-----------------------------------------------------------------------------------------------


=> Crowd Counting System 


     -> Suppose 100 camera are sending frames 


     Step 1. Camera send frame 


     Step 2. Instead of sendig frame directly to yolo , send it to Kafka
      
             Camera job is done , Does not wait for yolo 

     Step 3. Yolo Consumer 

          -> A yolo service continuously reads frames 


          -> kafka = yolo service 

     Step 4. Push Result Into another Queue

          Detection Result -> Result queue 

          Yolo does not wait for database storage 

          Yolo immedaitely start processing next frame 

     Step 5. Storage Service 


          Another service read result 

          Result -> Queue

          Database 


          Storage work independently                                 
   


"""