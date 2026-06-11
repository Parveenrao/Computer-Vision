""" 
=> Autograd In Pytorch 

    -> automatic differentitation system

    -> Automatically computes derviated(gradients)

    -> tell each parameter how to change to reduce error



"""


# Example 

import torch

x = torch.tensor(3.0 , requires_grad=True)

y = x ** 2 + 2 *x + 1 

y.backward()

print(x.grad)

# chain rule 

x = torch.tensor(2.0 , requires_grad=True)

a = x * 3

b = a ** 2 

b.backward()

print(x.grad)


# Important zero_grad -> clean old grad before computing new