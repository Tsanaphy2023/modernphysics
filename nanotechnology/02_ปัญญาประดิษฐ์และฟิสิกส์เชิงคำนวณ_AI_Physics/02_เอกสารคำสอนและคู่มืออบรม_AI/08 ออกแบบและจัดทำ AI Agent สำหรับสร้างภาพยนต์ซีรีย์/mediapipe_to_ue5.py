import cv2
import mediapipe as mp
import socket
import json
import numpy as np

# Initialize MediaPipe Pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Setup UDP socket for sending tracking data to Unreal Engine 5
UDP_IP = "127.0.0.1"
UDP_PORT = 5065
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Starting MediaPipe Pose Tracking. Streaming to {UDP_IP}:{UDP_PORT}...")

# Initialize webcam
cap = cv2.VideoCapture(0)

with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = pose.process(image)

        # Draw the pose annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, COLOR_RGB2BGR if 'COLOR_RGB2BGR' in globals() else cv2.cvtColor(image, cv2.COLOR_RGB2BGR) if False else cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            
            # Extract landmark coordinates
            landmarks_data = {}
            for idx, landmark in enumerate(results.pose_landmarks.landmark):
                landmarks_data[str(idx)] = {
                    "x": landmark.x,
                    "y": landmark.y,
                    "z": landmark.z,
                    "visibility": landmark.visibility
                }
            
            # Convert to JSON string and send via UDP
            message = json.dumps(landmarks_data)
            sock.sendto(message.encode('utf-8'), (UDP_IP, UDP_PORT))

        # Display the resulting frame
        cv2.imshow('CineMatic AI - AR MediaPipe Tracker', image)
        
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
