# Mettre PCA9685 et Robit dans le microbit (v2 uniquement si avec thonny)
from robit import *

# Initialisation communication avec le mBot (dont PCA9685)
MBot = Robit()

# Essai moteurs 1 et 2 (roues mBot)
MBot.dc_motor(1, 2000)  # Moteurs 1 et 2 - Demi tour Gauche
MBot.dc_motor(2, 2000)
sleep(250)              # Dodo 250 ms
MBot.dc_motor(1, -2000) # Moteurs 1 et 2 - Demi tour Droit
MBot.dc_motor(2, -2000)
sleep(250)              # Dodo 250 ms
MBot.dc_motor(1, 0)     # Moteurs 1 et 2 - Arrêt (l'arrêt du mBot n'arrête pas les moteurs)
MBot.dc_motor(2, 0)
MBot.clean()            # Arrêt du mBot
