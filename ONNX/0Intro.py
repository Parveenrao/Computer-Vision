""" 
=>  ONNX (Open Neural Network Exachange)
  
     -> Is a open standard for representing machine learning and deep learning 
        models so they can be moved between differnet framework and run efficiently 
        on different platforms 

     -> Why ONXX exist 

          Imagine you train a model in Pytroch and Tensorflow 

          But we want to deploy it somewhere else (Window , Linux , Mobile , cloud  , edge device)

          ONXX provide a common format 


            PyTorch Model
                  ↓
                 ONNX
                  ↓
             ONNX Runtime
                ↓
             CPU / GPU / Mobile / Cloud  



"""