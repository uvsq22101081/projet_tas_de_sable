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

from numpy import diff

# variables globales

config = []

# fonctions

def config_vide() :
    '''Initialise la configuration courante avec une configuration vide de grains de sable'''
    global config
    config = [[0] * 3 for i in range(3)]
    


def config_aléatoire():
    '''Ajoute pour chaque case un nombre aléatoire de grains de sable compris entre 0 et 3'''
    config_vide()
    for i in range(3) :
        for j in range(3) :
            nbr_grains = rd.randint(0,3)
            config[i][j] += nbr_grains


def affichage_grille():
    '''Met à jour l'affichage de la grille dans l'interface graphique à partir de la configuration courante'''
    
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
    '''Ecrit la configuration courante dans un fichier sauvegarde'''
    fic_sauvegarde = open("configuration sauvegardée", "w")
    fic_sauvegarde.write(str(config))
    fic_sauvegarde.close()


def etape_automate():
    '''Réalise une étape de l'automate et met à jour l'affichage de la grille à chaque avalanche'''
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


def addition():
    '''Fait l'addition case par case de la configuration courante et d'une configuration choisie par l'utilisateur'''
    config2 = config
    for i in range(len(config)) :
        for j in range(len(config[0])) :
            config[i][j] = config[i][j] + config2[i][j]
    print(config)


def soustraction():
    '''Fait la soustraction case par case de la configuration courante et d'une configuration choisie par l'utilisateur.
    Si la différence est négative, le résultat vaut 0.'''
    config2 = config
    for i in range(len(config)) :
        for j in range(len(config[0])) :
            diff = config[i][j] - config2[i][j]
            if diff > 0 :
                config[i][j] = diff
            else :
                config[i][j] = 0

    
#CREATION DE LA FENETRE#

HAUTEUR_CANEVAS, LARGEUR_CANEVAS = 420,420
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