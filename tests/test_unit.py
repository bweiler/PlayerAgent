from src.agent.dice_roll_functions import hitroll

num_dice = 6
toughness = 4
strength = 4
results = hitroll(num_dice, strength, toughness)

assert results <= num_dice, "result greater than number of dice"

