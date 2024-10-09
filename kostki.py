import random
import re


tokenSpecification = [
    ('DICE',     r'\d+d\d+'),
    ('NUMBER',   r'\d+'),
    ('PLUS',     r'\+'),
    ('MINUS',    r'\-'),
    ('WS',       r'\s+'),
]

pattern = re.compile('|'.join('(?P<%s>%s)' % pair for pair in tokenSpecification))

def tokenise(expression):
    tokens = []
    for mo in pattern.finditer(expression):
        kind = mo.lastgroup
        value = mo.group()
        if(kind == "NUMBER"):
            tokens.append((kind, int(value)))
        elif(kind == "WS"):
            continue
        else:
            tokens.append((kind, value))
    return tokens;

class Roller:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def roll(self):
        total_sum = 0
        results = []

        rolls, dsum = self.evaluate(self.tokens[self.pos])
        results.append(rolls)
        total_sum += dsum

        for token in self.tokens:
            if token[0] == "PLUS":
                rolls, dsum = self.evaluate(self.tokens[self.pos+1])
                results.append("+ "+rolls)
                total_sum += dsum
            elif token[0] == "MINUS":
                rolls, dsum = self.evaluate(self.tokens[self.pos+1])
                results.append("- "+rolls)
                total_sum -= dsum
            self.pos += 1
        return results, total_sum
                
    def evaluate(self, token):
        if token[0] == 'NUMBER':
            return str(token[1]), token[1]
        elif token[0] == 'DICE':
            num_dice, num_sides = self.splitDiceExpr(token[1])
            rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
            return "("+", ".join(map(str,rolls))+")", sum(rolls)
        
    def splitDiceExpr(self,dice_expr):
        expresion = dice_expr.split("d")
        return int(expresion[0]), int(expresion[1])
    

while True:
    if query := input("Dice to roll:") == "exit":
        break

    r1 = Roller(tokenise(query))
    results, total_sum = r1.roll()

    rolled_results = " ".join(map(str, results))
    total_sum_str = total_sum

    returner = f"**Rolled:** {rolled_results}\n**Sum:** {total_sum_str}"
    print(returner)
