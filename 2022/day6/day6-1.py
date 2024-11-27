
def hasDupes():
    for i in range(0, len(temp)):
            for j in range (i+1, len(temp)):
                if (temp[i] == temp[j]):
                    return True
    return False   

with open('input.txt', 'r') as f: 
    line = f.readline()

chars = list(line)
temp = []
counter = 0    

for i in range(0, 4):
    temp.append(chars[i])

while True:
    temp.append(chars[counter])
    temp.pop(0)
    counter += 1 
    if (hasDupes() == True):
        continue
    else:
        print(temp)
        print (counter)
        break





