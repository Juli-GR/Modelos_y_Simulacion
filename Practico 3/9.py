import numpy as np

N = 1000000

def dice_roll():
    return np.random.randint(low=1, high=7)

def win_game():
    fst_dice = dice_roll()
    if fst_dice in [1, 6]:
        return dice_roll()*2 > 6
    else:
        return dice_roll() + dice_roll() > 6

expected = 5/9

count = 0

for _ in range(N):
    if win_game(): count += 1

print(f"Expected value: {expected}")
print(f"N={N}: {count/N}")