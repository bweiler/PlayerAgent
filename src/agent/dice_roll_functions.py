import numpy as np   

#device roll functions


def hitroll(num_dice :int, strength :int, toughness :int) -> int:

    success_roll = 0
    if toughness == strength:
        success_roll = 4
    elif toughness > strength:
        if toughness >= strength*2:
            success_roll = 6
        else:
            success_roll = 5
    else:
        if toughness*2 <= strength:
            success_roll = 2
        else:
            success_roll = 3
    dice_for_hit_rolls = np.random.randint(low=1, high=6, size=(num_dice))
    # the array will be having 20 elements. 
    print(dice_for_hit_rolls)    
    success_hits = 0
    for single_roll in dice_for_hit_rolls:
        if single_roll >= success_roll:
            success_hits = success_hits + 1
    
    return success_hits




