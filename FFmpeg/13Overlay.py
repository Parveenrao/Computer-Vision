""" 

=> Overlay 
   
   -> Placing one layer on top of another layer without fully replacing it


   -> Visual / Ui Overlay
      
       in user interface , an overlay is a UI element that appears on top of the main screen content

   -> Example 

      A pop dialogue , Are you sure you want to delete

   -> Core Idea 

      1. Background is still visible

      2. OVerlay is temporary

   -> Common uses 

       1. Alerts 
       2. Forms 
       3. Confirmations 
       4. Tool tips

   -> Overlay in FFmpeg 

       We combine two input 

       1. Main video background 
       2. Overlay video / image

   -> Basic Syntax 

       ffmpeg -i background.mp4 -i overlay.png -filter_complex "overlay" output.mp4


       background.mp4 -> base layer 

       overlay.png -> image/video placed on top 

       overlay -> filter combine them

   -> Position Of overlay 

       By default overlay goes at top-left (0,0)     

       1. Top left 

          overlay 0.0 

       2. Top right 

          overlay = W-w:0

       3. Bottom left 

         overlay = 0:H-h

       4. Bottom right 

           overlay = W-w:H-h                       

"""