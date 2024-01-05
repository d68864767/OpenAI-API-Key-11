```python
# Importing necessary libraries
import unittest
import torch
import torch.nn as nn
from src.performance import Performance

class TestPerformance(unittest.TestCase):
    def setUp(self):
        """
        Set up a simple model for testing
        """
        self.model = nn.Sequential(
            nn.Conv2d(1, 20, 5),
            nn.ReLU(),
            nn.Conv2d(20, 64, 5),
            nn.ReLU()
        )
        self.performance = Performance(self.model)

    def test_gpu_acceleration(self):
        """
        Test if GPU acceleration is enabled when available
        """
        self.performance.gpu_acceleration()
        if torch.cuda.is_available():
            self.assertEqual(str(self.model.device), 'cuda')
        else:
            self.assertEqual(str(self.model.device), 'cpu')

    def test_distributed_training(self):
        """
        Test if distributed training is enabled when multiple GPUs are available
        """
        data = torch.randn(1, 1, 32, 32)
        target = torch.randn(1, 64, 28, 28)
        self.performance.distributed_training(data, target)
        if torch.cuda.device_count() > 1:
            self.assertIsInstance(self.model, nn.DataParallel)

    def test_model_quantization(self):
        """
        Test if model quantization is performed correctly
        """
        quantized_model = self.performance.model_quantization()
        for module in quantized_model.modules():
            if isinstance(module, nn.Linear):
                self.assertTrue(hasattr(module, 'qconfig'))

    def test_model_pruning(self):
        """
        Test if model pruning is performed correctly
        """
        self.performance.model_pruning()
        for name, module in self.model.named_modules():
            if isinstance(module, nn.Conv2d) or isinstance(module, nn.Linear):
                self.assertTrue(hasattr(module.weight, 'mask'))

if __name__ == '__main__':
    unittest.main()
```
