""" 
=> UnderSampling In Vision 

    -> Reduce the number of samples from the majority class so that dataset become 
       balanced 

    -> remove majority samples , keep a smaller , balanced dataset

    -> When to use UnderSampling 

       1. Dataset is huge 
       2. Majority class has redundant samples 
       3. Training speed matters 

    -> Problem with UnderSampling 

        -> Loose information from majority class 

        -> hurt performance if 

            1. Dataset is small 
            2. majority class has important diversity 

---------------------------------------------------------------------------------

=> Random Undersampling 

   -> Randomly removes majority samples 

=> Stratified / balanced undersampling 
  
   -> equal sample per class

=> Smart undersampling 

   -> Remove redundant / similar samples 


"""