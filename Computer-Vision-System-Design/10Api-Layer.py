""" 

=> API Layer 

    -> An API Layer is an entry point of your computer Vision system

       Client -> API Layer -> CV services 

       anything entering the system goes through API layer 


----------------------------------------------------------------------------------

=> Example 
 
    Short Color-Detection 


    User upload an image

     Frontend  -> Post/detect -> API layer 

     API layer receives the request 

     It does not detect color itself 


--------------------------------------------------------------------------------

=> Responsibility

    1. Receive Request 

        POST/detect-shirt-color 

    2. Validate Request

       -> Is image present 
       -> Is format jpg/png

       -> Is file size valid 

    3. Authentication 

        -> Who is calling 

    4. Generat Request ID

         RQ_12345 

         This ID follows the image through entire pipline 

    5. Route Request 

       -> API decide where work goes 

       Small System

       API -> Detection system 


       Large System 

       API -> Kafka queues                             


"""