```python
# Importing necessary libraries
import tensorflow as tf
import os

class StateManagement:
    def __init__(self, model):
        self.model = model

    def model_checkpointing(self, checkpoint_dir, max_to_keep=5):
        """
        Function to manage model checkpoints
        """
        # Create a callback that saves the model's weights
        cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_dir,
                                                         save_weights_only=True,
                                                         verbose=1,
                                                         max_to_keep=max_to_keep)

        # Train the model with the new callback
        self.model.fit(train_images, 
                       train_labels,  
                       epochs=10,
                       validation_data=(test_images,test_labels),
                       callbacks=[cp_callback])  # Pass callback to training

    def model_version_control(self, model_dir, model_version):
        """
        Function to manage model versions
        """
        # Save the model
        tf.saved_model.save(self.model, f"{model_dir}/{model_version}")

    def model_snapshot(self, snapshot_dir):
        """
        Function to create model snapshots
        """
        # Save the entire model as a single HDF5 file.
        self.model.save(f"{snapshot_dir}/my_model.h5")

    def model_migration(self, old_model_path, new_model_path):
        """
        Function to migrate models
        """
        # Load the old model
        old_model = tf.keras.models.load_model(old_model_path)

        # Save the old model to the new path
        old_model.save(new_model_path)
```
