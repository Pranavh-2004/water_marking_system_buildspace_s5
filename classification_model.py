import tensorflow as tf
import scipy
import PIL
import zipfile
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # type: ignore

tf.random.set_seed(42)

# Define ImageDataGenerators for training and testing

train_datagen_augmented = ImageDataGenerator(
    rotation_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    height_shift_range=0.2,
    width_shift_range=0.2,
)

test_datagen = ImageDataGenerator(
    # rescale=1./255
)
train_datagen = ImageDataGenerator(
    # rescale=1./255
)

# Flow training images in batches using the generator
train_data_augmented = train_datagen_augmented.flow_from_directory(
    "10_food_classes_all_data/train/",
    target_size=(128, 128),
    batch_size=32,
    class_mode="categorical",
    seed=42,
    shuffle=True,
)

# Flow validation images in batches using the generator
test_data = test_datagen.flow_from_directory(
    "10_food_classes_all_data/test/",
    target_size=(128, 128),
    batch_size=32,
    class_mode="categorical",
    seed=42,
)
train_data = train_datagen.flow_from_directory(
    "10_food_classes_all_data/train/",
    target_size=(128, 128),
    batch_size=32,
    class_mode="categorical",
    seed=42,
    shuffle=True,
)


# Creating CNN ( Ask sam if any doubts:) )

base_model = tf.keras.applications.EfficientNetB4(include_top=False)
base_model.trainable = False  # we are taking pre trained model so we shouldnt train it and disturb its accuracy

inputs = tf.keras.layers.Input(shape=(128, 128, 3))
x = base_model(inputs)
x = tf.keras.layers.GlobalAveragePooling2D()(x)
outputs = tf.keras.layers.Dense(10, activation="softmax")(x)
model = tf.keras.models.Model(inputs, outputs)
model.summary()
model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    metrics=["accuracy"],
)

# epoch creation

model.fit(
    train_data_augmented,
    epochs=3,
    validation_data=test_data,
    steps_per_epoch=len(train_data),
    validation_steps=int(0.2 * len(test_data)),
)

base_model.trainable = True
for i, layer in enumerate(base_model.layers[:-10]):
    layer.trainable = False

model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(
        learning_rate=0.0001
    ),  # new learning rate after changing layers=old learning rate/10
    metrics=["accuracy"],
)
model.fit(
    train_data_augmented,
    epochs=6,
    validation_data=test_data,
    steps_per_epoch=len(train_data),
    validation_steps=int(0.2 * len(test_data)),
    initial_epoch=3,
)

base_model.trainable = True
for i, layer in enumerate(base_model.layers[:-10]):
    layer.trainable = False

model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(
        learning_rate=0.0001
    ),  # new learning rate after changing layers=old learning rate/10
    metrics=["accuracy"],
)
model.fit(
    train_data_augmented,
    epochs=6,
    validation_data=test_data,
    steps_per_epoch=len(train_data),
    validation_steps=int(0.2 * len(test_data)),
    initial_epoch=3,
)

model.evaluate(test_data)
# model.save("saved_model/Objects_model_1.keras")
model.save("saved_model/my_model.keras")
