""" 
=> Load pre-trained model resent and convert it into onxx


"""

import torch

from torchvision.models import resnet18

# load pre-trained model 


model = resnet18(weights = "DEFAULT")

""" 
=> model.eval 
 
    -> means put the model into evaluation (inference) mode

    -> It change the behaviour of certain layer so the model behaves correctly during testing 
      
       and inference 

    -> Mainly effect 

        1. DROPOUT layers 

           Turned OFF (no random dropping neuron)

        2. BatchNorm Layers 

            Stop updating running statistic and use learned mean / variance instead 

    -> why matters 

       1. During training (model.train)

           -> Dropout is active (add randomness for regularization)

           -> batch norm keep updating statistic 

       2. During Evaluation (model.eval)

          -> we want stable , determinstic predictions 
          -> No randomness , no parameter update


"""

# create dummy input 

dummy = torch.randn(1, 3, 224, 224)


# export model to onxx format 

torch.onnx.export(

    model,
    dummy ,

    "resnet18.onxx",              # save the file in onnx format 

    input_names = ["images"]   ,   # gives a name to input node 

    output_names = ["predictions"] # gives a name to output node
)



""" 
=> What happens internally during export?

     PyTorch does this:

     Feeds dummy input into model
     Records every operation:
     conv layers
     relu
     pooling
     fully connected layers
     Builds a computational graph
     Converts it into ONNX format
     Saves it to file


"""