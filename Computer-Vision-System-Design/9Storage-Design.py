"""" 

=> Storage Design

   -> Is a important part of computer vision system design because videos and iamges consume
      Huge amount of storage 

   -> First question is , what data do we need to store 



------------------------------------------------------------------------------------------------

=> Example 

   Shirt Color Detecting System


   -> System produce 

       Input image 
       Shirt mask 
       Detection Result 
       Logs 

       Do we need to store all of them

----------------------------------------------------------------------------------------

=> Types Of data In Computer Vision

   1. Raw Images / Videos

       camera_1.mp4
       person.jpg 


       These are the large files usually stored in Amazon S3 MiniIO , Cloud object storage 

   2. Detection Result 

      {
         "image_id": 101,
         "shirt_color": "blue",
         "confidence": 0.94
      }       '


   3. Metadata

       {
         "camera_id": "cam01",
         "timestamp": "2026-06-04 10:00",
         "location": "Gate A"
      } 


      store in database 

   4. Logs 

       -> Model started 
       -> Detection completed 
       -> Error occured         


"""