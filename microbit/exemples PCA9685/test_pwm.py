# Mettre PCA9685 dans le microbit (v2 uniquement si avec thonny)
from microbit import *
from PCA9685 import PCA9685

# Initialisation communication avec le PCA9685 via i2c
power = PCA9685()

# Essai PWM sur la broche 14
power.freq(50)           # fréquence de 50Hz sur les 16 broches
power.pwm(14, 100, 1000) # Broche 14, mettre 1 à 100 et 0 à 1000 (intervalle 0-4095)
sleep(2000)              # Dodo
power.reset()            # "Arrêt" des 16 broches