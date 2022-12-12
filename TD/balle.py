import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
COMPTEUR = 0

###################
# Fonctions

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon), (x+rayon, y+rayon), fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    global COMPTEUR
    if COMPTEUR < 20:
        rebond()
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, COMPTEUR
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if COMPTEUR < 10:
        if x0 <= 0 or x1 >= 600:
            balle[1] = -balle[1]
        elif y0 <= 0:
            canvas.move(balle[0], balle[1], balle[2]+360)
            COMPTEUR += 1
        elif y1 >= 400:
            canvas.move(balle[0], balle[1], balle[2]-360)
            COMPTEUR += 1
    else:
        if x0 <= 0 or x1 >= 600:
            balle[1] = -balle[1]
        if y0 <= 0 or y1 >= 400:
            balle[2] = -balle[2]
            COMPTEUR += 1
    if COMPTEUR == 10:
        canvas.create_line(0, 400, 600, 400, fill="white")
        canvas.create_line(0, 0, 600, 0, fill="white")


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
