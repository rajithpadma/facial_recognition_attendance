import streamlit as st
import cv2
import face_recognition
import numpy as np
from utils import capture_and_encode_face, compare_faces, load_known_faces, save_known_faces

st.title("Facial Recognition Attendance System")

known_faces = load_known_faces()  # Load registered faces

stage = st.radio("Select Stage", ["Login", "Register", "Authenticate"])

if stage == "Register":
    user_id = st.text_input("Enter User ID")
    if st.button("Capture and Register"):
        encoding = capture_and_encode_face()
        if encoding is not None:
            known_faces[user_id] = encoding.tolist() # Convert numpy array to list for JSON
            save_known_faces(known_faces)
            st.success(f"User {user_id} registered successfully!")
        else:
          st.error("No face detected. Please try again.")

elif stage == "Authenticate":
    user_id = st.text_input("Enter User ID to Authenticate")

    if st.button("Authenticate"):
        if user_id in known_faces:
            captured_encoding = capture_and_encode_face()
            if captured_encoding is not None:
                known_encoding = np.array(known_faces[user_id]) # Convert back to numpy array
                if compare_faces([known_encoding], captured_encoding):
                    st.success("Authentication successful!")
                else:
                    st.error("Authentication failed. Face doesn't match.")
            else:
              st.error("No face detected. Please try again.")

        else:
            st.error("User ID not found.")

elif stage == "Login":
    st.write("Login functionality can be added here (e.g., using passwords).")
    # You can integrate other login mechanisms here


# ... (Add attendance tracking/logging functionality) ...