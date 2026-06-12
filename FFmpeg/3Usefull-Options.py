"""" 

=> More Usefull options 

   1. -c:v (Video codec)
       
       -c:v lib*264

       meaning = use 264 encoder 


       lib*264 = H.264
       lib*265 = H.265

       copy no encoding


       ffmpeg -i input.mp4 -c:v libx264 output.mp4


   2. -c:a Audio Codec

      -c:a acc

      -> Audio encoder

         acc
         mp3
         opus


         ffmpeg -i input.mov -c:a aac output.mp4        

   3. -b:v (Video bitrate)      

        -b:v = 2M  (Set video bitrate)    


        ffmpeg -i input.mp4 -b:v 4M output.mp4

   4. Set Audio Bitrate 

         ffmpeg -i input.mp4 -b:a 128k audio.mp3

   5. -y (Overwrite) 

        -> overwrite without asking


        ffmpeg -y -i input/mp4 output.mp4

   6. -hide_banner (Cleaner output)

       ffmpeg -hide_banner -i input.mp4 output.mp4    (used to hide ffmpeg build , version)

   7. -hwaccel

        ffmpeg -hwaccel cuda -i input.mp4 output.mp4        

                                              

"""