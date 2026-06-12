""" 
=> First FFmpeg Command 
     
     
    ffmpeg -i input.mp4 output mp4

    1. ffmpeg -> start ffmpeg program 
    2. -i -> input files , ffmpeg know what to read 
    3. input.mp4 -> This is the file you want to process(movie , clip , recording , song)

    4. output.mp4 -> This is the new file ffmpeg creates


    -> Visual Understanding 

                input.mp4
                   ↓
                 FFmpeg
                   ↓
                output.mp4 


---------------------------------------------------------------------------------

=> MP4 To MP3
    
    ffmpeg -i video.mp4 song.mp3

    video.mp4 -> extract audio -> song.mp3

"""