""" 
=> MediaMtx 

    -> MediaMtx is a video traffic controller 

    -> Camera stream come in -> MediaMtx recieve them -> Ai service consume them -> user watch them 
       vai browser/mobile


    -> Without MediaMtx

       Camera 1 -> AI services
       Camera 2 -> AI services
       Camera 3 -> AI services 

       Every service connect directly to camera 
       Camera overload 
       Hard to scale 
       Hard to record stream


    -> With MediaMtx

       Camera 1   
       Camera 2   ---> MediaMtx  -> AI service
       Camera 3      

    -> Deep Dive architecture 

       Imagine u have 10 cameras

       Each camera outputs -> rtsp://192.168.1.10/live

       MediaMtx pulls the stream , Camera -> MediaMtx

       Now MediaMtx store it in the memory      


"""