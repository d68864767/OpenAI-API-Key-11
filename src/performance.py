```python
# Importing necessary libraries
from tensorflow.python.framework import ops
from tensorflow.python.ops import math_ops
from tensorflow.python.eager import context
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable

class Performance:
    def __init__(self, model):
        self.model = model

    def gpu_acceleration(self):
        """
        Function to enable GPU acceleration
        """
        if torch.cuda.is_available():
            self.model = self.model.cuda()

    def distributed_training(self, data, target):
        """
        Function to perform distributed training
        """
        if torch.cuda.device_count() > 1:
            self.model = nn.DataParallel(self.model)
        self.model = self.model.to(device)
        data, target = data.to(device), target.to(device)

    def model_quantization(self):
        """
        Function to perform model quantization
        """
        quantized_model = torch.quantization.quantize_dynamic(
            self.model, {nn.Linear}, dtype=torch.qint8
        )
        return quantized_model

    def model_pruning(self, amount=0.5):
        """
        Function to perform model pruning
        """
        parameters_to_prune = (
            (self.model.conv1, 'weight'),
            (self.model.conv2, 'weight'),
            (self.model.fc1, 'weight'),
            (self.model.fc2, 'weight'),
        )

        torch.nn.utils.prune.global_unstructured(
            parameters_to_prune,
            pruning_method=torch.nn.utils.prune.L1Unstructured,
            amount=amount,
        )
```
