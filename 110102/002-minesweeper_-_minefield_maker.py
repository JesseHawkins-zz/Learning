import sys
import random

height = sys.argv[1]
width = sys.argv[2]
difficulty = sys.argv[3]  # 1 = HARD | 10 = EASY

grid = ""

for h in range(0, int(height)):
	for w in range (0, int(width)):
		temp = random.randint(0, int(difficulty))
		if temp == 0:
			grid = grid + "*"
		else:
			grid = grid + "."
		if w == int(width) - 1:
			grid = grid + "\n"

print str(height), str(width)
print grid