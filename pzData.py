import os
import numpy as np
import pandas as pd
from torch.utils.data import Dataset
import cv2

class pzNpz(Dataset):
    """Custom dataset for my npz files"""
    def __init__(self, label_file, data_dir, transform=None):
        self.labels = pd.read_csv(label_file)
        self.data_dir = data_dir
        self.transform = transform
    
    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        filename = self.labels.iloc[idx]['Filename']
        npz = np.load(os.path.join(self.data_dir, (filename + ".npz")))
        data = np.asarray([npz["arr_0"], npz["arr_1"]])

        if self.transform:
            data = self.transform(data)
        
        return np.asarray(data), self.labels.iloc[idx]['0']
    
class pzImg(Dataset):
    """Custom dataset for spectrogram images"""
    def __init__(self, label_file, data_dir, transform=None):
        self.labels = pd.read_csv(label_file)
        self.data_dir = data_dir
        self.transform = transform
    
    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        filename = self.labels.iloc[idx]['Filename']
        filename = os.path.join(self.data_dir, (filename + ".png"))
        data = cv2.imread(filename) 
        if self.transform:
            data = self.transform(data)
        return np.asarray(data), self.labels.iloc[idx]['0']