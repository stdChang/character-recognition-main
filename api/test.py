import cv2
import typing
import numpy as np
from mltu.configs import BaseModelConfigs
from mltu.inferenceModel import OnnxInferenceModel
from mltu.utils.text_utils import ctc_decoder
from mltu.transformers import ImageResizer
from flask import Flask, jsonify, request


class ImageToWordModel(OnnxInferenceModel):
    def __init__(self, char_list: typing.Union[str, list], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.char_list = char_list

    def predict(self, image: np.ndarray):
        image = ImageResizer.resize_maintaining_aspect_ratio(
            image, *self.input_shape[:2][::-1]
        )

        image_pred = np.expand_dims(image, axis=0).astype(np.float32)

        preds = self.model.run(None, {self.input_name: image_pred})[0]

        text = ctc_decoder(preds, self.char_list)[0]

        return text


app = Flask(__name__)


def inference(m, i):
    predicted_text = m.predict(i)
    return predicted_text


"""
@app.route('/predict', methods=['POST'])
def infer_image():
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Check if 'url' is in the JSON payload
        if 'url' not in data:
            return jsonify(error="Please provide the 'url' in the JSON payload")

        image_url = data['url']

        # Fetch the image from the provided URL
        response = requests.get(image_url)
        response.raise_for_status()
        image_data = response.content

        configs = BaseModelConfigs.load("./configs.yaml")

        model = ImageToWordModel(model_path=configs.model_path, char_list=configs.vocab)

        if response.status_code == 200:
            # Specify the file name where you want to save the image
            file_name = 'downloaded_image.jpg'
            name = file_name

            # Open the file in binary write mode and save the image data
            with open(file_name, 'wb') as f:
                f.write(image_data)

        image = cv2.imread(name)

        # Perform inference
        prediction_text = model.predict(image)
        print("Prediction: ", prediction_text)

        try:
            os.remove(name)
            print(f"{name} deleted.")
        except OSError as e:
            print(f"Error deleting {name}: {e}")

        return jsonify(prediction=prediction_text)

    except Exception as e:
        return jsonify(error=f"An error occurred: {str(e)}")
"""


# Define an endpoint for making predictions
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get the image data from the request
        image_data = request.get_data()

        if not image_data:
            return jsonify({"error": "Image data is missing"})

        # Convert the image data to a NumPy array
        image_np = np.frombuffer(image_data, dtype=np.uint8)
        image_np = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

        configs = BaseModelConfigs.load("../model/configs.yaml")
        configs.model_path = "../model/model.onnx"

        model = ImageToWordModel(model_path=configs.model_path, char_list=configs.vocab)
        print("loaded model")
        prediction_text = model.predict(image_np)
        print("Prediction: ", prediction_text)

        # Return the prediction result as a JSON object
        return jsonify({"prediction_text": prediction_text})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
