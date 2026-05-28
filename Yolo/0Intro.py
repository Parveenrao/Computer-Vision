""" 
=> Yolo 

    -> Yolo is an object detection model that 
       
       1. Take an image 
       2. Detect object 
       3. Outputs 
        
           -> Bounding boxes 
           -> Class labels 
           -> COnfidence score

    -> Instead of scanning an image multiple times , YOLO does it one forward pass


    -> Core Idea 
        YOLO divide image into grid and for each grid cell predicts 

        -> Object presenece 
        -> Bounding box (x , y w, h)

        -> class probability               


"""