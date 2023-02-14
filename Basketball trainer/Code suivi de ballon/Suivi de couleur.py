import cv2
import numpy as np

"""
[  0  50 130]
[  B  G  R]
"""
def testCouleur():
    # initialize OpenCV object and capture video
    cap = cv2.VideoCapture(0)


    # Capture frame-by-frame
    ret, frame = cap.read()

    print(frame[2])

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

def filtreCouleurRouge (coef_red, coef_green, coef_blue, cap):
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        #frame[:,:,1]=0
        frame[:,:,0]=0

        
        # Apply color filter for red channel
        """
        coef_red = 1
        coef_green = 1.4
        coef_blue = -4
        
        red_channel = frame[:,:,2]*coef_red + frame[:,:,1]*coef_green + frame[:,:,0]*coef_blue
        
        # Normalize values to [0, 255]
        red_channel = np.clip(red_channel, 0, 255)
        red_channel = red_channel.astype(np.uint8)
        """
        # Display the resulting frame
        cv2.imshow('FrameR', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def filtreCouleurVert (coef_red, coef_green, coef_blue, cap):
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame[:,:,2]=0
        frame[:,:,0]=0

        # Display the resulting frame
        cv2.imshow('FrameV', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def filtreCouleurBleue (coef_red, coef_green, coef_blue, cap):
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame[:,:,1]=0
        frame[:,:,2]=0

        
        # Apply color filter for red channel
        """
        coef_red = 1
        coef_green = 1.4
        coef_blue = -4
        
        red_channel = frame[:,:,2]*coef_red + frame[:,:,1]*coef_green + frame[:,:,0]*coef_blue
        
        # Normalize values to [0, 255]
        red_channel = np.clip(red_channel, 0, 255)
        red_channel = red_channel.astype(np.uint8)
        """
        # Display the resulting frame
        cv2.imshow('FrameB', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def main (coef_red,coef_green,coef_blue):
    # initialize OpenCV object and capture video
    cap = cv2.VideoCapture(0)

    jaune = (255,255,0)
    vert = (0,255,0)
    rouge = (255,0,0)
    bleu = (0,0,255)
    noir = (0,0,0)
    blanc = (255,255,255)
    bleuclair = (0,255,255)
    violet = (255,0,255)

    # Filter application
    filtreCouleurRouge (coef_red, coef_green, coef_blue,cap)
    filtreCouleurVert (coef_red, coef_green, coef_blue,cap)
    filtreCouleurBleue (coef_red, coef_green, coef_blue,cap)
 
    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()


