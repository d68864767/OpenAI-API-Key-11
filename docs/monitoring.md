# AI Model Monitoring and Alerting

This document provides an overview of the monitoring module of our AI project. The purpose of this module is to monitor the performance of our AI models and alert the relevant stakeholders when necessary.

## Libraries Used

- Prometheus: An open-source systems monitoring and alerting toolkit.
- Datadog: A monitoring service for cloud-scale applications, providing monitoring of servers, databases, tools, and services.
- New Relic: A software analytics product that helps you analyze and improve application interactions.

## Code Overview

The `monitoring.py` script contains a `Monitoring` class with the following methods:

- `process_request(t)`: This method simulates a delay in processing a request. The time taken to process the request is monitored using Prometheus's `Summary` metric type.

- `send_metrics_to_datadog(metric_name, metric_value)`: This method sends metrics to Datadog. The metrics are visualized as a time series on a Datadog dashboard.

- `record_custom_metrics_newrelic(metric_name, metric_value)`: This method records custom metrics in New Relic.

## Testing

The `test_monitoring.py` script contains unit tests for the `Monitoring` class. The tests use the `unittest` and `unittest.mock` libraries to test the functionality of the methods in the `Monitoring` class.

## Usage

To use the `Monitoring` class, create an instance of the class and call the desired methods. For example:

```python
monitor = Monitoring()
monitor.process_request(1)
monitor.send_metrics_to_datadog('test_metric', 1)
monitor.record_custom_metrics_newrelic('test_metric', 1)
```

## Conclusion

The monitoring module provides a way to monitor the performance of our AI models and alert the relevant stakeholders when necessary. It uses Prometheus, Datadog, and New Relic to monitor and visualize metrics.
