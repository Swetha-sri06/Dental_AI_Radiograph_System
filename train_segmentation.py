# training script for UNet segmentation
import torch
from models.unet_model import get_unet

model = get_unet()

optimizer = torch.optim.Adam(model.parameters(),lr=1e-4)

loss_fn = torch.nn.BCEWithLogitsLoss()

print("Segmentation model ready")
