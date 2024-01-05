# AI Model Explainability and Interpretability

This document provides an overview of the explainability and interpretability features of our AI model. We use several libraries to achieve this, including SHAP, Lime, Captum, and InterpretML.

## SHAP (SHapley Additive exPlanations)

SHAP is a game theoretic approach to explain the output of any machine learning model. It connects optimal credit allocation with local explanations using the classic Shapley values from game theory and their related extensions.

In our project, we use the `shap_explain` function to explain predictions using SHAP. This function takes in data as input and returns the SHAP values.

```python
def shap_explain(self, data):
    """
    Function to explain predictions using SHAP
    """
    explainer = shap.Explainer(self.model)
    shap_values = explainer(data)
    return shap_values
```

## Lime (Local Interpretable Model-Agnostic Explanations)

LIME is a novel explanation technique that explains the predictions of any classifier in an interpretable and faithful manner by learning an interpretable model locally around the prediction.

In our project, we use the `lime_explain` function to explain predictions using LIME. This function takes in data as input and returns the LIME values.

```python
def lime_explain(self, data):
    """
    Function to explain predictions using LIME
    """
    explainer = lime.LimeTabularExplainer(data)
    lime_values = explainer.explain_instance(data, self.model.predict)
    return lime_values
```

## Captum

Captum is a model interpretability and understanding library for PyTorch. Captum means comprehension in Latin and contains general purpose implementations of integrated gradients, saliency maps, smoothgrad, vargrad and others for PyTorch models.

In our project, we use the `captum_explain` function to explain predictions using Captum. This function takes in data as input and returns the Captum values.

```python
def captum_explain(self, data):
    """
    Function to explain predictions using Captum
    """
    explainer = captum.attr.LayerConductance(self.model, self.model.layer1)
    captum_values = explainer.attribute(data)
    return captum_values
```

## InterpretML

InterpretML is an open-source package that incorporates state-of-the-art machine learning interpretability techniques under one roof. With this package, you can train interpretable glassbox models and explain blackbox systems.

In our project, we use the `interpret_explain` function to explain predictions using InterpretML. This function takes in data as input and returns the InterpretML values.

```python
def interpret_explain(self, data):
    """
    Function to explain predictions using InterpretML
    """
    explainer = interpret.blackbox.LocalExplainer(self.model.predict, data)
    interpret_values = explainer.explain_local(data)
    return interpret_values
```

## Testing

We have also implemented tests for each of these functions to ensure they are working as expected. You can find these tests in the `tests/test_explainability.py` file.

```python
class TestExplainability(unittest.TestCase):
    def setUp(self):
        """
        Set up a dummy model and data for testing
        """
        self.model = DummyModel()
        self.data = np.random.rand(10, 5)
        self.explainability = Explainability(self.model)

    def test_shap_explain(self):
        """
        Test SHAP explainability
        """
        shap_values = self.explainability.shap_explain(self.data)
        self.assertIsNotNone(shap_values)

    def test_lime_explain(self):
        """
        Test LIME explainability
        """
        lime_values = self.explainability.lime_explain(self.data)
        self.assertIsNotNone(lime_values)

    def test_captum_explain(self):
        """
        Test Captum explainability
        """
        captum_values = self.explainability.captum_explain(self.data)
        self.assertIsNotNone(captum_values)

    def test_interpret_explain(self):
        """
        Test InterpretML explainability
        """
        interpret_values = self.explainability.interpret_explain(self.data)
        self.assertIsNotNone(interpret_values)
```
