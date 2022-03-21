# Mettre PCA9685 et Robit dans le microbit (v2 uniquement si avec thonny)
from robit import *

# Initialisation communication avec le mBot (dont PCA9685)
MBot = Robit()

# Essai buzzer
MBot.buzzer(50)   # Signal sonor 50 Hz
sleep(1000)       # Dodo
MBot.buzzer(5000) # Signal sonor 5000 Hz
sleep(1000)       # Dodo
MBot.clean()      # Arrêt du mBot
