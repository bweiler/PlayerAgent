import numpy as np   

#device roll functions


def hitroll(num_dice :int, skill :int, modifier :int) -> int:

    success_hits = 0
    dice_for_hit_rolls = np.random.randint(low=1, high=7, size=(num_dice))
    # the array will be having 20 elements. 
    for single_roll in dice_for_hit_rolls:
        if single_roll == 6:
            success_hits = success_hits + 1
        elif (single_roll - modifier) >= skill and single_roll != 1:
                success_hits = success_hits + 1

    return success_hits

def woundroll(num_dice :int, strength :int, toughness :int) -> int:

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
    dice_for_wound_rolls = np.random.randint(low=1, high=7, size=(num_dice))
    # the array will be having 20 elements. 
    #print(dice_for_wound_rolls)    
    success_wounds = 0
    for single_roll in dice_for_wound_rolls:
        if single_roll >= success_roll:
            success_wounds = success_wounds + 1
    
    return success_wounds
    
def saveroll(num_dice :int, savevalue :int, AP :int, damage :int) -> int:

    dice_for_save_rolls = np.random.randint(low=1, high=7, size=(num_dice))
    # the array will be having 20 elements. 
    #print(dice_for_save_rolls)    
    success_saves = 0
    for single_roll in dice_for_save_rolls:
        if (single_roll + AP) >= savevalue:
            success_saves = success_saves + 1
    
    return (num_dice - success_saves) * damage
    
   
t_dice = 10
t_skill = 4
t_mod = 0
t_T = 4
t_S = 4
t_Sv = 3
t_AP = -1
t_D = 1

print("Test of 10 shooting phases")
print("Friendly: 10 Necron Warriors T4,A1,BS4,S4,AP-1,D1")
print("Enemy: 5 Assault Inter T4,Sv3,W2")
for i in range(0,10,1):
    print(" ")
    n_hits = hitroll(t_dice,t_skill,t_mod)
    print(f"D {t_dice}, WS {t_skill}, M {t_mod} Hits {n_hits}")
    n_wounds = woundroll(n_hits,t_S,t_T)
    print(f"D {n_hits}, T {t_T}, S {t_S} Wounds {n_wounds}")
    damage = saveroll(n_wounds,t_Sv,t_AP,t_D)
    print(f"D {n_wounds}, Sv {t_Sv}, AP {t_AP}, D {t_D} Damage {damage}")

  
