from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
from model.resnet import ResNet50
import pickle
import logging
import os
from data.data import load_set
JSON_CONFIG = 'config.json'


''''
## run it the first time to get class_names
classes_dict = load_set('Dataset/', only_dict=True)
# Open a file in write binary mode
with open("data.pkl", "wb") as f:
    # Serialize the dictionary using pickle.dump()
    pickle.dump(classes_dict, f)'''


def predict_img(model_folder, img_file, classes_dict, debug=False):
    weights = os.path.join(model_folder, 'model.ckpt')
    n_classes = len(classes_dict)
    model = ResNet50(JSON_CONFIG, n_classes)
    image_path = str(img_file.filename)

    filenames = model.load_pred(image_path)
    #print("filenames",filenames)
    predictions = model.predict(weights, debug=debug)
    assert len(filenames) == predictions.shape[0]

    for i, file in enumerate(filenames):
        print(file)
        prediction = predictions[0]
        class_index = np.argmax(prediction)
        accuracy = prediction[class_index]
        class_name = classes_dict[class_index]
    return accuracy,class_name


# Create Flask app
app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    # Get the uploaded image file
    image_file = request.files["image"]
    # Generate a secure filename for the image
    filename = secure_filename(image_file.filename)
    # Save the image to a temporary file
    image_file.save(filename)

    # Open and preprocess the image
    image = Image.open(filename)


    # Load the dictionary
    with open("data.pkl", "rb") as f:
        classes_dict = pickle.load(f)

    
    logging.info(classes_dict)
    # Predict the class using the ResNet model
    model_folder= 'training/epoch49'
    accuracy,class_name=predict_img(model_folder, image, classes_dict, debug=False)

    # Return the predicted class and probability in JSON format
    response = {
        "class": class_name,
        "probability": accuracy*100,
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

