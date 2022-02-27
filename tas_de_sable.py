#########################################
# groupe MI 3
# ABALIL YASMINE  
# MENNOUR THOMAS  
# GOD ELIES
#      GAEL
# https://github.com/uvsq22101081/projet_tas_de_sable.git
#########################################

#import des modules

import random as rd

# variables globales

config = []

# fonctions

def config_vide() :
    global config
    config = [[0] * 3 for i in range(3)]


def config_aléatoire():
    for i in range(3) :
        for j in range(3) :
            nbr_grains = rd.randint(0,3)
            config[i][j] += nbr_grains
