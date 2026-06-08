""" 

=> Rotate In FFmpeg 
   
  -> Rotate the video frame 


  1. Rotate 90 degree clockwise

     
     ffmpeg -i input.mp4 -vf "transpose=1" output.mp4

  2. Rotate 90 degree counter clockwise

      ffmpeg -i input.mp4 -vf "transpose=2" output.mp4

  3. Rotate 180 degree

      ffmpeg -i input.mp4 -vf "transpose=2 , transpose=2" output.mp4              

"""