import random
import re

def roll_dice(roll_expression):
    dice_parts = re.split(r'(?=[+-])', roll_expression)
    results = []
    total_sum = 0
    
    for part in dice_parts:
        if "d" in part:
            dice = part.split("d")

            if dice[0].replace(" ","")=='':
                dice[0] = '1'
            elif dice[0].replace(" ","") == '-':
                dice[0]='-1'
            elif dice[0].replace(" ","") == '+':
                dice[0]='1'
            
            num_sides = int(dice[1].replace(" ",""))
            num_dice = int(dice[0].replace(" ",""))

            if num_dice  > 0:
                dice_rolls = [random.randint(1, num_sides ) for _ in range(num_dice )]
                results.append("(" + " + ".join(map(str, dice_rolls)) + ")")
                total_sum += sum(dice_rolls)
            elif num_dice  < 0:
                dice_rolls = [random.randint(1, num_sides ) for _ in range(abs(num_dice ))]
                results.append("- (" + " + ".join(map(str, dice_rolls)) + ")")
                total_sum -= sum(dice_rolls)
        else:
            results.append(part)
            total_sum += int(part.replace(" ","").replace("+",""))
    return results, total_sum

while True:
    expression = input("Dice to roll: \n")

    if expression.lower() == 'exit':
        break

    results, total_sum = roll_dice(expression)

    print(" + ".join(results).replace("+ -","- ").replace("+ +","+"), '=', total_sum)