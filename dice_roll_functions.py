#device roll functions


def hitroll(num_dice :int, strength :int, toughness :int) -> int:
	int dice_for_hit_roll[num_dice]
	int success_roll, success_hits = 0, 0
	if toughness == strength:
		success_roll = 4
	elif toughness > strength:
		if toughness >= strength*2:
			success_roll = 6
		else
			success_roll = 5
	else
		if toughness*2 <= strength:
			success_roll = 2
		else
			success_roll = 3
		
	#generate random numbers 1-6 and assign to dice
	for single_roll in dice_for_hit_roll:
		if single_roll >= success_roll:
			success_hits = success_hits + 1
	
	return success_hits




