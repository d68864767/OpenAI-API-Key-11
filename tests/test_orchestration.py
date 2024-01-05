```python
# Importing necessary libraries
import unittest
from unittest.mock import patch, MagicMock
from src.orchestration import Orchestration

class TestOrchestration(unittest.TestCase):
    def setUp(self):
        self.model = MagicMock()
        self.orchestration = Orchestration(self.model)

    @patch('src.orchestration.DAG')
    @patch('src.orchestration.PythonOperator')
    def test_airflow_orchestration(self, mock_python_operator, mock_dag):
        tasks = {'task1': MagicMock(), 'task2': MagicMock()}
        dependencies = {'task1': ['task2']}
        self.orchestration.airflow_orchestration(tasks, dependencies)
        mock_dag.assert_called_once_with('model_pipeline', description='A pipeline to train and deploy AI model',
                                         schedule_interval='0 12 * * *',
                                         start_date=datetime(2021, 1, 1), catchup=False)
        self.assertEqual(mock_python_operator.call_count, len(tasks))

    @patch('src.orchestration.dsl.pipeline')
    @patch('src.orchestration.compiler.Compiler')
    def test_kubeflow_orchestration(self, mock_compiler, mock_pipeline):
        pipeline_func = MagicMock()
        self.orchestration.kubeflow_orchestration(pipeline_func)
        mock_pipeline.assert_called_once()
        mock_compiler.return_value.compile.assert_called_once_with(pipeline_func, 'model_pipeline.zip')

    @patch('src.orchestration.NiFi')
    def test_nifi_orchestration(self, mock_nifi):
        host = 'localhost'
        port = 8080
        process_group_id = '123'
        self.orchestration.nifi_orchestration(host, port, process_group_id)
        mock_nifi.assert_called_once_with(host=host, port=port)
        mock_nifi.return_value.pg.get.assert_called_once_with(process_group_id)
        mock_nifi.return_value.pg.get.return_value.schedule_components.assert_called_once_with(state='RUNNING')

if __name__ == '__main__':
    unittest.main()
```
