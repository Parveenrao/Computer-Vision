""" 
=> Model Serving 

    -> Process of taking a trained machine learning and making it available for 

        real-world use - typically thorugh an api , application or service 

        so that it can generate predicitions or response on demand


    -> Meaning 

        -> After training a model in memory , it just a file with weight 


        1. Load that model into memory 
        2. Accept request (text , image , data)
        3. Run inference  (Make , predicition)
        4. Return result quickly and reliably 

---------------------------------------------------------------------------------------

=> Key component Of model serving

   1. Inference Engine

      The runtime that executes the model 

      Tensorflow serving 
      Torch serve 
      ONNX Runtime

   2. API Layer 

     -> Model are usually exposed via 

        REST API
        grpc services 

   3. Infrastructure 

      -> WHere and how the model runs 

         1. Cloud(AWS , GCP , Azure)

         2. Container (Docker)

         3. Orchestration (Kubernetes)

   4. Scaling and Performance 

       -> To handle real users 

       1. Load balancing 
       2. Auto-scaling 
       3. GPU/CPU optimization 
       4. Batching Request 

   5. Monitoring & Logging

      -> Track 

        1. Latency 
        2. Error rates 
        3. Model drift 
        4. Usage patterns 

------------------------------------------------------------------------------------------

=> Types Of Model Serving 

   1. Real-time (online serving)

      -> Immediate response(millisecond)
      -> Used in chatbots , recommendations system

   2. batch Serving 

       -> Process large data periodically 
       -> Used for reports , offline predictions 

   3. Streaming 

      -> Continuous data flow 

      
----------------------------------------------------------------------------------

=>     Example workflow
            Train model in Python (PyTorch/TensorFlow)
            Export model file
            Deploy via serving framework
            Wrap with API
            Scale with Kubernetes
            Monitor performance 


"""