#!/usr/bin/env python

'''
SOURCE: http://www.programming-challenges.com/pg.php?page=downloadproblem&probid=110102&format=html

Have you ever played Minesweeper? This cute little game comes with a certain operating system whose name we
can't remember. The goal of the game is to find where all the mines are located within a M x N field.

The game shows a number in a square which tells you how many mines there are adjacent to that square. Each
square has at most eight adjacent squares. The 4 x 4 field on the left contains two mines, each represented
by a ``*'' character. If we represent the same field by the hint numbers described above, we end up with
the field on the right:

*...
....
.*..
....
*100
2210
1*10
1110

Input

The input will consist of an arbitrary number of fields. The first line of each field contains two
integers n and m ( 0 < n, m$ \le$100) which stand for the number of lines and columns of the field,
respectively. Each of the next n lines contains exactly m characters, representing the field.

Safe squares are denoted by ``.'' and mine squares by ``*,'' both without the quotes. The first field
line where n = m = 0 represents the end of input and should not be processed.

Output

For each field, print the message Field #x: on a line alone, where x stands for the number of the
field starting from 1. The next n lines should contain the field with the ``.'' characters replaced
by the number of mines adjacent to that square. There must be an empty line between field outputs.

Sample Input

4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0

Sample Output

Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100
'''

import sys

listImport = []
lineNum = 1
sizeHolder = ""
sizeNum = []
prevGrab = 1
listCurrentField = []

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

with open('002-minesweeper_-_mines.txt', 'r') as f:
	for line in f:
		line = line.rstrip()
		listImport.append(line)
f.closed

print ""
print ""
print ""
print ""

for foo in listImport:
	if is_number(foo[0]):
		print "-" * 80
		lineNum += 1
		for i in range(len(foo)):
			if is_number(foo[i]):
				sizeHolder = sizeHolder + foo[i]
			else:
				sizeNum.append(sizeHolder)
				sizeHolder = ""
		sizeNum.append(sizeHolder)
		sizeHolder = ""
		grab = prevGrab + int(sizeNum[0])
		for bar in range(prevGrab, grab):
			listCurrentField.append(listImport[bar])
			lineNum += 1
		prevGrab = lineNum
		#### Field size and layout has been processed, now let's map it!		
		print "Field Size     :", sizeNum
		for i in range(0, len(listCurrentField)):
			print "Field Row " + str(i) + (" " * (5 - int(len(str(i))))) + " :", listCurrentField[i]
		print ""
		print "Mapping field..."
		print ""
		for foo in range(0, len(listCurrentField)):
			sys.stdout.write("Field Row " + str(foo) + (" " * (4 - int(len(str(foo))))) + "  : ")
			for bar in range(0, len(listCurrentField[foo])):
				if str(listCurrentField[foo][bar]) == "*":
					sys.stdout.write("*")
				else:
					### Look for mines...
					neighboringMines = 0
					### Skip these three if testing the first row
					if foo != 0:
						### UP & LEFT
						try:
							if str(listCurrentField[foo - 1][bar - 1]) == "*":
								neighboringMines += 1
						except:
							IndexError
						### UP
						try:
							if str(listCurrentField[foo - 1][bar]) == "*":
								neighboringMines += 1
						except:
							IndexError
						### UP & RIGHT
						try:
							if str(listCurrentField[foo - 1][bar + 1]) == "*":
								neighboringMines += 1
						except:
							IndexError
					### LEFT
					try:
						if str(listCurrentField[foo][bar - 1]) == "*":
							neighboringMines += 1
					except:
						IndexError
					### RIGHT
					try:
						if str(listCurrentField[foo][bar + 1]) == "*":
							neighboringMines += 1
					except:
						IndexError
					### DOWN & LEFT
					try:
						if str(listCurrentField[foo + 1][bar - 1]) == "*":
							neighboringMines += 1
					except:
						IndexError
					### DOWN
					try:
						if str(listCurrentField[foo + 1][bar]) == "*":
							neighboringMines += 1
					except:
						IndexError
					### DOWN & RIGHT
					try:
						if str(listCurrentField[foo + 1][bar + 1]) == "*":
							neighboringMines += 1
					except:
						IndexError
					### ... done looking for mines.
					### Print Results
					sys.stdout.write(str(neighboringMines))
			print ""
		### RESET
		sizeNum = []
		listCurrentField = []

print "-" * 80
print ""
print ""
print ""
print ""

