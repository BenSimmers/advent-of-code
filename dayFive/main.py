import re
from collections import defaultdict



def aocPart1():
  stacking = defaultdict(list)

  # Read input
  for l in open('inputnew.txt'):
    # If line starts with '[', then we need to move a number of discs from one stack to another
    if '[' in l:
      # Get the number of discs to move
      for i in range(1, len(l) - 1, 4):
        # If the character is not a space, then we need to move it
        if l[i] != ' ':
          stacking[(i - 1) // 4].append(l[i])
    # If line starts with 'move', then we need to move a number of discs from one stack to another
    elif l.startswith('move'):
      # Get the number of discs to move, the source stack, and the destination stack
      a, b, c = map(int, re.findall(r'\d+', l))
      # Move the discs
      stacking[c - 1] = stacking[b - 1][:a][::-1] + stacking[c - 1]
      stacking[b - 1] = stacking[b - 1][a:]
  # Print the result
  print(''.join(stacking[i][0] for i in range(len(stacking))))
aocPart1()




def aocPart2():
  stackingNew = defaultdict(list)
  # Read input
  for line in open('inputnew.txt'):
    # If line starts with '[', then we need to move a number of discs from one stack to another
    if '[' in line:
      # Get the number of discs to move
      for i in range(1, len(line) - 1, 4):
        # If the character is not a space, then we need to move it
        if line[i] != ' ':
          stackingNew[(i - 1) // 4].append(line[i])
    # If line starts with 'move', then we need to move a number of discs from one stack to another
    elif line.startswith('move'):
      # Get the number of discs to move, the source stack, and the destination stack
      a, b, c = map(int, re.findall(r'\d+', line))
      # Move the discs
      stackingNew[c - 1] = stackingNew[b - 1][:a] + stackingNew[c - 1]
      stackingNew[b - 1] = stackingNew[b - 1][a:]

  print(''.join(stackingNew[i][0] for i in range(len(stackingNew))))


aocPart2()