```python
# Importing necessary libraries
from tensorboard import SummaryWriter
from torch.profiler import profile, record_function, ProfilerActivity
from tensorflow.python.debug.lib import debug_utils
from mlflow import log_metric, log_param, log_artifacts

class Debugging:
    def __init__(self, model):
        self.model = model
        self.writer = SummaryWriter()

    def tensorboard_debug(self, data, target):
        """
        Function to debug model using TensorBoard
        """
        self.writer.add_graph(self.model, data)
        self.writer.add_histogram('predictions', self.model(data), 0)
        self.writer.add_histogram('target', target, 0)
        self.writer.close()

    def pytorch_profile(self, data):
        """
        Function to profile model using PyTorch Profiler
        """
        with profile(activities=[ProfilerActivity.CPU], record_shapes=True) as prof:
            with record_function("model_inference"):
                self.model(data)
        print(prof.key_averages().table(sort_by="cpu_time_total", row_limit=10))

    def tensorflow_debug(self, data):
        """
        Function to debug model using TensorFlow Debugger
        """
        debug_utils.dump_root_tensors()
        self.model(data)

    def mlflow_track(self, param, metric, artifact):
        """
        Function to track model parameters, metrics, and artifacts using MLflow
        """
        log_param("param", param)
        log_metric("metric", metric)
        log_artifacts(artifact)
```
