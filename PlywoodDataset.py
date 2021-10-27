import os
import pandas as pd
from PIL import Image
import torch
from torch.utils.data import Dataset

class PlywoodDataset(Dataset):
    def __init__(self, annotation_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotation_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, index):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[index, 0])
        image = Image.open(img_path)
        label = self.img_labels.iloc[index, 1]
        label = torch.as_tensor(label, dtype=torch.float64)
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transfrom(label)

        return image, label.float()