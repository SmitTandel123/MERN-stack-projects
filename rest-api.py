from flask import Flask, jsonify, request
from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import os
import tensorflow as tf
import numpy as np


app = Flask(__name__)
CORS(app)


def loadModel():
    model = tf.keras.models.load_model('cnn_version_1.h5')
    return model

def preprocess_image(filename, target_size=(128, 128)):
    image = tf.keras.preprocessing.image.load_img(filename, target_size=target_size)
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = image / 255.0  # Normalize the image data
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/', methods=['GET'])
def filename():
    if request.method == "GET":
        no_bedroom = int(request.args.get("no_bedroom"))
        no_bath = int(request.args.get("no_bath"))
        cars = int(request.args.get("cars"))
        model = loadModel()
        file_location = os.listdir("plans")
        array=[]
  
        for plans in file_location:
            plan=random.choice(file_location)
            img = preprocess_image(os.path.join("plans", plan))
            predictions = model.predict(img)
            bedroom_predictions = predictions[0].flatten().round().astype(int)
            bathroom_predictions = predictions[1].flatten().round().astype(int)
            cars_predictions = predictions[2].flatten().round().astype(int)
            if (no_bedroom == bedroom_predictions and no_bath == bathroom_predictions and cars == cars_predictions):
                array.append(plan)
        if(len(array)!=0):
            data = [{'filename': array}]
            return jsonify(data)
        return jsonify([{"filename": "NoMatch."}])

if __name__ == '__main__':
    app.run()
    

