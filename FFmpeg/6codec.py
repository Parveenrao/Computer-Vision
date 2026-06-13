""" 

=> Codec
    
   -> coder + decoder 

   -> It decides 
      
      1. how video / audio compressed
      2. how it is stored 
      3. how it is played

   -> Raw video === codec compression ==== smaller file    

------------------------------------------------------------------------------

=> Important Video Codecs
  
   1. H.264
      
      -> Work everywhere  (phone , PC , web , Whatsapp , Youtube)
      -> Balace quality + size + speed

        ffmpeg -i input.mp4 -c:v libx264 output.mp4

      -> When to use 

          1. Always if unsure
          2. Social media uploads
          3. General video compression 

      -> Think of like it Universal Video Codec

   2. H.264 / HEVC (Small files)


       -> lib * 265

       -> Why matters 

          1. 30-50% smaller than H.264

          -> Slower encoding

       -> When to use 

          1. Storage saving
          2. High-resolution 4K
          3. Archiving

    3. VP9 

       -> Web video / Youtube alternative

       -> Good for web streaming 

       -> Used in youtube (some content)     

    4. AV1

       -> Best compression 
       -> Future proof
       -> Used by netflix                            




"""