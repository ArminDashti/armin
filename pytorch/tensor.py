import numpy as np
import torch
from armin_utils.pytorch.device import detect_device


default_device = detect_device()


def to_numpy(tensor):
    return tensor.cpu().numpy()


def numpy_to_tensor(tensor, device=None):
    pass


def zeros(shape, device=None):
    pass


def ones(shape, device=None):
    pass


def rand(shape, dtype='float', device=None):
    pass

