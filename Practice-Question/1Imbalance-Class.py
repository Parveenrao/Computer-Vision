""" 
=> How to Handle Class Imbalance In a Vision Dataset 

     -> In computer vision class imbalance happens when some classes appear far more often  
        than others (95% cat  , 5% dog images). This cause model to  bias towards the 
        majority class 

     -> Data level methods are techniques that try to fix this problem before training 
        the model , by changing the dataset itself rather then modifying 
        the algorithm


     -> Data Level methods 

         They are the strategies that rebalances the training data distribution so the 
         model sees a more uniform representation of classes


         Fix the dataset , instead of fix the model

-------------------------------------------------------------------------------------------

1. OverSampling 
  
    -> Data level technique where you increase the number of samples of minority classes 
       so that all classes become more balanced 

       We give the rare classes more presence in the dataset 

    -> Why do we need it 

       In class imbalance , model sees the majority class more often and learns to bias towards it 

       cat -> 10,000 images 
       dog -> 500 images 

       Without correction 

       Model become very good at "cat"
       Poor at detecting "dog"


       Over sampling fix this by incresing dog samples


    -> Types Of Oversampling In Vision   

       1. Random Oversampling

          -> Simply duplicate existing minority images      

          -> Example , let say we have 500 dog images , we copy them until reach 10000

          -> Overfitting (Model memorize repeated images , No new information is added)

       2. Oversampling With Data Augmentation 

          -> Instead of copying identical images , we create new variations 

          -> Example Transformation

            1. Horizontal flip 
            2. Rotations 
            3. Random crop 
            4. Color jitter(brightness / contrast)    
            5. Scaling / zooming

         -> Different looking version of same class

         -> So model learn robust feature instead of memorization

         -> Example Dog 

            flipped Dog 
            rotated Dog 
            darker  Dog 
            zoomed  Dog

       3. Synthetic Oversampling 

          -> Instead of modifying existing images , we generate new ones 

          -> GANs , Diffusion models

       4. Oversampling via Sampling Strategy (Batch - Level)

          -> Instead of changing dataset size , we change how batches are formed 

          -> we use Weighted Random Sampler 

              minority class get higher probability of being picked 

              So each batch has balanced classes 

   -> Effect Of oversampling 

       1. Model sees minority class more often 
       2. Decision boundary become less biased 

   -> Problem with oversampling 

      1. Overfitting 

         -> Duplication 
         -> Model memorizing instead of learning 

      2. Training inefficiency 

        -> Dataset become larger -> slower traning 

     3. No  new information 



=> Key takeways 

      Oversampling + Data Augmentation 
"""