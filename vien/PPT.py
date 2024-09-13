import mediapipe as mp
import cv2
import numpy as np
import pyautogui
import time
def PPT():
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
        # Flip the image horizontally
        cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))

        l_hip_y = float(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y)
        l_wrist_y = float(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y)
        r_wrist_x = float(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x)
        r_wrist_y = float(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y)
        r_shoulder_x= float(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x)
        r_shoulder_y= float(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y)
        RE = float(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].x)
        RH2 = float(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].y)
        

        if(l_hip_y-l_wrist_y<0.2)&(r_wrist_y-r_shoulder_y<0.4):
          
          if(r_wrist_x-r_shoulder_x>0.1):
            pyautogui.press('left')
            print("left")
            pyautogui.sleep(1)
          elif(r_shoulder_x-r_wrist_x>0.1):
            pyautogui.press('right')
            print("right")
            
            pyautogui.sleep(1)
        elif(RE>0.4 and RH2<0.45):
          return

        if cv2.waitKey(5) & 0xFF == 27:
          break
      except:
        continue
  cap.release()
