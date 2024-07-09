from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import tensorflow as tf
import requests
import hash  # import histogram_hash

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads/"

# Ensure the upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Google Drive file ID and download URL
file_id = "1875CZkQWUZDlehjCWxURdTSa6n2_xf0s"
model_url = f"https://drive.google.com/uc?export=download&id={file_id}"
model_path = "saved_model/my_model.keras"

# Download the model from Google Drive if it does not exist locally
if not os.path.exists(model_path):
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    response = requests.get(model_url)
    with open(model_path, "wb") as f:
        f.write(response.content)

# Load the pre-trained model
model = tf.keras.models.load_model(model_path)


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
            image_hash = hash.histogram_hash(file_path)

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
    app.run(debug=True)
