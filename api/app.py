import os
import sys
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import tensorflow as tf
import requests
import keras

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from hash import histogram_hash

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "static/uploads/")

# Ensure the upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Google Drive file ID and download URL
file_id = os.getenv("GOOGLE_DRIVE_FILE_ID")
model_url = f"https://drive.google.com/uc?export=download&id={file_id}"
model_path = os.path.join(os.getcwd(), "api/saved_model/my_model.keras")

# Debug: Check the model path
print(f"Model path: {model_path}")

# Download the model from Google Drive if it does not exist locally
if not os.path.exists(model_path) or os.path.getsize(model_path) == 0:
    print("Model file does not exist locally. Downloading...")
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    response = requests.get(model_url)
    if response.status_code == 200:
        with open(model_path, "wb") as f:
            f.write(response.content)
        print("Model downloaded successfully.")
    else:
        print(f"Failed to download model, status code: {response.status_code}")
else:
    print("Model file already exists locally.")

# Verify model file existence after download
print(f"Model file exists after download: {os.path.exists(model_path)}")

# Check the file size to ensure it is not empty
if os.path.exists(model_path):
    print(f"Model file size: {os.path.getsize(model_path)} bytes")

# Load the pre-trained model
try:
    model = keras.models.load_model(model_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    sys.exit(1)


def predict_image(image_path):
    img_size = (128, 128)
    img = cv2.imread(image_path)
    img = cv2.resize(img, img_size)
    img = np.expand_dims(img, axis=0)

    # Make a prediction
    predictions = model.predict(img)

    # Print the entire predictions output to understand its structure
    print("Predictions:", predictions)
    print("Predictions type:", type(predictions))
    if isinstance(predictions, np.ndarray):
        print("Predictions shape:", predictions.shape)
        print("Predictions array:", predictions)

    # Convert predictions to desired format
    object_positions_list = []
    for pred in predictions:
        object_positions = []
        for i in range(
            0, len(pred), 4
        ):  # Assuming each object has 4 coordinates (a, b, c, d)
            if i + 4 <= len(pred):  # Check if there are enough values for unpacking
                a, b, c, d = pred[i : i + 4]
                object_positions.append({"x": [[a, b], [c, d]]})
            else:
                break
        object_positions_list.append({"objects": object_positions})

    print("Object Positions List:", object_positions_list)
    return object_positions_list


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            # Generate hash
            image_hash = histogram_hash(file_path)

            # Predict using the pre-trained model
            object_positions_list = predict_image(file_path)

            return render_template(
                "index.html",
                image_hash=image_hash,
                object_positions_list=object_positions_list,
                file_path=file_path,
            )
    return render_template(
        "index.html", image_hash=None, object_positions_list=None, file_path=None
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
