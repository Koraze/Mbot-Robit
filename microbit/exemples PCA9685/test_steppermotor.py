# Mettre PCA9685 dans le microbit (v2 uniquement si avec thonny)
from microbit import *
from PCA9685 import PCA9685

# Initialisation communication avec le PCA9685 via i2c
power = PCA9685()

# Essai moteur pas à pas 0-3
power.freq(25)               # "Vitesse" de 25Hz - La vitesse se règle ici sur un moteur pas à pas
power.stepper_motor(0, True) # Allumage moteur pas à pas, Activation sens 1 (1+, 0-)
sleep(2000)                  # Dodo
power.reset()                # Arrêt moteur pas à pas
