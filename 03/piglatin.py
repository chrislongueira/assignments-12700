#Write a program with a function piglatinify(s) which will be passed a string with a word in s and return the string converted to pig latin.

def piglatinify(s):
    first = s[0]
    if first in 'aeiou':
        return (s + 'ay')
    else:
        return (s[1:] + s[0] + 'ay')
    
print(piglatinify('elephant'))
print(piglatinify('computer'))
print(piglatinify('television'))
print(piglatinify('autobiography'))