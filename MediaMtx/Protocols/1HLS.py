"""" 

=> HLS 

   -> HTTP Live streaming 

   -> Created by apple

   -> It is a way to stream video over a normal HTTP , just like downloading web pages


=> Why was HLS Created 

   -> Imagine a camera produces 

     Frame 1 
     Frame 2 
     Frame 3

     Sending frames continuously to every browser is difficult 

   -> Instead HLS 

      Video Stream  ---> Split into small files -> chunk.ts , chunk.ts , chunk.ts

------------------------------------------------------------------------------------------

=> Working Of HLS 

   Suppose a camera stream video

   Camera -> MediaMtx 


   MediaMtx creates 

   playlist.m3u8


   segment1.ts 
   segment2.ts
   segment3.ts


   Step 1 

     -> HLS create a playlist file 

          playlist.m3u8

          Example 

          segment1.ts 
          segment2.ts
          segment3.ts

   Step 2. Video segement

     -> The stream is cut into pieces

           10:00:00 - 10:00:02 → segment1.ts
           10:00:02 - 10:00:04 → segment2.ts
           10:00:04 - 10:00:06 → segment3.ts        


     Each segment contains  a few second of video

    Step 3 Browser Downloads 

      Download full playlist -> Download segment1.ts -> play -> Download segment2.ts -> play 

      Just like downloading normal file from website 


=> HLS Delay 

    -> Delay come from from that, HLS does not send frame immediatley

    -> Instead it waits and groups frame into chunks (segment)

    -> Suppose HLS segment size is 2 second 

        MediaMtx cannot send yet 

        It waits unitl it has full 2 second segment 

        Only then browser can download it 


"""