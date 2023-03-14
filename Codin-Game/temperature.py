import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
result = 0
# the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an inte1ger ranging from -273 to 5526
    
    t = int(i)
    if t in range(-273,5526):
        if result == 0:
            result = t
        elif abs(t) < abs(result):
            result = t
        elif abs(t) == abs(result) and t > result:
            result = t

# Write an answer using print3
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(result)

