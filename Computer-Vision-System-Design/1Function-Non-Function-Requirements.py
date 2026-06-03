""" 

=> Functional Requirement

   -> What should the system do 

        These are functional requirements 

   -> Functional Requirements describe the feature and capabilities of the system

   -> What action must the system peform 

   -> Example For Automatic Number Plate Recognition

       1. Detect vehicles 
       2. Detect number plates 
       3. Read plate text using OCR
       4. Store result in Database
       5. Show result in dashboard 
       6. Search vehicle  by plate number 
       7. Generate entry / exit log 

    These define what the system do 

   -> Shoplifting Detection 

       Functional Requirements 

       1. Detect people 
       2. Detect products 
       3. Track customer 
       4. Detect suspicious behaviour 
       5. Generate alerts 
       6. Save evidence video 
       7. Notify Security personnel

----------------------------------------------------------------------------------

=> Non-Functional Requirements

   -> Define system quality 


   -> How fast  , how accurate  , how reliable 


   1. Latency 

      -> Time taken to generate output 

          Frame -> Result generated (100 millisecond)

          Requirement (latency < 100ms)

   2. Throughput

      -> How much work system can process 

        100 camers 

        30 FPS


        Total -> 3000 frame / sec

        System should handle this load 

   3. Accuracy 

      -> Plate detection accuracy > 95% 

      -> OCR accuracy > 98%

   4. Scalability 

      -> Can system grow

         Today 10 cameras 

         Future -> 1000 cameras

   5. Availability 

       -> How much uptime 

          99.9 % uptime 


        -> Means system should almost always be availabe 

   6. Reliability 

      -> Can it continue working without failure 

      -> Example 

          Camera disconnect 
          Network issue 
          GPU restart 


          System should recover automatically 

   7. Cost 

      -> Client budget  =  2 lakh

      -> We cannot design a 20 lakh solution

   8. Security 

      -> Encrypt video stream 

      -> User authenication 

      -> Role - based access 


      
---------------------------------------------------------------------------

=> Example Interview Question

       1. Design a Traffic Monitoring System

            => Functional Requirements
                   -> Detect vehicles
                   -> Count vehicles
                   -> Detect violations
                   -> Track vehicle movement
                   -> Generate reports

                   
            => Non-Functional Requirements
                    
                    -> 30 FPS processing
                    -> Latency < 200 ms
                    -> Accuracy > 95%
                    -> Support 500 cameras
                    -> 99.9% uptime
                    -> Secure data storage
                                                                      


"""