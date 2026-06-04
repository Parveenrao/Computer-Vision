""" 

=> Synchronous Data Flow

   -> Step B cannot start until Step A finish

   -> Think of standing in a queue at a bank. The next customer  wait until the current customer 
      is done


   -> Example 

       Person Detecting API 


       Image -> Processig -> Yolo detection -> Return Result 

--------------------------------------------------------------------------------------------------------
Step 1 Receive Image
      
         -> System get the image 

Step 2 Preprocessing

        -> Resizing , yolo need specific output

Step 3 Yolo Inference 

      Image -> Bounding box 


      Next step cannot start until yolo completes

Step 4 Post Processing

       -> Apply thresholding
       -> NMS 

    Wait until processing finsish

Step 5. Return Response 

     -> Only after previous step finish

-------------------------------------------------------------------------------------

=> Why it is called Blocking

   -> Because each step is blocking the next step 


   -> Post processing cannot do anything until YOLO finish

--------------------------------------------------------------------------------------

=> When It become problem 

   Imagine 100 camera 

   30 FPS each


   Thats 3000 frame / per second


   IF every frame wait for the previous processing chain to finish, system become bottleneck


"""