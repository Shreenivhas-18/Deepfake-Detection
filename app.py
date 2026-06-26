from flask import Flask, request, jsonify, render_template
import os
import tempfile
from main import deepfakespredict, image_predictor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/analyze')
def Video_detect():
    return render_template('index.html')

@app.route("/upload")
def img_detect():
    return render_template('image.html')

# VIDEO API

@app.route('/deepfakespredict', methods=['POST'])
def deepfakespredict_endpoint():
    try:
        if 'video' not in request.files:
            return jsonify({'error': 'No video file provided'}), 400

        video_file = request.files['video']

        if not video_file.filename:
            return jsonify({'error': 'Invalid file'}), 400

        with tempfile.TemporaryDirectory() as temp_dir:
            video_path = os.path.join(temp_dir, video_file.filename)
            video_file.save(video_path)

            result_text, confidence_text, _ = deepfakespredict(video_path)

            return jsonify({
                'resultText': result_text,
                'confidenceText': confidence_text
            })

    except Exception as e:
        print(f"Error processing the video: {e}")
        return jsonify({'error': 'Internal server error occurred.'}), 500

# -------------------------
# IMAGE API
# -------------------------

@app.route('/imagepredict', methods=['POST'])
def image_predict_endpoint():

    if 'image' not in request.files:
        return jsonify({"resultText": "No image uploaded", "confidenceText": ""}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({"resultText": "No image selected", "confidenceText": ""}), 400

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = os.path.join(temp_dir, file.filename)
            file.save(image_path)

            result, confidence, face_img = image_predictor(image_path)

            return jsonify({
                "resultText": result,
                "confidenceText": confidence
            })

    except Exception as e:
        print(f"Error processing the image: {e}")
        return jsonify({"error": "Internal server error occurred."}), 500


if __name__ == '__main__':
    app.run(debug=True)
