import cv2
import numpy as np

# Lire l'image
img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Appliquer un filtre Gaussien pour �liminer le bruit
gray = cv2.medianBlur(gray, 5)

# Utiliser la transform�e de Hough pour d�tecter les cercles
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

# Dessiner les cercles d�tect�s sur l'image
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Dessiner le cercle ext�rieur
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Dessiner le centre du cercle
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

# Afficher l'image avec les cercles dessin�s
cv2.imshow("detected circles", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Dans ce code, nous utilisons la fonction cv2.HoughCircles pour d�tecter les cercles dans l'image en niveaux de gris. Les param�tres param1 et param2 sont utilis�s pour contr�ler la sensibilit� de la d�tection de cercles. La valeur de minRadius et maxRadius sont utilis�es pour limiter la taille des cercles d�tect�s.

# Ensuite, nous utilisons la fonction cv2.circle pour dessiner les cercles d�tect�s sur l'image d'origine. Pour afficher le r�sultat, on utilise cv2.imshow() puis on attend une touche pour fermer l'image.
