""" 

=> Stream Control 
   
   -> A media file is made of stream 

   1. Video stream 
   2. Audio stream
   3. Subtitle stream 
   4. Metadata / chapters

   -> Stream Control deciding 

      1. which stream to keep 
      2. which to remove 
      3. which to map 
      4. how to encode them 
      5. how to stream live

   -> View stream in a file 

      ffprobe input.mp4

      or cleaner version 

      ffprobe -hide_banner input.mp4

   -> Select stream with map 

      1.Keep only video (Remove audio)


         ffmpeg -i input.mp4 -map 0:v -c copy video_only.mp4

      2. Keep only audio 

          ffmpeg -i input.mp4 -map 0:a -c copy audio_only.aac

     3. Keep audio + video explicilty 

         ffmpeg -i input.mp4 -map 0:v -map 0:a -c copy output.mp4

   -> Remove audio 

       ffmpeg -i input.mp4 -an output.mp4

   -> Remove video 

     ffmpeg -i input.mp4 -vn output.mp3                                              

"""