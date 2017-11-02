def rle_decode(list):
    s = ''
    x = 0
    while x < len(list):
        if (str(list[x]).isdigit()):
            s += list[x] * list[x+1]
            x += 2
        else:
            s += list[x]
            x += 1
    return s

print(rle_decode([2, 'a', 3, 'b', 'c', 2, 'd']))