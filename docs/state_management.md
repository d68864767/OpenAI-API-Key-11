# State Management

State management in AI models involves the process of managing model checkpoints, version control, snapshots, and model migrations. This document provides an overview of the state management functionality implemented in our project.

## Model Checkpointing

Model checkpointing is a process that saves a model's weights at certain intervals so that you can resume from exactly where you left off. This is particularly useful in case of a long training process that could potentially be interrupted.

In our project, we have implemented a `model_checkpointing` function in the `StateManagement` class. This function takes in a directory path where the checkpoints will be saved and an optional parameter `max_to_keep` which specifies the maximum number of recent checkpoint files to keep. As training progresses, older checkpoints are deleted.

```python
def model_checkpointing(self, checkpoint_dir, max_to_keep=5):
    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_dir,
                                                     save_weights_only=True,
                                                     verbose=1,
                                                     max_to_keep=max_to_keep)
    self.model.fit(train_images, 
                   train_labels,  
                   epochs=10,
                   validation_data=(test_images,test_labels),
                   callbacks=[cp_callback])
```

## Model Version Control

Model version control is a method to manage multiple versions of the model. It allows us to keep track of various versions of the model, and revert to any previous version if needed.

In our project, we have implemented a `model_version_control` function in the `StateManagement` class. This function takes in a directory path and a version number, and saves the model to the specified directory with the version number.

```python
def model_version_control(self, model_dir, model_version):
    tf.saved_model.save(self.model, f"{model_dir}/{model_version}")
```

## Model Snapshot

A model snapshot is a saved state of the model at a particular point in time. It is similar to a checkpoint but is typically used less frequently.

In our project, we have implemented a `model_snapshot` function in the `StateManagement` class. This function takes in a directory path and saves the entire model as a single HDF5 file to the specified directory.

```python
def model_snapshot(self, snapshot_dir):
    self.model.save(f"{snapshot_dir}/my_model.h5")
```

## Model Migration

Model migration involves moving a model from one location to another. This can be useful in various scenarios such as moving a model from a development environment to a production environment.

In our project, we have implemented a `model_migration` function in the `StateManagement` class. This function takes in the old model path and the new model path, loads the model from the old path, and saves it to the new path.

```python
def model_migration(self, old_model_path, new_model_path):
    old_model = tf.keras.models.load_model(old_model_path)
    old_model.save(new_model_path)
```

## Testing

We have also implemented tests for each of these functions in the `TestStateManagement` class in the `test_state_management.py` file. These tests ensure that each function is working as expected.

```python
class TestStateManagement(unittest.TestCase):
    def setUp(self):
        self.model = Sequential([Dense(units=1, input_shape=[1])])
        self.state_management = StateManagement(self.model)
        self.checkpoint_dir = './checkpoints'
        self.model_dir = './models'
        self.snapshot_dir = './snapshots'
        self.old_model_path = './old_model'
        self.new_model_path = './new_model'
        os.makedirs(self.checkpoint_dir, exist_ok=True)
        os.makedirs(self.model_dir, exist_ok=True)
        os.makedirs(self.snapshot_dir, exist_ok=True)
        os.makedirs(self.old_model_path, exist_ok=True)
        os.makedirs(self.new_model_path, exist_ok=True)

    def test_model_checkpointing(self):
        self.state_management.model_checkpointing(self.checkpoint_dir)
        self.assertTrue(os.listdir(self.checkpoint_dir))

    def test_model_version_control(self):
        self.state_management.model_version_control(self.model_dir, '1')
        self.assertTrue(os.path.exists(f"{self.model_dir}/1"))

    def test_model_snapshot(self):
        self.state_management.model_snapshot(self.snapshot_dir)
        self.assertTrue(os.path.exists(f"{self.snapshot_dir}/my_model.h5"))

    def test_model_migration(self):
        self.model.save(f"{self.old_model_path}/my_model.h5")
        self.state_management.model_migration(f"{self.old_model_path}/my_model.h5", self.new_model_path)
        self.assertTrue(os.path.exists(f"{self.new_model_path}/my_model.h5"))
```
