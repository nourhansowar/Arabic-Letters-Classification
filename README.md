# Valify
# Arabic Letters Classification using ResNet50
This project aims to classify Arabic letters using the ResNet50 model implemented in TensorFlow. The dataset used for training and testing the model is the Arabic Letters & Numbers OCR dataset available on Kaggle.

## Dataset
The dataset used for this task can be found at the following Kaggle link: Arabic Letters & Numbers OCR. It contains a collection of images representing Arabic letters and numbers. Ensure that you have downloaded and extracted the dataset before proceeding.

## Model
The ResNet50 model

### Training
To train the Arabic letters classification model, follow these steps:

Install the required dependencies, including Python 3.10 and TensorFlow 2.x.
Prepare the dataset by organizing the images into separate folders for each class. Refer to the dataset documentation for more details on the folder structure.
Open the terminal and navigate to the cloned resnet50-tensorflow repository.
Run the training script train.py with the appropriate command-line arguments:
```
$ python3 train.py -e=[number of epochs] -f=[path to dataset folder]
eg :  python3 train.py -e=50 -f=/home/norhan/Norhan/Dataset/
```
Replace `[number of epochs]` with the desired number of training epochs and `[path to dataset folder]` with the path to the prepared dataset folder.
During training, the script will output the training and validation accuracy and loss metrics. Additionally, the model weights will be saved in the training folder.


## Flask App

After training the model, a Flask application is created to serve predictions based on input images. Follow these steps to set up and run the Flask app:

Install the required dependencies, including Flask.

Open the terminal and navigate to the project folder
Run the Flask app using the following command:
```
$ python3 app.py
```
This will start the Flask server on a local port.
Use a tool like Postman to send a POST request to the Flask app's endpoint (/predict). Include an image file in the request body.

eg:  http://127.0.01:5000/predict
The app will process the image and return the predicted class and accuracy.


## Dockerization

To containerize the Flask app and run it using Docker, follow these steps:

Install Docker on your machine.

Create a Dockerfile in the project directory with the following content:

dockerfile
```
# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Expose the port that the application listens on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "app.py"]
```

Build the Docker image by running the following command in the terminal:

```
$ docker build -t arabic-classification .
```

Once the image is built, run the Docker container:

```
$ docker run -p 5000:5000 arabic-classification
```

The Flask app will be accessible on port 5000 of your local machine.

Use Postman or any other HTTP client to send a POST request to http://localhost:5000/predict with an image file in the request body.

The app will process the image and return the predicted class and accuracy.

Make sure to adjust the necessary paths and configurations according to your setup.

## Conclusion
By following the steps outlined in this README, you will be able to train a ResNet50 model on the Arabic Letters & Numbers OCR dataset, create a Flask app for serving predictions, and containerize the app using Docker. This will allow you to classify Arabic letters based on input images and obtain the predicted class and accuracy.

