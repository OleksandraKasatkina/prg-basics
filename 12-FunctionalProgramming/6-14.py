BOTTLE_CAPACITY = 500
TOLERANCE_PERCENT = 2  # Allowable tolerance in percentage
MIN_FILL = BOTTLE_CAPACITY * (1 - TOLERANCE_PERCENT / 100)
MAX_FILL = BOTTLE_CAPACITY * (1 + TOLERANCE_PERCENT / 100)

fillings = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

def is_incorrect_fill(filling):
    return filling < MIN_FILL or filling > MAX_FILL

incorrect_bottles = list(filter(is_incorrect_fill, fillings))

incorrect_percentage = (len(incorrect_bottles) / len(fillings)) * 100

print(f"Bottle capacity:    {BOTTLE_CAPACITY}ml")
print(f"Filling tolerance:  {TOLERANCE_PERCENT}%")
print(f"Filled bottles:     {', '.join(map(str, fillings))}")
print(f"Incorrectly filled: {incorrect_percentage:.0f}%")