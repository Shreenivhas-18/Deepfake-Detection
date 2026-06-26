# Deepfake Detection Project 🎥🔍

Welcome to the **Deepfake Detection Project**! This project utilizes advanced machine learning techniques to identify deepfake videos and images. Follow the instructions below to set up your environment and start detecting deepfakes. 🚀

---

# 📚 What is Deepfake Detection?

Deepfake detection involves identifying manipulated media, such as videos and images, where artificial intelligence has been used to alter the content. This project leverages machine learning models to differentiate between authentic and deepfake content, helping combat misinformation and improve digital media authenticity.

---

# 🛠️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Shreenivhas-18/Deepfake-Detection.git
cd Deepfake-Detection
```

---

## 2️⃣ Install Python

Install **Python 3.10.7** (recommended).

Download:
https://www.python.org/downloads/release/python-3107/

---

## 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 🤖 Download Pre-trained Models

The trained AI models are **not included** in this repository because they exceed GitHub's file size limits.

Download the model folders from Google Drive:

### 📥 Image Detection Model

https://drive.google.com/drive/folders/1tM2WrJs7EQMkVhuKKx4zuroIML4VxyCZ?usp=drive_link

### 📥 Video Detection Model

https://drive.google.com/drive/folders/19l6TswPDIaDrkT5x94yIT6g8bHaSneJg?usp=drive_link

After downloading, place the folders inside the project directory exactly like this:

```
Deepfake-Detection/
│── app.py
│── main.py
│── image_models/
│── Video_models/
│── templates/
│── static/
│── uploads/
│── requirements.txt
│── README.md
```

---

# ⚙️ Configure Model Paths

Open **main.py** and update the model paths if necessary.

Example:

```python
# Video Model
model = tf.keras.models.load_model(r"Video_models")

# Image Model
model_dir = r"image_models"
```

If the folders are placed in the project root as shown above, no further changes should be required.

---

# ▶️ Run the Application

```bash
python app.py
```

The application will start and be ready for deepfake detection.

---

# 📂 Project Structure

```
Deepfake-Detection/
│── app.py
│── main.py
│── templates/
│── static/
│── uploads/
│── image_models/
│── Video_models/
│── requirements.txt
│── README.md
│── LICENSE
```

---

# 🧠 Technologies Used

* Python
* TensorFlow
* OpenCV
* Vision Transformer (ViT)
* MTCNN
* Flask
* HTML
* CSS
* JavaScript

---

# 🤔 Troubleshooting

If you encounter any issues:

* Verify that Python 3.10.7 is installed.
* Ensure the virtual environment is activated.
* Confirm that both `image_models` and `Video_models` folders are downloaded and placed in the project root.
* Install all required dependencies using:

```bash
pip install -r requirements.txt
```

---

# 📖 How It Works

The application detects deepfake content using deep learning models trained on authentic and manipulated media.

### Workflow

1. Upload an image or video.
2. The application preprocesses the input.
3. The appropriate trained model analyzes the media.
4. The prediction (Real or Fake) is displayed with confidence.

---

# 📜 License

This project is intended for educational and research purposes.

---

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!
