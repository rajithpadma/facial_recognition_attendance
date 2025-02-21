import cv2
import face_recognition
import numpy as np

def capture_and_encode_face():
    """Captures a frame from the camera and returns face encodings."""
    video_capture = cv2.VideoCapture(0)  # 0 usually is the default camera
    ret, frame = video_capture.read()
    video_capture.release()
    if not ret:
        return None  # No frame captured

    rgb_frame = frame[:, :, ::-1]  # BGR to RGB for face_recognition
    face_encodings = face_recognition.face_encodings(rgb_frame)

    if face_encodings:
        return face_encodings[0] # Return the first encoding (handle multiple faces if needed)
    else:
      return None

def compare_faces(known_encodings, captured_encoding):
    """Compares captured encoding with known encodings."""
    if known_encodings is None or captured_encoding is None:
        return False

    matches = face_recognition.compare_faces(known_encodings, captured_encoding)
    return any(matches) # Return True if there's at least one match

# ... (Add functions to load/save known encodings with user IDs) ...
# Example:
import json
def load_known_faces(filename="known_faces.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return empty dict if file doesn't exist

def save_known_faces(known_faces, filename="known_faces.json"):
    with open(filename, "w") as f:
        json.dump(known_faces, f)