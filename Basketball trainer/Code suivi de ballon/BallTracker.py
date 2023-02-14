import argparse
import datetime
import numpy
import numpy as np
import time
import cv2
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
base_name = 'PNG/videos_Eurosmart/Lancerdeberet_'
file="D:/Ecole d'ingénieur/Année 2022-2023/Projet/Code suivi de ballon/Béret.avi"
cap = cv2.VideoCapture(file)

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=600, help="minimum area size")
ap.add_argument("-A", "--max-area", type=int, default=900, help="maximum area size")
args = vars(ap.parse_args())

# Définir le codec et création de l'objet VideoWriter
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('lancerdebéret.avi',cv2.VideoWriter_fourcc('I','4','2','0'),25.0,(width,height))
x1 = []
y1 = []
y2 = []
x3 = []
y3 = []
tab = (x1,y1)
n = 0
t = 0.0
dt = 0.0

while(cap.isOpened()):
    ret, frame = cap.read()
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    if ret == True:
        
        # Traitement de l'image avec les procédés qui paraissent les plus adaptés à la video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
        cv2.THRESH_BINARY,11,2)
        (cnts, _) = cv2.findContours(th2.copy(), cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE)
        
        # loop sur les contours
        for c in cnts :
            
            # si le contour est trop petit ou trop grand, l'ignorer
            if cv2.contourArea(c) < args["min_area"] or cv2.contourArea(c) > args["max_area"] :
                continue
            
            # calcul du cadre limitant les contours, et tracé de celui-ci sur l'image,
            (x, y, w, h) = cv2.boundingRect(c)
            if ((h - 20 < w < h + 20) and x < 540): # Pour éliminer les rectangles parasites

                # qui persistent malgré le précédent 'si' éliminatoire et ne garder
                # que celui qui concerne le béret (rectangle très proche d'un carré)
                n = n + 1
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.circle(frame,(x+w/2,y+h/2), int(math.sqrt((w/2)**2+(h/2)**2)), (0,0,255), 2)
                y2.append((y+h/2.0)*1.8/360.0)
                y0 = float(y2[0])
                x1.append((x+w/2.0)*3.2/640.0)
                y1.append(2*y0-(y+h/2.0)*1.8/360.0)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        if cv2.waitKey(10)== 27 : # touche Echap
            break
        
        # visualisation de l'image
        cv2.imshow("Lancer de béret", frame)
        cv2.imshow("Thresh", th2)
        writer.write(frame)

        # 100 millisecondes sur chaque image
        key = cv2.waitKey(100) & 0xFF

        t = t + dt
        dt = 1/ 25.0

        if n == fps - 4 :
            break
    if cv2.waitKey(10)== 27 :
        break

fig = plt.figure('Lancer de béret', figsize=(5,4))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 3), ylim=(0, 3))
ax.grid()

line, = ax.plot([], [], 'bo',markeredgecolor='r',markerfacecolor= 'black', markersize=8.0 )
line2, = ax.plot([], [], '--', lw=1)

time_template = 'time = %.2fs'
time_text = ax.text(0.05, 0.90, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    line2.set_data([], [])
    time_text.set_text('')
    return line, line2, time_text

def animate(i):
    thisx = x1[i]
    thisy = y1[i]
    x3.append(thisx)
    y3.append(thisy)
    line.set_data(thisx, thisy)
    line2.set_data(x3, y3)
    time_text.set_text(time_template%(i*dt))
    #fichier = base_name + '{:03d}'.format(i)
    # plt.savefig(fichier) # On sauvegarde un fichier par temps
    # plt.clf() # et on nettoie pour le suivant
    return line, line2, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(0, len(y1)),interval=400, blit=False, init_func=init, repeat = False)
plt.show()

# Nettoyage et fermeture de toutes les fenêtres
cap.release()
cv2.destroyAllWindows()
