# AI Model Deployment and Serving

This document provides an overview of the deployment and serving strategies implemented in our project. We have used TensorFlow Serving, ONNX Runtime, and Nvidia Triton Inference Server for model deployment and serving.

## TensorFlow Serving

TensorFlow Serving is a flexible, high-performance serving system for machine learning models, designed for production environments. It deals with the inference aspect of machine learning, taking models after training and managing their lifetimes, providing clients with versioned access via a high-performance, reference-counted lookup table.

In our project, we have a function `tensorflow_serving` in `src/deployment.py` that loads a TensorFlow model from a specified directory and serves it.

```python
def tensorflow_serving(self, model_dir, model_version):
    """
    Function to serve a TensorFlow model
    """
    # Load the model
    model = tf.saved_model.load(model_dir)

    # Serve the model
    tf.saved_model.save(model, f"{model_dir}/{model_version}")
```

## ONNX Runtime

ONNX Runtime is a performance-focused engine for ONNX (Open Neural Network Exchange) models, which inferences efficiently across multiple platforms and hardware (Windows, Linux, and Mac and on both CPUs and GPUs). ONNX Runtime has proved to considerably increase performance over multiple models and, as of now, supports ONNX 1.2 and higher.

In our project, we have a function `onnx_runtime` in `src/deployment.py` that loads an ONNX model from a specified path and serves it.

```python
def onnx_runtime(self, model_path):
    """
    Function to serve an ONNX model
    """
    # Load the model
    sess = InferenceSession(model_path)

    # Serve the model
    input_name = sess.get_inputs()[0].name
    label_name = sess.get_outputs()[0].name
    return sess, input_name, label_name
```

## Nvidia Triton Inference Server

Nvidia Triton Inference Server simplifies the deployment of AI models at scale in production. It supports a wide range of AI frameworks.

In our project, we have a function `nvidia_triton` in `src/deployment.py` that serves a model using Nvidia Triton Inference Server.

```python
def nvidia_triton(self, model_repository, model_name, model_version):
    """
    Function to serve a model using Nvidia Triton Inference Server
    """
    # Create a gRPC stub
    channel = grpc.insecure_channel('localhost:8001')
    grpc_stub = service_pb2_grpc.GRPCInferenceServiceStub(channel)

    # Create a request for model status
    request = service_pb2.StatusRequest(model_name=model_name)

    # Get model status
    response = grpc_stub.Status(request)

    # Check the model version status
    version_status = response.model_status[model_name].version_status[model_version]
    if version_status.ready_state == service_pb2.ModelReadyState.READY:
        print(f"Model {model_name} (version {model_version}) is ready to serve requests.")
    else:
        print(f"Model {model_name} (version {model_version}) is not ready to serve requests.")
```

## Model Deployment Best Practices

We also have a function `model_deployment_best_practices` in `src/deployment.py` that outlines the best practices for model deployment.

```python
def model_deployment_best_practices(self):
    """
    Function to outline model deployment best practices
    """
    print("""
    1. Test the model thoroughly before deployment.
    ...
    """)
```

## Testing

We have also written tests for these deployment strategies in `tests/test_deployment.py`.

```python
class TestDeployment(unittest.TestCase):
    def setUp(self):
        self.deployment = Deployment('test_model')

    def test_tensorflow_serving(self):
        ...
    def test_onnx_runtime(self):
        ...
    def test_nvidia_triton(self):
        ...
```
