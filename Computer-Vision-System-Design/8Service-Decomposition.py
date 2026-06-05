""" 
=> Service Decomposition

    -> Breaking a large application into smaller service , where each service has one 

       Responsibility


    -> Instead of one gaint doing everything

        Camera -> One Huge Application -> Database 


    -> We split into smaller service 

-----------------------------------------------------------------------------------------

=> Shirt Color Detection System 

    1. Bad Design (Monolithic)

       Upload -> Resize -> Detect person -> Segment shirt -> Detect color -> Save result 


       ALl logic in one codebase 

       -> Hard to maintain , Hard to scale , One bug crash everything 


   2. Better Design (Decomposed Service)

       -> Image upload service 

       -> Processig service 

       -> Segmentation service 

       -> Color Detection  Service 

       -> Storage service 


    Service 1. Image Upload Service

        -> Responsibility

           1. Recieve image 
           2. validae image 
           3. Store image 

        -> Should not run yolo , detect colors , access model logic 

    Service 2. Preprocessing Service 

        -> Responsibility 

           1. Resize 
           2. Normalize 
           3. Convert color space 

    Service 3. Segmentation Service

        -> Responsibility 

        1. Input image 
        2. YOlo seg / Mask R-CNN 

        -> This servie know nothing about colors

    Service 4. Color Detection Service    


       -> Responsibility 

         Shirt Region -> HSV conversion -> Dominant Color 

    Service 5. Storage Service 


        -> Responsibility

         Save Result 

         Save metadata                                                  



"""