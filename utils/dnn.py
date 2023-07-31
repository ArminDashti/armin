import torch
import torch.nn as nn
import numpy as np
from torchvision import transforms as T
from PIL import Image
import sqlalchemy as db


def pgsql_connection(ip, port, db_name, username, password):
    engine = db.create_engine(f"postgresql://{username}:{password}@{ip}:{port}/{db_name}")
    return engine.connect()

def sqlserver_connection(ip, port, db_name, username, password):
    pass

def clc_prc(a, b, c):
    return round(((a/b) * 100) - 100 , c)

def df_find_nan(df):
    return df[df.isna().any(axis=1)]

def df_drop_nan(df):
    pass

def df_drop_value(df):
    pass

def tensor_to_array(tensor_image):
    image_array = (tensor_image.detach().numpy()*255).astype('int')
    return (np.transpose(image_array, (1, 2, 0))).astype('uint8')

def array_to_tensor():
    pass

def tensor_to_image(tensor_image):
    pass

def numpy_to_image(array_image):
    pass

def path_to_image(path):
    pass

# https://stackoverflow.com/questions/49201236/check-the-total-number-of-parameters-in-a-pytorch-model
def parameters_number(model):
    parameters_num = sum(p.numel() for p in model.parameters())
    return "{:,}".format(parameters_num)

def get_paramters(model):
    pass

def get_gradient(model):
    pass
