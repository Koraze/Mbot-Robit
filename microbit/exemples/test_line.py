# Mettre PCA9685 et Robit dans le microbit (v2 uniquement si avec thonny)
from robit import *

# Initialisation communication avec le mBot (dont PCA9685)
MBot = Robit()

# Essai suiveur de ligne connecté sur J3
for i in range(30):
    print(MBot.line(J3)) # Valeur sol [right left] : Blanc 1, Noir/vide 0
    sleep(250)
MBot.clean()            # Arrêt du mBot
