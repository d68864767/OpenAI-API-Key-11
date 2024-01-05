```python
# Importing necessary libraries
import unittest
import torch
from tensorflow.python.framework import ops
from src.debugging import Debugging

class TestDebugging(unittest.TestCase):
    def setUp(self):
        """
        Function to set up necessary variables for tests
        """
        self.model = torch.nn.Linear(10, 1)
        self.debugging = Debugging(self.model)
        self.data = torch.randn(1, 10)
        self.target = torch.randn(1, 1)
        self.param = "param"
        self.metric = 0.5
        self.artifact = "artifact"

    def test_tensorboard_debug(self):
        """
        Function to test tensorboard_debug function
        """
        self.debugging.tensorboard_debug(self.data, self.target)

    def test_pytorch_profile(self):
        """
        Function to test pytorch_profile function
        """
        self.debugging.pytorch_profile(self.data)

    def test_tensorflow_debug(self):
        """
        Function to test tensorflow_debug function
        """
        ops.reset_default_graph()
        self.debugging.tensorflow_debug(self.data)

    def test_mlflow_track(self):
        """
        Function to test mlflow_track function
        """
        self.debugging.mlflow_track(self.param, self.metric, self.artifact)

if __name__ == '__main__':
    unittest.main()
```
