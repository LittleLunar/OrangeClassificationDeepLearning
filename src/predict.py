import numpy as np
import os
import tensorflow as tf

CWD = os.getcwd().replace('\\','/')
MODEL_JSON_PATH = ""
MODEL_WEIGHTS_PATH = ""

model_json_file = open(MODEL_JSON_PATH,'r')
predict_model = tf.keras.models.model_from_json(model_json_file.read())
predict_model.load_weights(MODEL_WEIGHTS_PATH)
predict_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss=tf.keras.losses.categorical_crossentropy, metrics = ['accuracy'])

img = tf.keras.preprocessing.image.load_img(f'{CWD}/images/test/clementine/1000.jpg', target_size=(224,224))
X= tf.keras.preprocessing.image.img_to_array(img)
X= np.expand_dims(X,axis=0)
image = np.vstack([X])
val = predict_model.predict(image)
print("Val : ",end="")
print(val[0][0])
