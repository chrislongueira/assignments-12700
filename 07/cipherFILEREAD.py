import math
real_stats = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

def rotate_char(c, r):
    """
    Rotates character c by amount r. Wraps if past z.
    """
    v = ord(c)
    v = v - 97 # shift down so that 'a' is 0
    v = (v + r) % 26
    v = v + 97 # shift back up so that 'a' is 97
    result = chr(v)
    return result

def encode_string(s, r):
    """
    rotate a string (lowercase letters only)
    """
    result = ''
    for letter in s:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            letter = rotate_char(letter, r)
        result = result + letter
    return result

def full_encode(s):
    n = ''
    for i in range(26):
        n = n + encode_string(s, i) + '\n'
    return n

def distance(l1, l2):
    '''
    Euclidean distance between l1 and l2. If the lists are of
    different lengths, go to the length of the shorter one.
    '''
    length = len(l2)
    if len(l1) > len(l2):
        length = len(l2)
    sum = 0
    for i in range(length):
        sum = sum + (l1[i] - l2[i])*(l1[i]-l2[i])
    d = math.sqrt(sum)
    return d

def build_frequency_vector(s):
    #count the letters in the string
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v = []
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        v.append(s.count(letter) / num_letters)
    
    return v
    #count each letter to see how many times in appears

def print_vector_table(v):
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        print(s[i], ' : ', v[i])
        
def decode(s):
    values = []
    for i in range (0, 26):
        s_value = build_frequency_vector(encode_string(s, i))
        dis = distance(real_stats, s_value)
        values.append(dis)
    return encode_string(s, values.index(min(values)))

encodedstr = 'wklv lv d vwulqj wkdw zdv rqfh hqfrghg dqg qrz ghfrghg'
print(encodedstr)
print(decode(encodedstr))

f = open('sherlockholmes.txt')
r = f.read()
r = r.lower()
real_stats = build_frequency_vector(r)
f.close()
print(real_stats)