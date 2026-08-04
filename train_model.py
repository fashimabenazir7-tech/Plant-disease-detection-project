import os
from disease_info import DISEASE_DATA
# List of classes matching disease_info.py
CLASS_NAMES = sorted(list(DISEASE_DATA.keys()))
MODEL_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'leaf_model.h5')
# Attempt TensorFlow Import
try:
    import numpy as np
    import tensorflow as tf
    from tensorflow.keras.models import Sequential, load_model as keras_load_model
    from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Rescaling
    HAS_TENSORFLOW = True
except ImportError:
    HAS_TENSORFLOW = False
    print("[Model Alert] TensorFlow or NumPy not found. CNN will run in Simulated Mode.")
class SimulatedCNNModel:
    def __init__(self):
        pass
    def predict(self, img_expanded):
        # Return mock probability vector matching CLASS_NAMES length
        num_classes = len(CLASS_NAMES)
        # Give a healthy or blight class a higher random weight for realism
        mock_probs = [0.05] * num_classes
        import random
        # Pick 2 classes to highlight
        idx1 = random.randint(0, num_classes - 1)
        idx2 = random.randint(0, num_classes - 1)
        mock_probs[idx1] = 0.65
        mock_probs[idx2] = 0.20
        # Normalize
        total = sum(mock_probs)
        mock_probs = [p / total for p in mock_probs]
        return [mock_probs]
def load_model(path):
    if HAS_TENSORFLOW:
        return keras_load_model(path)
    else:
        return SimulatedCNNModel()
def build_model(input_shape=(224, 224, 3), num_classes=len(CLASS_NAMES)):
    if not HAS_TENSORFLOW:
        return None
    model = Sequential([
        Rescaling(1./255, input_shape=input_shape),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model
def create_placeholder_model():
    if not HAS_TENSORFLOW:
        print("[Model] TensorFlow is missing. Skipping actual model file generation. Simulated model will load automatically.")
        return None
    print("Generating a pre-compiled CNN model for leaf disease detection...")
    model = build_model()
    model.save(MODEL_PATH)
    print(f"Model saved successfully to: {MODEL_PATH}")
    print(f"Supported Classes ({len(CLASS_NAMES)}): {CLASS_NAMES}")
    return model
def train_on_dataset(dataset_dir, epochs=10, batch_size=32):
    if not HAS_TENSORFLOW:
        print("[Model Error] Cannot train without TensorFlow/NumPy.")
        return
    print(f"Starting training on dataset from: {dataset_dir}")
    train_ds = tf.keras.utils.image_dataset_from_directory(
        dataset_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(224, 224),
        batch_size=batch_size
    )
    val_ds = tf.keras.utils.image_dataset_from_directory(
        dataset_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(224, 224),
        batch_size=batch_size
    )
    model = build_model(num_classes=len(train_ds.class_names))
    model.fit(train_ds, validation_data=val_ds, epochs=epochs)
    model.save(MODEL_PATH)
    print(f"Trained model saved successfully to: {MODEL_PATH}")
    
if __name__ == '__main__':
    # When run directly, generate a ready-to-use model file
    create_placeholder_model()
