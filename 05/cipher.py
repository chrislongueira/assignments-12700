def encode_letter(c,r):
    lowercase='abcdefghijklmnopqrstuvwxyz'
    uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if c in lowercase:
        c_loc = lowercase.index(c)
        new_loc = c_loc + r
        if new_loc > 25 or new_loc < -25:
            new_loc =  new_loc % 26
        return lowercase[new_loc]
    elif c in uppercase:
        c_loc = uppercase.index(c)
        new_loc = c_loc + r
        if new_loc > 25 or new_loc < -25:
            new_loc =  new_loc % 26
        return uppercase[new_loc]
    else:
        return c

def encode_string(s, r):
    str2 = ''
    for i in s:
        str2 += encode_letter(i, r)
    return str2

def full_encode(s):
    inp = ''
    for i in range(26):
        inp += str(i+1) + ': ' + encode_string(s, i)
        inp += '\n'
    return inp

print(encode_letter('f', 14))
print(encode_string('Knicks', 4))
print(full_encode('The Jets beat the Dolphins.'))