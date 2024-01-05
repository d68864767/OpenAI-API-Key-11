# Fairness

This document provides an overview of the fairness module of our project. The fairness module is responsible for checking the fairness of a model's predictions, mitigating bias in a dataset, and checking the algorithmic fairness of a model's predictions.

## check_fairness function

The `check_fairness` function checks the fairness of a model's predictions using Fairlearn's MetricFrame. It takes as input the true labels, the predicted labels, and the sensitive features. It returns a dictionary containing the difference in metrics for each sensitive feature.

```python
def check_fairness(y_true, y_pred, sensitive_features):
    """
    This function checks the fairness of a model's predictions using Fairlearn's MetricFrame.
    """
    mf = MetricFrame(metrics={'accuracy': accuracy_score,
                              'precision': precision_score,
                              'recall': recall_score,
                              'false positive rate': false_positive_rate,
                              'false negative rate': false_negative_rate,
                              'selection rate': selection_rate,
                              'demographic parity difference': demographic_parity_difference,
                              'demographic parity ratio': demographic_parity_ratio,
                              'equalized odds difference': equalized_odds_difference,
                              'equalized odds ratio': equalized_odds_ratio},
                     y_true=y_true,
                     y_pred=y_pred,
                     sensitive_features=sensitive_features)
    return mf.difference()
```

## mitigate_bias function

The `mitigate_bias` function mitigates bias in a dataset using Reweighing from AI Fairness 360. It takes as input a dataset and the protected attribute names. It returns the transformed dataset.

```python
def mitigate_bias(dataset, protected_attribute_names):
    """
    This function mitigates bias in a dataset using Reweighing from AI Fairness 360.
    """
    rw = Reweighing(unprivileged_groups=[{'race': 0}],
                    privileged_groups=[{'race': 1}])
    dataset_transf = rw.fit_transform(dataset)
    return dataset_transf
```

## check_algorithmic_fairness function

The `check_algorithmic_fairness` function checks the algorithmic fairness of a model's predictions using Audit-AI. It takes as input the true labels and the predicted labels. It returns the results of the fairness check.

```python
def check_algorithmic_fairness(y_true, y_pred):
    """
    This function checks the algorithmic fairness of a model's predictions using Audit-AI.
    """
    results = check_algorithmic_fairness(y_true, y_pred)
    return results
```

## Testing

The fairness module includes a test suite, which can be found in `tests/test_fairness.py`. This test suite includes tests for the `check_fairness`, `mitigate_bias`, and `check_algorithmic_fairness` functions.

To run the tests, use the following command:

```bash
python -m unittest tests.test_fairness
```
