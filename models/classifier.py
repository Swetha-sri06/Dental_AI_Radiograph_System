# Tooth condition classifier
import torchvision.models as models
import torch.nn as nn

def get_classifier():

    model = models.efficientnet_b0(pretrained=True)

    model.classifier[1] = nn.Linear(1280,4)

    return model
