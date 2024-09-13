import mediapipe as mp
import cv2
import numpy as np
import pyautogui
import speech_recognition as sr
from playsound import playsound
def Speech():
  pyautogui.FAILSAFE='FALSE'
  mp_drawing = mp.solutions.drawing_utils
  mp_drawing_styles = mp.solutions.drawing_styles
  mp_pose = mp.solutions.pose
  cap = cv2.VideoCapture(0)
  cap. set(cv2.CAP_PROP_FRAME_WIDTH,160)
  cap. set(cv2.CAP_PROP_FRAME_HEIGHT,90)
  with mp_pose.Pose( min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
      try:
        success, image = cap.read()
        results = pose.process(image)
        if not success:
          print("Ignoring empty camera frame.")
          continue

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        # Draw the pose
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        RE = float(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].x)
        RH2 = float(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].y)
        if(RE>0.4 and RH2<0.45):
          recognizer = sr.Recognizer()
          with sr.Microphone() as source:
            print("Say something...")
            audio = recognizer.listen(source)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            c=text.lower()
            a=["volume","brightness","mouse","presentation"]
            if "presentation" in c:
              playsound("./voice/ppt.mp3")
              return(a[3])
            if "mouse" in c:
              playsound("./voice/mouse.mp3")
              return a[2]
            if "brightness" in c:
              playsound("./voice/brightness.mp3")
              return a[1]
            if "volume" in c:
              playsound("./voice/sound.mp3")
              return a[0]
        # Flip the image horizontally
        cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
          break
      except:
        continue
  cap.release()

