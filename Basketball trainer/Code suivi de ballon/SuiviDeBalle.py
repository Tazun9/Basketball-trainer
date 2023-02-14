import cv2
import numpy as np

# Lire l'image
img = cv2.imread('test3.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Appliquer un filtre Gaussien pour éliminer le bruit
gray = cv2.medianBlur(gray, 5)

intparam2 = 10
nb_circle = 0
while nb_circle != 3:
    nb_circle = 0
    circles = []
    # Utiliser la transformée de Hough pour détecter les cercles
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=intparam2, minRadius=0, maxRadius=0)
    intparam2=intparam2+1
    nb_circle = circles.size
    print("nb_circle: ",nb_circle,"intparam2:",intparam2)
print("final : ", nb_circle)


# Dessiner les cercles détectés sur l'image
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Dessiner le cercle extérieur
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Dessiner le centre du cercle
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

# Afficher l'image avec les cercles dessinés
cv2.imshow("detected circles", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Dans ce code, nous utilisons la fonction cv2.HoughCircles pour détecter les cercles dans l'image en niveaux de gris. Les paramètres param1 et param2 sont utilisés pour contrôler la sensibilité de la détection de cercles. La valeur de minRadius et maxRadius sont utilisées pour limiter la taille des cercles détectés.

# Ensuite, nous utilisons la fonction cv2.circle pour dessiner les cercles détectés sur l'image d'origine. Pour afficher le résultat, on utilise cv2.imshow() puis on attend une touche pour fermer l'image.
