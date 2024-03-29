"""
Contain parameters to easily tuning
"""
import torch
PATH_TRAIN = "Data/train.npz"
PATH_TEST = "Data/validate.npz"
LEARNING_RATE= 0.0001
EPOCHS=100
BATCH_SIZE=64
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
