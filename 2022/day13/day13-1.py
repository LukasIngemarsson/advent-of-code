
index = -1
def createPacket(input):
    global index
    temp = []
    while index < len(input):
        index += 1
        if input[index] == '[':
            if index != 0:
                temp.append(createPacket(input))
        elif input[index] == ']':
            return temp
        else:
            temp.append(int(input[index]))  

def savePacket(input):
    packet = createPacket(input)
    global index; index = -1
    return packet

inOrder = True
def compareItem(item_one, item_two):
    global inOrder
    for i in range(0, len(item_one)):
        if len(item_two) == i:
            inOrder = False
            return
        elif isinstance(item_one[i], list) or isinstance(item_two[i], list):
            if not isinstance(item_two[i], list):
                item_two[i] = [item_two[i]]  
            elif not isinstance(item_one[i], list):
                item_one[i] = [item_one[i]]
            for j in range(0, len(item_one[i])):
                if len(item_two[i]) == 0:
                    inOrder = False
                    return
                elif isinstance(item_one[i][j], list) or len(item_two[i]) > j and isinstance(item_two[i][j], list):
                    compareItem(item_one[i][j], item_two[i][j])    
                elif len(item_two[i]) > j and item_one[i][j] > item_two[i][j]:
                    inOrder = False
                    return        
        else:
            if item_one[i] > item_two[i]:
                inOrder = False
                return
        if not inOrder:
            return  

def comparePacket(packet_one, packet_two):
    global inOrder
    compareItem(packet_one, packet_two)
    if inOrder:
        inOrder = True
        return True
    else:
        inOrder = True
        return False    

#######################################################

pair_nr = 1
inorder_indices = 0
ordered_indices = []
while True:
    line_one = input().replace('[', ',[,').replace(']', ',],').split(',')
    line_two = input().replace('[', ',[,').replace(']', ',],').split(',')
    while '' in line_one:
        line_one.remove('')
    while '' in line_two:
        line_two.remove('')

    packet_one = savePacket(line_one)
    packet_two = savePacket(line_two)

    if (comparePacket(packet_one, packet_two)):
        inorder_indices += pair_nr
        ordered_indices.append(pair_nr)

    pair_nr += 1            

    if input() == "#":
        print(inorder_indices)
        print(ordered_indices)
        break
