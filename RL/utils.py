import torch
import torch.nn as nn


# https://github.com/davidbrandfonbrener/onestep-rl/blob/main/utils.py
def soft_update_params(net, target_net, tau):
    for param, target_param in zip(net.parameters(), target_net.parameters()):
        target_param.data.copy_(tau * param.data + (1 - tau) * target_param.data)