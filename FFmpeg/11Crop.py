""" 

=> Crop In FFmpeg
  
   -> Cropping removes unwanted part of a video frame

   -> Remove black bars , focus on subject , Convert landscape


   -> Basic Syntax 
      
     ffmepg -i input.mp4 -vf "crop = w:h:x:y" output.mp4

     w = width of crop area 
     h = height of crop area
     x = left starting position 
     y = top starting position

----------------------------------------------------------------------------------

1. Crop Centre 

   ffmpeg -i input.mp4 -vf "crop= 1280:720" output.mp4


2. Vertical Centre
  
    ffmepg -i input.mp4 -vf "crop = 1080:1920" output.mp4

"""