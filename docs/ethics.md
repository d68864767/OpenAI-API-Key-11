# Ethics

This document provides an overview of the `Ethics` class in the `src/ethics.py` file. The `Ethics` class is designed to handle various tasks related to AI ethics, including bias mitigation, fairness checking, and relabelling.

## Class Definition

The `Ethics` class is defined with the following methods:

- `__init__(self, model)`: Initializes the `Ethics` class with a given model.

- `reweighing(self, dataset)`: Mitigates bias in the dataset using Reweighing.

- `mean_difference(self, y_true, y_pred)`: Calculates the mean difference to check fairness.

- `relabelling(self, y_true, y_pred)`: Relabels the predictions to mitigate bias.

- `check_algorithmic_fairness(self, y_true, y_pred, protected_class)`: Checks algorithmic fairness of the model.

## Class Usage

The `Ethics` class can be used as follows:

```python
from src.ethics import Ethics
from aif360.datasets import BinaryLabelDataset

# Initialize the Ethics class
ethics = Ethics(model)

# Mitigate bias in the dataset
dataset_transf = ethics.reweighing(dataset)

# Calculate the mean difference
mean_diff = ethics.mean_difference(y_true, y_pred)

# Relabel the predictions
y_pred_relab = ethics.relabelling(y_true, y_pred)

# Check algorithmic fairness
fairness = ethics.check_algorithmic_fairness(y_true, y_pred, protected_class)
```

## Testing

The `Ethics` class is tested in the `tests/test_ethics.py` file. The tests include:

- `test_reweighing(self)`: Tests the `reweighing` method.

- `test_mean_difference(self)`: Tests the `mean_difference` method.

- `test_relabelling(self)`: Tests the `relabelling` method.

- `test_check_algorithmic_fairness(self)`: Tests the `check_algorithmic_fairness` method.

To run the tests, use the following command:

```bash
python -m unittest tests.test_ethics
```
