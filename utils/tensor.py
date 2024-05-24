import numpy as np
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def tensor_to_numpy(tensor):
    return tensor.cpu().numpy()