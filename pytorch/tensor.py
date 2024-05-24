import numpy as np
import torch
from armin_utils.pytorch.device import detect_device


default_device = detect_device()


def to_numpy(tensor):
    return tensor.cpu().numpy()


def numpy_to_tensor(tensor, device=None):
    pass


def zeros(shape, device=None):
    zero_tensor = torch.zeros(*shape)
    return zero_tensor


def ones(shape, device=None):
    zero_tensor = torch.ones(*shape)
    return zero_tensor


def rand(shape, dtype='float', device=None):
    if dtype == 'int':
        random_int_tensor = torch.randint(0, 10, shape)
        return random_int_tensor
    else:
        random_float_tensor = torch.rand(*shape)
        return random_int_tensor
    
    

