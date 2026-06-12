""" 

=> Usefull Options 
    
   
   1. -i -> use this input files 

   2. -an (audio none) , Remove audio
       
       ffmpeg -i input.mp4 -an silent.mp4

       video kept , audio removed

   3. -vn (Remove audio)        
      
       ffmpeg -i video.mp4 -vn audio.mp3

       extract audio only

   4. -vf (Video Filter)  Apply video filters

        ffmpeg -i input.mp4 -vf scale = 1280:720 output mp4   (Resize video)
   
   5. -af (audio filter) Apply audio filter
      
       ffmpeg -i input.mp3 -af volume =2 louder.mp3

   6. copy (Fast Copy Mode) 

       -c copy (copy streams wihtout re-encoding) 

       ffmpeg -i input.mp4 -c copy output.mkv

   7. -ss (Start time) 

        ss 00:01:30  -> start at 1 minute 30 seconds

        ffmpeg -ss 10 -i input.mp4 clip.mp4

        start from 10s

   8. -t (Duration) 

        meaning output duration = 5 sec


        ffmpeg -ss 30 -t 10   input.mp4  clip.mp4

        cut 10 second clip starting at 30s

   9. -to (END) 

       stop at this timestamp 

       ffmpeg -ss 00:01::00 -to 00:02:00 -i input.mp4 clip.mp4      

   10. -r frame rate 

        -r 60 (set FPS) 

        ffmpeg -i input.mp4 -r 60 smooth.mp4

   11. -s Resolution 

      -s 1280 * 720

      ffmpeg -i input.mp4 -s 640*360 small.mp4

   12. -crf (Quality control)
     
       control quality vs size 

       FOr H.264 and H.265


       For H.264/H.265:

       CRF	Quality
       18	very high
       23	default
       28	smaller
       35	poor


       ffmpeg -i input.mp4 -crf 28 output.mp4

   13. -preset (Encoding speed)      

       -> speed
       -> compression efficiency

       -> options 

          ultrafast
          fast
          medium
          slow
          very slow


          ffmpeg -i input.mp4 -c:v libx264 -preset slow output.mp4 

"""