import random
dice_rolled = random.randint(1,6)
print('Dice rolled: ', dice_rolled)
special = dice_rolled == 1 or dice_rolled == 6
print('Special nukber(1 or 6): ', special)