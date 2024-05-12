import numpy as np
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def tensor_to_numpy(tensor):
    return tensor.cpu().numpy()


def to_tensor(var):
    if (isinstance(var, bool)):
        return torch.tensor([var]).to(device)
    
    if (isinstance(var, int)):
        return torch.tensor([var]).to(device).float()

    if (isinstance(var, float)):
        return torch.tensor([var]).to(device).float()
    
    if (var.ndim == 1):
        return torch.tensor([var]).to(device).float()
    else:
        return torch.tensor(var).to(device).float()