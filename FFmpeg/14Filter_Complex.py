"""  
=> Filter_Complex 
    
   -> Filter_Complex lets you 

   1. Combine mulitple inputs
   2. Apply multiple filter in a graph
   3. Split , merge , overlay , scale , crop , mix audio/video


   -> Normal simple filter 
      
      ffmpeg -i input.mp4 -vf "scale = 1280:720" output.mp4

   -> but if we need multiple inputs 

      ffmpeg -i a.mp4 -i b.mp4 -filter_complex "..." output.mp4

--------------------------------------------------------------------------

=> Simple overlay (Pip Video)
   
    Put video on top of video A

      ffmpeg -i main.mp4 -i overlay.mp4 -filter_complex "[0:v][1:v] overlay = 10:10 output.mp4



"""