tot = 0

# while(True):
#      line = input()

#      if line == "exit":
#         print(tot)
#         break
#      elif line == "A Y" or line == "B Z" or line == "C X":
#         tot += 6
#      elif line == "A X" or line == "B Y" or line == "C Z":
#         tot += 3

#      if line.endswith("X"):
#         tot += 1
#      elif line.endswith("Y"):
#         tot += 2
#      else:
#         tot += 3   

while(True):
    line = input()

    if line == "exit":
        print(tot)
        break
    elif line.startswith("A"):
        if (line.endswith("X")):
            tot += 3
        elif (line.endswith("Y")):
            tot += 4
        else:
            tot += 8
    elif line.startswith("B"):
        if (line.endswith("X")):
            tot += 1
        elif (line.endswith("Y")):
            tot += 5
        else:
            tot += 9
    else:
        if (line.endswith("X")):
            tot += 2
        elif (line.endswith("Y")):
            tot += 6
        else:
            tot += 7

      