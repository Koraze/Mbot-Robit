# Mettre PCA9685 et Robit dans le microbit (v2 uniquement si avec thonny)
from robit import *

# Initialisation communication avec le mBot (dont PCA9685)
MBot = Robit()

# Essai couleur avant
MBot.color(0, 20, 0, 0) # Led 0, couleur RGB (20, 0, 0), max (255, 255, 255)
sleep(1000)             # Dodo
MBot.color(1, 0, 20, 0) # Led 0, couleur RGB (20, 0, 0), max (255, 255, 255)
sleep(1000)             # Dodo
MBot.clean()            # Arrêt du mBot
