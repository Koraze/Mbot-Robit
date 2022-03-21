# Mettre PCA9685 et Robit dans le microbit (v2 uniquement si avec thonny)
from robit import *

# Initialisation communication avec le mBot (dont PCA9685)
MBot = Robit()

# Essai servo broche 7
MBot.servo(7, 180) # Activation Servo 7 angle 180
sleep(5000)        # Dodo
MBot.servo(7, 90)  # Remise servo angle 90 (l'arrêt du mBot ne réinitialise pas les servos)
MBot.clean()       # Arrêt du mBot
