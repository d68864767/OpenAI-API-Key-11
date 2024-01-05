```python
# Importing necessary libraries
import shap
import lime
import captum
import interpret

class Explainability:
    def __init__(self, model):
        self.model = model

    def shap_explain(self, data):
        """
        Function to explain predictions using SHAP
        """
        explainer = shap.Explainer(self.model)
        shap_values = explainer(data)
        return shap_values

    def lime_explain(self, data):
        """
        Function to explain predictions using LIME
        """
        explainer = lime.LimeTabularExplainer(data)
        lime_values = explainer.explain_instance(data, self.model.predict)
        return lime_values

    def captum_explain(self, data):
        """
        Function to explain predictions using Captum
        """
        explainer = captum.attr.LayerConductance(self.model, self.model.layer1)
        captum_values = explainer.attribute(data)
        return captum_values

    def interpret_explain(self, data):
        """
        Function to explain predictions using InterpretML
        """
        explainer = interpret.blackbox.LocalExplainer(self.model.predict, data)
        interpret_values = explainer.explain_local(data)
        return interpret_values
```
