import numpy as np
import torch
# from armin_utils.pytorch.device import detect_device


# default_device = detect_device()


def to_numpy(tensor):
    return tensor.cpu().numpy()


def numpy_to_tensor(tensor, device=None):
    pass


def zeros(shape, grad=False, device=None):
    if type(shape) is int:
        return torch.zeros(shape, requires_grad=grad)
    zero_tensor = torch.zeros(*shape, requires_grad=grad)
    return zero_tensor


def ones(shape, grad=False, device=None):
    zero_tensor = torch.ones(*shape, requires_grad=grad)
    return zero_tensor


def rand(shape, dtype='float', grad=False, device=None):
    if dtype == 'int':
        rand_int = torch.randint(0, 10, shape, requires_grad=grad)
        return rand_int
    else:
        rand_float = torch.rand(*shape, requires_grad=grad)
        return rand_float


def fanin_init(tensor):
    size = tensor.size()
    if len(size) == 2:
        fan_in = size[0]
    elif len(size) > 2:
        fan_in = np.prod(size[1:])
    else:
        raise Exception("Shape must be have dimension at least 2.")
    bound = 1. / np.sqrt(fan_in)
    return tensor.data.uniform_(-bound, bound)