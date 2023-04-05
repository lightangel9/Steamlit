import matplotlib.pyplot as plt
import streamlit as st

st.subheader('🤖 Python Code to build model for Image Classification')
st.success('**Install Library**')
code = '''!pip install streamlit
!pip install tensorflow
!pip install keras_applications
!pip install tensorflow-addons'''
st.code(code, language='python')

st.success('**Import Library**')
code = '''import os
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.layers import Dense,Conv2D,GlobalAveragePooling2D,Input
from tensorflow.keras.preprocessing.image import load_img, ImageDataGenerator
from tensorflow.keras import callbacks,optimizers
from PIL import Image
import numpy as np
from google.colab import drive'''
st.code(code, language='python')

st.success('**Prepare Dataset on Google Drive**')
code = '''drive.mount('/content/drive')'''
st.code(code, language='python')

code = '''%cd /content/drive/MyDrive/Dog/'''
st.code(code, language='python')

st.caption('First put files Train.zip and Test.zip in directory path')
st.caption('Train.zip included total 120 classes and have 100 images per class')
st.caption('Test.zip included total 120 classes and have 20 images per class')
code = '''!unzip Train.zip
!unzip Test.zip'''
st.code(code, language='python')

st.success('**Image Preprocessing**')
code = '''def img_Data(dir_path,target_size,batch,class_lst,preporcssing,):
  if preporcssing:
    gen_object = ImageDataGenerator(preprocessing_function=preporcssing)
  else:
    gen_object = ImageDataGenerator()

  return(gen_object.flow_from_directory(dir_path,
                                          target_size=target_size,
                                          batch_size=batch,
                                          class_mode='sparse',
                                          classes=class_lst,
                                          shuffle=True))
'''
st.code(code, language='python')

code = '''train_data_gen = img_Data("Train",(224,224),500,os.listdir("Train"),preprocess_input)
    valid_data_gen = img_Data("Test",(224,224),500,os.listdir("Test"),preprocess_input)'''
st.code(code, language='python')

st.success('**Define base model**')
code = '''base_model = tf.keras.applications.mobilenet_v2.MobileNetV2(
    input_shape=(224,224,3),
    alpha=1.0,
    include_top=False,
    weights='imagenet',
    input_tensor=None,
    pooling=None,
    classes=1000,
    classifier_activation='softmax',)'''
st.code(code, language='python')

st.success('**Pre-train model**')
code = '''base_model.trainable = False'''
st.code(code, language='python')

code = '''model = tf.keras.models.Sequential()
model.add(base_model)
model.add(GlobalAveragePooling2D())
model.add(Dense(1024,activation='relu'))
model.add(Dense(120,activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])'''
st.code(code, language='python')

code = '''model.summary()'''
st.code(code, language='python')

st.success('**Train model**')
code = '''elst = callbacks.EarlyStopping(monitor='val_loss',patience=5,mode='min')
save_ck = callbacks.ModelCheckpoint('.mdl_wt2.hdf5',save_best_only=True,monitor='val_loss',mode ='min')'''
st.code(code, language='python')

code = '''model.fit(train_data_gen,batch_size=500,validation_data=valid_data_gen,callbacks=[elst,save_ck],epochs=10)'''
st.code(code, language='python')

st.success('**Visualization Data**')
code = '''plt.plot(model.history.history['accuracy'], label='training accuracy')
plt.plot(model.history.history['val_accuracy'], label='validation accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.plot(model.history.history['loss'], label='training loss')
plt.plot(model.history.history['val_loss'], label='validation loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
'''
st.code(code, language='python')

# define the data
train_loss = [1.8038, 0.5357, 0.3422, 0.2379, 0.1750, 0.1335, 0.0989, 0.0734, 0.0598, 0.0478]
train_accuracy = [0,0.5897, 0.8303, 0.8943, 0.9305, 0.9557, 0.9695, 0.9833, 0.9901, 0.9924, 0.9962]
val_loss = [0.8115, 0.6790, 0.6555, 0.6531, 0.6331, 0.6417, 0.6465, 0.6384, 0.6374, 0.6484]
val_accuracy = [0,0.7569, 0.7906, 0.7964, 0.8047, 0.8068, 0.8156, 0.8102, 0.8185, 0.8114, 0.8147]

# create a figure and axis for Accuracy graph
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(train_accuracy, color='blue', linestyle='-', linewidth=2, label='Training Accuracy')
ax.plot(val_accuracy, color='orange', linestyle='--', linewidth=2, label='Validation Accuracy')
ax.legend()
ax.set_title('Training and Validation Accuracy')
ax.set_xlabel('Epochs')
ax.set_ylabel('Accuracy')
ax.set_xlim(0,9)

# display the plot
st.pyplot(fig)

# create a figure and axis for Loss graph
fig, ax = plt.subplots(figsize=(8,3))
ax.plot(train_loss, color='blue', linestyle='-', linewidth=2, label='Training Loss')
ax.plot(val_loss, color='orange', linestyle='--', linewidth=2, label='Validation Loss')
ax.legend()
ax.set_title('Training and Validation Loss')
ax.set_xlabel('Epochs')
ax.set_ylabel('Loss')
ax.set_xlim(0,9)

# display the plot
st.pyplot(fig)