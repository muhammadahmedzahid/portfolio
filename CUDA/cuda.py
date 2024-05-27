import torch

if torch.cuda.is_available():
    print("CUDA is available. GPU is accessible.")
else:
    print("CUDA is not available. GPU cannot be accessed.")
