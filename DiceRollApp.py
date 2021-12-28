# Step 1: Utworzenie prostego programu losującego liczbę poprzez rzut kostką.
# Step 2: Update programu tak, aby zapamietywał poprzednio wylosowane liczby i losował kolejne na wypadek 
# # wystąpienia poprzedniej.
# Step 3: Update programu tak, aby zapisywał wyniku w pliku tekstowym.
# Step 4: Update programu tak, aby zapisywał wyniki i przypisywał je do daty dnia losowania
# -----------------------------------------------------------------------------------------------------------
import random

dice_roll = random.randint(1,6)
def diceRoll(dice_roll):
    if dice_roll == 1:
        print('30%')
    if dice_roll in range(2,4):
        print('40%')
    else:
        print('50%')

diceRoll(dice_roll)