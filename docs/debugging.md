# Debugging AI Models

This document provides an overview of the debugging process for AI models in our project. We use various tools and libraries to ensure the correctness and efficiency of our models.

## Libraries Used

- TensorBoard: Provides visualization and tooling needed for machine learning experimentation.
- PyTorch Profiler: A tool for profiling PyTorch code, particularly focused on identifying performance bottlenecks in models.
- TensorFlow Debugger: A tool for debugging TensorFlow programs, providing visibility into internal structure and states of running TensorFlow graphs.
- MLflow: An open source platform for managing the end-to-end machine learning lifecycle.

## Debugging Class

We have a `Debugging` class in `src/debugging.py` which uses the above libraries to debug our AI models. The class has the following methods:

- `tensorboard_debug(data, target)`: This method uses TensorBoard to visualize the model graph and histograms of predictions and target values.
- `pytorch_profile(data)`: This method uses PyTorch Profiler to profile the model inference and print the profiling results.
- `tensorflow_debug(data)`: This method uses TensorFlow Debugger to dump root tensors and run the model.
- `mlflow_track(param, metric, artifact)`: This method uses MLflow to track model parameters, metrics, and artifacts.

## Testing

We also have a `TestDebugging` class in `tests/test_debugging.py` which tests the methods of the `Debugging` class. The class has the following methods:

- `test_tensorboard_debug()`: This method tests the `tensorboard_debug` method of the `Debugging` class.
- `test_pytorch_profile()`: This method tests the `pytorch_profile` method of the `Debugging` class.
- `test_tensorflow_debug()`: This method tests the `tensorflow_debug` method of the `Debugging` class.
- `test_mlflow_track()`: This method tests the `mlflow_track` method of the `Debugging` class.

## Usage

To use the `Debugging` class, you need to create an instance of the class with a model as an argument. Then, you can call the methods of the class with appropriate arguments.

```python
from src.debugging import Debugging

# create an instance of the Debugging class
debugging = Debugging(model)

# call the methods of the Debugging class
debugging.tensorboard_debug(data, target)
debugging.pytorch_profile(data)
debugging.tensorflow_debug(data)
debugging.mlflow_track(param, metric, artifact)
```

To run the tests, you can use the following command:

```bash
python -m unittest tests/test_debugging.py
```
