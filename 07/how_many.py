def freq(n, l):
    frequency = 0
    for i in l:
        if i == n:
            frequency += 1
    return frequency

def min(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min

def mode(l):
    newlist = []
    for i in l:
        newlist.append(freq(i, l))
    
    mode = newlist[i]
    for i in newlist:
        if mode < newlist[i]:
            mode = l[i]
    
    return mode

list1 = [1, 2, 3, 5, 6, 3, 4, 16, 27, 4, -1000, 5, 6, 9, 8, 3]
print('The list used in this program is ' + str(list1) + '.')
print('The number 3 appears in this list ' + str(freq(3, list1)) + ' times.')
print('The minimum value of this list is ' + str(min(list1)) + '.')
print('The mode of this list is ' + str(mode(list1)) + '.')