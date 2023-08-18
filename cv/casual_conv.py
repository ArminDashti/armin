import torch
import torch.nn as nn

class Casual_Conv1D(nn.Module):
    def __init__(self, receptive_field, kernel_size=2):
        super().__init__()
        self.rf = receptive_field
        self.kernel_size = kernel_size
        self.casual_conv = self.generate_casual_conv()
        
    def generate_casual_conv(self):
        casual_conv = nn.Sequential()
        for i in range(self.rf-1):
            casual_conv.append(nn.Conv1d(1, 1, self.kernel_size))
        return casual_conv
        
    def forward(self, x):
        return self.casual_conv(x)
