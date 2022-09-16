import torch
import torch.nn as nn
import numpy as np
from torchvision import transforms as T
from PIL import Image
import sqlalchemy as db


def what_device():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

def pgsql_connection(ip, port, db_name, username, password):
    engine = db.create_engine(f"postgresql://{username}:{password}@{ip}:{port}/{db_name}")
    return engine.connect()

def clc_prc(a, b, c):
    return round(((a/b) * 100) - 100 , c)

def find_nan_df(df):
    return df[df.isna().any(axis=1)]

def tensor_to_image(tensor_image):
    image_array = (tensor_image.detach().numpy()*255).astype('int')
    return (np.transpose(image_array, (1, 2, 0))).astype('uint8')

def image_to_tensor(img_path):
    img = Image.open(img_path).convert("RGB")
    image_tensor_transform = T.ToTensor()
    return image_tensor_transform(img)

def show_tensor_image(tensor_image):
    pass

def show_array_image(array_image):
    pass

def show_image_from_path(path):
    pass

