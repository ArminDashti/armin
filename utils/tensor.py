import numpy as np
import torch


def tensor_to_numpy(tensor):
    return tensor.cpu().numpy()

