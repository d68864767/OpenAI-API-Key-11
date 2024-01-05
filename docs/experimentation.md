# Experimentation

This document provides an overview of the `Experimentation` class in the `src/experimentation.py` file.

## Overview

The `Experimentation` class provides methods for running experiments using different platforms and tools such as Google Cloud AI Platform, DVC, H2O.ai Driverless AI, and MLflow. 

## Methods

The `Experimentation` class has the following methods:

### `google_ai_platform_experiment(self, project_id, region, experiment_id)`

This method runs an experiment using Google Cloud AI Platform. It takes the following parameters:

- `project_id`: The ID of the Google Cloud project.
- `region`: The region of the Google Cloud project.
- `experiment_id`: The ID of the experiment.

### `dvc_experiment(self, data_file, params_file)`

This method runs an experiment using DVC. It takes the following parameters:

- `data_file`: The data file to be used in the experiment.
- `params_file`: The parameters file to be used in the experiment.

### `h2oai_experiment(self, server_url, username, password, dataset)`

This method runs an experiment using H2O.ai Driverless AI. It takes the following parameters:

- `server_url`: The URL of the H2O.ai server.
- `username`: The username for the H2O.ai server.
- `password`: The password for the H2O.ai server.
- `dataset`: The dataset to be used in the experiment.

### `mlflow_track(self, param, metric, artifact)`

This method tracks experiment parameters, metrics, and artifacts using MLflow. It takes the following parameters:

- `param`: The parameter to be tracked.
- `metric`: The metric to be tracked.
- `artifact`: The artifact to be tracked.

## Testing

The `tests/test_experimentation.py` file contains unit tests for the `Experimentation` class. To run the tests, use the following command:

```bash
python -m unittest tests/test_experimentation.py
```
