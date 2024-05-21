import torch

# Check if GPU is available
print("CUDA Available: ", torch.cuda.is_available())

# Test a simple tensor operation
x = torch.rand(5, 3)
print(x)