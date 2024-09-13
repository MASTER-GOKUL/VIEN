import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import screen_brightness_control as sbc
def Brightness():
    pyautogui.FAILSAFE='FALSE'
    cap = cv2.VideoCapture(0)   
    cap. set(cv2.CAP_PROP_FRAME_WIDTH,160)
    cap. set(cv2.CAP_PROP_FRAME_HEIGHT,90)
    hand_detector = mp.solutions.hands.Hands()  
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    val = 0
    while True:
        _, frame = cap.read()   
        frame = cv2.flip(frame, 1) 
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks 
        try:
            if(len(hands)==1):
                if hands:
                    for hand in hands:
                        drawing_utils.draw_landmarks(frame, hand)    
                        landmarks = hand.landmark
                        for id, landmark in enumerate(landmarks):
                            x = int(landmark.x*frame_width)
                            y = int(landmark.y*frame_height)
                            if id == 8:
                                cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255, 255))
                                x1 = x
                                y1 = y
                            if id == 4:
                                cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255, 255))
                                x2 = x
                                y2 = y
                    dis = ((x2-x1)**2 + (y2-y1)**2)**(0.5)//2
                    #print(dis)
                    blevel = np.interp(dis,[0,60],[0,100])
                    val = np.interp(dis, [0, 50],[300,80])
                    blevel = int(blevel)
                    sbc.set_brightness(blevel)
                    #print(blevel)
                    cv2.rectangle(frame,(20,80),(85,300),(0,255,255),4)
                    cv2.rectangle(frame, (20, int(val)), (85, 300), (0, 0, 255), -1)
                    cv2.putText(frame,str(blevel)+'%',(20,330),cv2.FONT_HERSHEY_COMPLEX,1,
                               (255,0,0),3)
            elif(len(hands)== 2):
                return
        except:
            continue
        cv2.imshow('Virtual Mouse', frame)  
        cv2.waitKey(1)  
