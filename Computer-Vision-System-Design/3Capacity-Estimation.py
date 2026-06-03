""" 
=> Capacity Estimation 

    -> Estimating how much data , storage , network bandhwidth and compute power will your system need 



    -> Lets understand through  public-place graffiti detection system using CCTV cameras 



    Step 1. Number of cameras 

        
      Let say 

      100 cameras 

      Each camera  = 1080p video 

      15 FPS


    Step 2 Data Generation 

      -> Assume each camera generates 2Mbps video 

        Total bandwidth = 100 * 2 => 200 Mbps 

        So system must handle 200 Mbps incoming video traffic 

    Step 3 Storage Estimation 

        Per camera per day = 2Mbps  21.6 GB/day

        For 100 camera  = 100 * 21.6 => 2160 GB/day


        2.16TB/DAY

    Step 4 Compute Estimation 

      -> One GPU can process 25 video streams 

      -> You have 100 cameras 


        Required GPU 100 / 25  => 4

------------------------------------------------------------------------------------

=> What we estimate in CV system Design 

    1. Request per second 
    2. Frame per second 
    3. Bandwidth 
    4. Storage 
    5. GPU / CPU  requirements 
    6. Database size 
    7. Number of servers 


"""