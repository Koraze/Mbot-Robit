# Mettre PCA9685 dans le microbit (v2 uniquement si avec thonny)
from microbit import *
from PCA9685 import PCA9685

# Initialisation communication avec le PCA9685 via i2c
power = PCA9685()

# Essai du moteur lié aux broches 0, 1 du PCA9685
power.freq(1000)         # fréquence de 1000Hz sur les 16 broches
power.dc_motor(0,  2048) # Moteur à la puissance 2048 (max 4095)
sleep(500)               # Dodo
power.dc_motor(0, -2048) # Moteur à la puissance 2048 (max 4095)
sleep(500)               # Dodo
power.reset()            # "Arrêt" des 16 broches