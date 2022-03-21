# Mettre PCA9685 dans le microbit (v2 uniquement si avec thonny)
from microbit import *
from PCA9685 import PCA9685

# Initialisation communication avec le PCA9685 via i2c
power = PCA9685()

# Essai Servo sur la broche 8
power.freq(50)      # fréquence de 50Hz sur les 16 broches
power.servo(8, 180) # Déclenchement servo angle 180 (0-180)
sleep(2000)         # Dodo
power.servo(8, 90)  # Remettre servo angle 90 (0-180) - Important ppour les servos continus !
power.reset()       # "Arrêt" des 16 broches