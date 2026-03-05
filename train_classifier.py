# training script for implant condition classifier
%%writefile train_classifier.py
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from models.classifier import get_classifier
from torch.utils.data import DataLoader

# Image transforms
transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor()
])

# Dataset path
dataset_path = "data/classifier"

dataset = datasets.ImageFolder(dataset_path, transform=transform)

loader = DataLoader(dataset, batch_size=8, shuffle=True)

# Load model
model = get_classifier()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = model.to(device)

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=0.0001)

# Train for 1 epoch (hackathon trick)
epochs = 1

for epoch in range(epochs):

    total_loss = 0

    for images, labels in loader:

        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        loss = criterion(outputs, labels)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1} Loss: {total_loss}")

# Save model
torch.save(model.state_dict(), "implant_classifier.pth")

print("Classifier saved!")
