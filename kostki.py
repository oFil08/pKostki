import random
import re

def roll_dice(roll_expression):
    dice_parts = re.split(r'\s*[\+]\s*', roll_expression)
    results = []
    total_sum = 0
    
    for part in dice_parts:
        if "d" in part:
            dice = part.split("d")
            if int(dice[0]) > 0:
                dice_rolls = [random.randint(1, int(dice[1])) for _ in range(int(dice[0]))]
                results.append("(" + " + ".join(map(str, dice_rolls)) + ")")
                total_sum += sum(dice_rolls)
            elif int(dice[0]) < 0:
                dice_rolls = [random.randint(1, int(dice[1])) for _ in range(abs(int(dice[0])))]
                results.append("- (" + " + ".join(map(str, dice_rolls)) + ")")
                total_sum -= sum(dice_rolls)
        else:
            results.append(part)
            total_sum += int(part);
    return results, total_sum

while True:
    expression = input("Dice to roll: \n")

    if expression.lower() == 'exit':
        break

    results, total_sum = roll_dice(expression)

    print(" + ".join(results).replace("+ - ","- "), '=', total_sum)