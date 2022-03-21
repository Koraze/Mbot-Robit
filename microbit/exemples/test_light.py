# Mettre PCA9685 et Robit dans le microbit (v2 uniquement si avec thonny)
from robit import *

# Initialisation communication avec le mBot (dont PCA9685)
MBot = Robit()

# Essai capteur de lumière
for i in range(30):
    print(MBot.light()) # Luminosité (min 0 - max 1)
    sleep(250)
MBot.clean()            # Arrêt du mBot
