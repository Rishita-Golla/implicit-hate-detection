from collections import Counter

import pandas as pd
import torch
from torch.utils.data import DataLoader

import config
from dataloader import Stage1Dataset, Stage2Dataset


def load_into_dataframe(dataset):
    return pd.read_csv(dataset, delimiter='\t')


# Confirm that the GPU is detected

assert torch.cuda.is_available()

# Get the GPU device name.
device_name = torch.cuda.get_device_name()
n_gpu = torch.cuda.device_count()
print(f"Found device: {device_name}, n_gpu: {n_gpu}")
device = torch.device("cuda")

# Stage 1 Annotations: see config.py for dataset specs
training_data = Stage1Dataset(config.dataset_filename["stage-1"])
train_dataloader = DataLoader(training_data, batch_size=len(training_data), shuffle=False)

# Print post and label.
posts, classes, input_ids, attention_masks, labels = next(iter(train_dataloader))
print('Original: ', posts[0], classes[0])
print('Token IDs:', input_ids[0])
print('Attention Mask IDs:', attention_masks[0])
print('Label:', labels[0])
print(Counter(classes))

dataset_df = load_into_dataframe(config.dataset_filename["stage-1"])
assert len(training_data) == len(dataset_df)

# Stage 1 Annotations: see config.py for dataset specs
training_data = Stage1Dataset(config.dataset_filename["stage-1"], drop_explicit_hate=True)
train_dataloader = DataLoader(training_data, batch_size=len(training_data), shuffle=False)

# Print post and label.
posts, classes, input_ids, attention_masks, labels = next(iter(train_dataloader))
print('Original: ', posts[0], classes[0])
print('Token IDs:', input_ids[0])
print('Attention Mask IDs:', attention_masks[0])
print('Label:', labels[0])
print(Counter(classes))

dataset_df = load_into_dataframe(config.dataset_filename["stage-1"])
dataset_df = dataset_df.loc[dataset_df['class'] != 'explicit_hate']
assert len(training_data) == len(dataset_df)

# Stage 2 Annotations: see config.py for dataset specs
training_data = Stage2Dataset(config.dataset_filename["stage-2"])
train_dataloader = DataLoader(training_data, batch_size=64, shuffle=False)

# Print post and label.
posts, im_classes, ext_im_classes, input_ids, attention_masks, im_labels, ext_im_labels = next(iter(train_dataloader))
print('Original: ', posts[0], im_classes[0], ext_im_classes[0])
print('Token IDs:', input_ids[0])
print('Attention Mask IDs:', attention_masks[0])
print('Label:', im_labels[0], ext_im_labels[0])

dataset_df = load_into_dataframe(config.dataset_filename["stage-2"])
assert len(training_data) == len(dataset_df)
