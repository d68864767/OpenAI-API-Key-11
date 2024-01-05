# AI Model Documentation Platforms

This document provides an overview of the different methods used in our project for generating documentation for AI models. The `Documentation` class in `src/documentation.py` contains methods for generating documentation using Sphinx, Jupyter Notebook, Confluence, and Read the Docs.

## Sphinx Documentation

Sphinx is a tool that makes it easy to create intelligent and beautiful documentation. It was originally created for the Python documentation. 

In our project, we use Sphinx to generate HTML documentation for our AI models. The `sphinx_documentation` method in the `Documentation` class takes in the source directory, build directory, and config directory as arguments, and generates the documentation.

```python
def sphinx_documentation(self, source_dir, build_dir, config_dir):
    app = Sphinx(source_dir, config_dir, build_dir, build_dir, 'html')
    app.build()
    return app.statuscode
```

## Jupyter Notebook Documentation

Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text.

In our project, we use Jupyter Notebook to generate interactive documentation for our AI models. The `jupyter_notebook_documentation` method in the `Documentation` class takes in the path to the Jupyter notebook as an argument, and generates the documentation.

```python
def jupyter_notebook_documentation(self, notebook_path):
    kernel_manager, kernel_client = start_new_kernel()

    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': 'notebooks/'}})

    with open(notebook_path, 'wt') as f:
        nbformat.write(nb, f)

    return nb
```

## Confluence Documentation

Confluence is a collaboration wiki tool used to help teams to collaborate and share knowledge efficiently.

In our project, we use Confluence to generate online documentation for our AI models. The `confluence_documentation` method in the `Documentation` class takes in the page id, title, and body as arguments, and generates the documentation.

```python
def confluence_documentation(self, page_id, title, body):
    confluence = Confluence(
        url='https://your-domain.atlassian.net/wiki',
        username='email@example.com',
        password='api_token')

    status = confluence.update_page(
        parent_id = '123456',
        page_id = page_id,
        title = title,
        body = body)

    return status
```

## Read the Docs Documentation

Read the Docs simplifies software documentation by automating building, versioning, and hosting of your docs for you.

In our project, we use Read the Docs to generate online documentation for our AI models. The `read_the_docs_documentation` method in the `Documentation` class takes in the docstring as an argument, and generates the documentation.

```python
def read_the_docs_documentation(self, docstring):
    html = publish_string(source=docstring, writer_name='html')
    return html
```

## Testing

The `tests/test_documentation.py` file contains unit tests for the `Documentation` class. These tests ensure that the documentation generation methods are working correctly.

```python
class TestDocumentation(unittest.TestCase):
    def setUp(self):
        self.documentation = Documentation('test_model')

    def test_sphinx_documentation(self):
        statuscode = self.documentation.sphinx_documentation('source_dir', 'build_dir', 'config_dir')
        self.assertEqual(statuscode, 0)

    def test_jupyter_notebook_documentation(self):
        nb = self.documentation.jupyter_notebook_documentation('notebook_path')
        self.assertIsNotNone(nb)

    def test_confluence_documentation(self):
        status = self.documentation.confluence_documentation('page_id', 'title', 'body')
        self.assertTrue(status)

    def test_read_the_docs_documentation(self):
        html = self.documentation.read_the_docs_documentation('docstring')
        self.assertIsNotNone(html)
```
