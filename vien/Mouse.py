'''from turtle import ht
import numpy as np'''
import cv2
import mediapipe as mp
import pyautogui
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
def Mouse():
        '''import matplotlib.pyplot as plt
        from IPython.display import Image'''
        pyautogui.FAILSAFE='FALSE'
        cap = cv2.VideoCapture(0)   # capture video '0' one cam
        cap. set(cv2.CAP_PROP_FRAME_WIDTH,160)
        cap. set(cv2.CAP_PROP_FRAME_HEIGHT,90)
        hand_detector = mp.solutions.hands.Hands()  # detect hand
        drawing_utils = mp.solutions.drawing_utils
        screen_width, screen_height = pyautogui.size()
        midpoint = [ screen_width/2, screen_height/2 ]
        '''print(screen_width, screen_height)'''

        index_y, index_x = 0, 0
        thumb_x, thumb_y = 0, 0
        mid_x, mid_y = 0, 0
        indbot_x, indbot_y = 0, 0
        '''pink_x, pink_y = 0, 0'''
        pmid_x, pmid_y = 0, 0
        drag, temp = 0, 0
        midd_x, midd_y = 0,0
        '''Smoothen the movement of mouse to stop at the exact position of,
           our hand movement without any shake in the movement of the mouse'''
        smoothening = 10
        plocx, plocy = 0, 0
        clocx, clocy = 0, 0


        while True:
                _, frame = cap.read()   # read data from cap
                '''Flip the frame or screen since the camera shows the mirror image,
                   of our hand and moves in opposite direction so we need to flip the screen'''
                frame = cv2.flip(frame, 1)
                 # shape gives frame height and width using shape 
                frame_height, frame_width, _ = frame.shape
                x_multiplier = screen_width/frame_width
                y_multiplier = screen_height/frame_height
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # detect on rgb frame color
                output = hand_detector.process(rgb_frame)
                hands = output.multi_hand_landmarks # hand landmark
                try:
                    if(len(hands)==1):
                            if hands:
                                for hand in hands:
                                    drawing_utils.draw_landmarks(frame, hand)   # see landmarks on frame 
                                    landmarks = hand.landmark
                                    
                                    for id, landmark in enumerate(landmarks):   # add counter
                                        # show the landmarks on kernel in x and y axis
                                        # x and y axis is multiplied by the height and width to get the x and y axis on the frames
                                        x = int(landmark.x*frame_width)
                                        y = int(landmark.y*frame_height)
                                        
                                        # print(x,y)
                                        # Index finger tip point number is 8
                                        # and draw a boundary to the point a circle


                                        #'''Middle finger tip is used for mouse tracking'''

                                        
                                        if id == 12:
                                            cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255, 255))
                                            # pyautogui.moveTo(x,y)
                                            mid_x = x_multiplier*x
                                            mid_y = y_multiplier*y
                                            # co-ordinates need to be changed 
                                            # smoothining varies with the change in the smoothening factor
                                            '''clocx = plocx + (mid_x - plocx) /smoothening
                                            clocy = plocy + (mid_y - plocy) /smoothening
                                            pyautogui.moveTo(clocx, clocy)#0, pyautogui.easeOutQuad
                                            plocx, plocy = clocx, clocy'''
                                            if mid_x < midpoint[0]:
                                                quicker_x = mid_x - (midpoint[0] - mid_x)/smoothening
                                            else:
                                                quicker_x = mid_x + (mid_x - midpoint[0])/smoothening
                                            if mid_y < midpoint[1]:
                                                quicker_y = mid_y - (midpoint[1] - mid_y)/smoothening
                                            else:
                                                quicker_y = mid_y + (mid_y - midpoint[1])/smoothening


                                                
                                            pyautogui.moveTo(quicker_x, quicker_y)
                                        
                                        # thumb tip point number is 4


                                        
                                        #'''index finger is used for left click'''


                                        if drag == 0:    
                                            if id == 5:
                                                cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255, 255))
                                                indbot_x = x_multiplier*x
                                                indbot_y = y_multiplier*y
                                            if id == 8:
                                                cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255, 255))
                                                index_x = x_multiplier*x
                                                index_y = y_multiplier*y
                                                if (abs(index_y - indbot_y) < 70) and (abs(index_x - indbot_x)<40):
                                                    print('Lclick')
                                                    pyautogui.click()
                                                    pyautogui.sleep(0.1)



                                        #'''thumb finger is used for right click'''

                                        
                                        if drag == 0:    
                                            if id == 4:
                                                cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255, 255))
                                                thumb_x = x_multiplier*x
                                                thumb_y = y_multiplier*y
                                                if (abs(indbot_x - thumb_x) < 30) and (abs(indbot_y - thumb_y) < 30):
                                                    print('Rclick')
                                                    pyautogui.click(button='right')
                                                    pyautogui.sleep(0.8)


                                            
                                        if id == 4:
                                            cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255, 255))
                                            thumb_x = x_multiplier*x
                                            thumb_y = y_multiplier*y
                                            if id == 8:
                                                cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255, 255))
                                                index_x = x_multiplier*x
                                                index_y = y_multiplier*y
                                            if(abs(index_y - thumb_y) < 40) and (abs(index_x - thumb_x) < 40) and (temp != 1):
                                                pyautogui.mouseDown()
                                                print('Mouse Down')
                                                drag, temp = 1, 1
                                            '''if id == 20:
                                                cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255, 255))
                                                pink_x = x_multiplier*x
                                                pink_y = y_multiplier*y
                                            if id == 17:
                                                cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255, 255))
                                                pmid_x = x_multiplier*x
                                                pmid_y = y_multiplier*y'''
                                            
                                        if (temp == 1):
                                            if id == 11:
                                                midd_x = x_multiplier*x
                                                midd_y = y_multiplier*y      
                                                if (abs(index_y - midd_y) < 70):
                                                    pyautogui.mouseUp()
                                                    print('Mouse Up')
                                                    drag, temp = 0, 0
                    elif(len(hands)==2):
                        return
                                        
                except:
                    continue
                cv2.imshow('Virtual Mouse', frame)  # show image
                cv2.waitKey(1)  # waits for key infinitely
