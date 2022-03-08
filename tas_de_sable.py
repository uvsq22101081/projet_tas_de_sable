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
    del config[0], config[3]
    for i in range(3) :
        del config[i][0], config[i][3]

config_vide()
config_aléatoire()
config_aléatoire()
etape_automate()
print(config)