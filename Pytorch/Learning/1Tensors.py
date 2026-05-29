""" 
=> Tensors 
   
   -> Tensors are the main data structure used for everything
     
       data , images , model inputs and computations


"""

import torch


# Scalar tensor 

t1 = torch.tensor(5)

print(t1)


# vector tensor 

t2 = torch.tensor([1, 2, 3])

print(t2)

# matrix 

t3 = torch.tensor([[1, 2, 3],
                  [4, 5 ,6]])

print(t3)


# Common tensor type 

torch.float64  # for deep learning 

torch.int    # integer 

torch.bool


x = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)



# useful tensor creating function 

t5 = torch.zeros(3 ,3)   # 3*3 matrix of zeros

print(t5)


t6 = torch.ones(2 ,4)  # 2 * 4 matrix of ones 


t7 = torch.rand(2 ,2)   # random values between 0 to 1

print(t7)


t8 =  torch.arange(0, 10, 2) # [0, 2, 4, 6, 8]



# tensor shape 

x = torch.tensor([[1, 2, 3] ,
                  [4 ,5 ,6]])

print(x.shape)



# Basic Operation 

a = torch.tensor([1,2 ,3])

b= torch.tensor([4 ,5 ,6])

print(a + b)

print(a * b)

print(a / b)



# matrix multiplication 

A = torch.tensor([[1,2],
                  [3 ,4]])


B = torch.tensor([[4, 5],
                  [7 ,8]])


C = (torch.matmul(A, B))

print(C)


# Indexig In tensors


z = torch.tensor([1 , 2 ,3 ,4, 5])

print(z[0])


print(z[1:3])


# For 2D tensor 

N = torch.tensor([[1, 2],
                  [3 ,4]])

print(N[0 ,1])


# GPU support 


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

x = torch.tensor([1.0, 2.0]).to(device)


# Autograd 

x = torch.tensor(2.0, requires_grad=True)

y = x ** 2
y.backward()

print(x.grad)  # derivative = 2x = 4