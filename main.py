import cv2
import torch
import numpy as np
from PIL import Image
from facenet_pytorch import MTCNN
from transformers import ViTForImageClassification, ViTFeatureExtractor


# LOAD MODEL

IMAGE_MODEL_PATH = "image_models"

print("Loading image deepfake model...")

feature_extractor = ViTFeatureExtractor.from_pretrained(IMAGE_MODEL_PATH)
image_model = ViTForImageClassification.from_pretrained(IMAGE_MODEL_PATH)
image_model.eval()

mtcnn = MTCNN(image_size=224, margin=20)


# IMAGE PREDICTOR


def image_predictor(image_path):

    image = Image.open(image_path).convert("RGB")

    face = mtcnn(image)

    if face is None:
        return "No face detected", "0%", None

    face = face.permute(1,2,0).numpy()
    face = (face * 255).astype("uint8")
    face_img = Image.fromarray(face)

    inputs = feature_extractor(images=face_img, return_tensors="pt")

    with torch.no_grad():
        outputs = image_model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)[0]
        pred = torch.argmax(probs).item()

    labels = {0: "Real", 1: "Fake"}
    confidence = round(float(probs[pred]) * 100, 2)

    return f"The image is {labels[pred]}", f"Confidence: {confidence}%", face_img



# VIDEO PREDICTOR


def deepfakespredict(video_path):

    cap = cv2.VideoCapture(video_path)

    fake = 0
    real = 0
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % 15 == 0:

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(rgb)

            face = mtcnn(pil_img)

            if face is not None:
                face = face.permute(1,2,0).numpy()
                face = (face * 255).astype("uint8")
                face_img = Image.fromarray(face)

                inputs = feature_extractor(images=face_img, return_tensors="pt")

                with torch.no_grad():
                    outputs = image_model(**inputs)
                    pred = torch.argmax(outputs.logits, dim=1).item()

                if pred == 1:
                    fake += 1
                else:
                    real += 1

        frame_count += 1

    cap.release()

    total = fake + real

    if total == 0:
        return "No face detected", "0%", None

    fake_ratio = fake / total

    result = "The video is FAKE" if fake_ratio > 0.5 else "The video is REAL"
    confidence = f"Confidence: {round(fake_ratio*100,2)}%"

    return result, confidence, None
