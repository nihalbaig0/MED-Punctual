import streamlit as st
from PIL import Image
import cv2
import numpy as np
import io
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

# Azure Custom Vision credentials (Get this from Azure custom vision)
ENDPOINT = ""      
PREDICTION_KEY = ""
PROJECT_ID = ""
MODEL_NAME = ""

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)


def detect_objects_in_image(image):
    """
    Detect objects in a single image using Azure Custom Vision.
    """
    # Convert PIL image to a bytes stream compatible with Azure Custom Vision
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format=image.format)
    img_byte_arr = img_byte_arr.getvalue()

    results = predictor.detect_image(PROJECT_ID, MODEL_NAME, img_byte_arr)

    # Convert PIL image to OpenCV format
    cv_image = np.array(image)
    cv_image = cv_image[:, :, ::-1].copy()  # Convert RGB to BGR

    for prediction in results.predictions:
        if prediction.probability >= 0.5:  # Threshold can be adjusted
            left = int(prediction.bounding_box.left * cv_image.shape[1])
            top = int(prediction.bounding_box.top * cv_image.shape[0])
            width = int(prediction.bounding_box.width * cv_image.shape[1])
            height = int(prediction.bounding_box.height * cv_image.shape[0])
            cv2.rectangle(cv_image, (left, top), (left + width, top + height), (255, 0, 0), 2)

    # Convert back to PIL format
    image = Image.fromarray(cv_image[:, :, ::-1])  # Convert BGR back to RGB

    return image


def main():
    st.title("Webcam Live Object Detection")

    # Widget to capture images from the user's webcam
    picture = st.camera_input("Take a picture")

    if picture:
        image = Image.open(picture)
        st.image(image, caption="Original Image")

        # Process the image for object detection
        processed_image = detect_objects_in_image(image)

        # Display the processed image
        st.image(processed_image, caption="Processed Image with Detected Objects")


if __name__ == "__main__":
    main()
