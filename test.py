from PlywoodDataset import PlywoodDataset
from AlexNet import AlexNet
from PIL import Image
import torchvision.transforms as transforms
import torch
import numpy as np
import warnings

warnings.filterwarnings('ignore')

transform = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Resize((227, 227)),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)
image = Image.open("test_image.jpg")
image = transform(image)
image = torch.unsqueeze(image, dim=0)

net = AlexNet()
net.load_state_dict(torch.load(f"alexnet/alexnet_epoch{30}.pt"))

output = net(image)
print(output.flatten().tolist()[0])


