""" 

=> City Traffic Monitoring 

    -> Requirement 

         1000 cameras 

         30 FPS

         Alert within  100ms

    -> Load becomes 

        1000 * 30 ==> 30000 frame / second

        -> A single server cannnot handle this        


              Multiple GPUs
              Load balancing
              Distributed processing
              Message queues
              Scalable storage



----------------------------------------------------------------------------

=> Latency 

   Time taken to produce output after receiving input 

   latency = Ouput time - input time

      Frame arrives: 10:00:00.000  
      Result ready : 10:00:00.080

   Latency = 80ms

=> Throughput 

   
   -> Amount of work processed per second

      100 frames every second 

      Througput => 100FPS


   -> High Throughput means handling more cameras 


=> FPS (Frame Per Second)

    -> Tell us how many image arrive each second 

    -> 30 FPS = 30 image every second


    Time between frames  = 1/ 30 => 0.033 sec

"""