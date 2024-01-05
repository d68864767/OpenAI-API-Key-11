```python
# Importing required libraries
from prometheus_client import start_http_server, Summary
import time
from datadog import initialize, api
import newrelic.agent

# Prometheus settings
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Datadog settings
options = {
    'api_key':'<DATADOG_API_KEY>',
    'app_key':'<DATADOG_APP_KEY>'
}

initialize(**options)

# New Relic settings
newrelic.agent.initialize('<PATH_TO_NEW_RELIC_CONFIG_FILE>')

class Monitoring:
    def __init__(self):
        pass

    @REQUEST_TIME.time()
    def process_request(self, t):
        """A dummy function that simulates a delay."""
        time.sleep(t)

    def send_metrics_to_datadog(self, metric_name, metric_value):
        """
        This function sends metrics to Datadog.
        """
        title = "Time series for the metric"
        description = "Time series description"
        graphs = [{
            "definition": {
                "events": [],
                "requests": [
                    {"q": "avg:%s{*}" % metric_name}
                ],
                "viz": "timeseries"
            },
            "title": "My Timeboard"
        }]
        template_variables = [{
            "name": "host1",
            "prefix": "host",
            "default": "host:my-host"
        }]
        read_only = True

        api.Timeboard.create(title=title,
                             description=description,
                             graphs=graphs,
                             template_variables=template_variables,
                             read_only=read_only)

    def record_custom_metrics_newrelic(self, metric_name, metric_value):
        """
        This function records custom metrics in New Relic.
        """
        newrelic.agent.add_custom_parameter(metric_name, metric_value)

if __name__ == "__main__":
    # Create an instance of the Monitoring class
    monitor = Monitoring()

    # Start up the server to expose the metrics.
    start_http_server(8000)

    # Process requests
    while True:
        monitor.process_request(1)
```
