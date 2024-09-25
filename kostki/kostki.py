import random
import re

def roll_dice(roll_expression):
    dice_parts = re.findall(r'(\d*)d(\d+)|([+-]?\d+)', roll_expression)
    results = []
    total_sum = 0

    for x in dice_parts:
        if x[0]:
            num_dice = int(x[0]) if x[0] else 1 
            num_sides = int(x[1])
            dice_rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
            results.append("(" + " + ".join(map(str, dice_rolls)) + ")")
            total_sum += sum(dice_rolls)
        elif x[2]:
            modifier = int(x[2])
            results.append(x[2])
            total_sum += modifier

    return results, total_sum

while True:
    polecenie = input("Podaj rzut: ")

    if polecenie.lower() == 'exit':
        print("Koniec programu.")
        break

    results, total_sum = roll_dice(polecenie)

    print(" + ".join(results), '=', total_sum)
