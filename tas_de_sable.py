#########################################
# groupe MI 3
# ABALIL YASMINE  
# MENNOUR THOMAS  
# ELIES ROMAIN
# PEMBELE GAEL
# https://github.com/uvsq22101081/projet_tas_de_sable.git
#########################################

#import des modules

import random as rd
import tkinter as tk

# variables globales

config = []

# fonctions

def config_vide() :
    global config
    config = [[0] * 3 for i in range(3)]
    


def config_aléatoire():
    config_vide()
    for i in range(3) :
        for j in range(3) :
            nbr_grains = rd.randint(0,9)
            config[i][j] += nbr_grains


def affichage_grille():
    
    x = 0
    y =0
    canvas.delete("all")
    for i in range(len(config)):
        x +=140
        for j in range(len(config[i])):
            y +=140
            canvas.config(bg="white")
            canvas.create_rectangle(0, 0, x, y)
            canvas.create_text( (x-HAUTEUR_GRILLE), (y-LARGEUR_GRILLE), text =str(config[i][j]), width=70)
        y=0



def générer_aléatoirement():
    config_aléatoire()
    affichage_grille()


def générer_vide():
    config_vide()
    affichage_grille()


def sauvegarde():
    fic_sauvegarde = open("configuration sauvegardée", "w")
    fic_sauvegarde.write(str(config))
    fic_sauvegarde.close()


def etape_automate():
    for i in range(len(config)) :
        config[i].insert(0, 0)
        config[i].insert(4, 0)
    config.insert(0, [0]*5)
    config.insert(4, [0]*5)
    for i in range(1, len(config)) :
        for j in range(1, len(config[0])) :
            if config[i][j] >= 4 :
                config[i-1][j] += 1
                config[i+1][j] += 1
                config[i][j-1] += 1
                config[i][j+1] += 1
                config[i][j] -= 4
    del config[0], config[3]
    for i in range(3) :
        del config[i][0], config[i][3]

<<<<<<< HEAD
config = [[2, 2, 3], [1, 6, 1], [3, 2, 1]]
etape_automate()
print(config)
=======

config_vide()
config_aléatoire()
config_aléatoire()
etape_automate()
print(config)





    
#CREATION DE LA FENETRE#

HAUTEUR_CANEVAS,LARGEUR_CANEVAS = 420,420
HAUTEUR_GRILLE, LARGEUR_GRILLE= 70,70


racine=tk.Tk()
racine.title("Ecoulement d'un tas de sable")
canvas = tk.Canvas(racine, height= HAUTEUR_CANEVAS, width=LARGEUR_CANEVAS,  bg="grey")
boutonaléatoire =tk.Button(racine, text="Génération aléatoire", command= générer_aléatoirement)
boutonvide =tk.Button(racine, text="Génération vide", command=générer_vide)
boutoncommencer =tk.Button(racine, text="Commencement")
canvas.grid(row=1, column=0, columnspan=3)
boutonaléatoire.grid(row=2, column=0)
boutoncommencer.grid(row=2, column=1)
boutonvide.grid(row=2, column=2)
racine.mainloop()

>>>>>>> ee3aba9988d0f9793c5c9a392e7cb85a74980d68
