###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll_1 = random.randint(0,6)
dice_roll_2 = random.randint(0,6)
dice_roll_3 = random.randint(0,6)
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print('Sum od dice rolled: ', total)