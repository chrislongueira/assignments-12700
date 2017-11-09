def remove_non_alpha(w):
    """
    input: w - string representing a "word"
    output: the string with non alpha chars removed
    """
    result=""
    for l in w:
        if l.isalpha():
            result = result + l
    return result

def bwcd(wordlist):
    d={}
    for w in wordlist:
        d.setdefault(w,0)
        d[w] = d[w] + 1
    return d

def bwcff(f):
    """
    input: f - string representing a filename
    returns: a dictionary with keys for words and values
             of the number of times each word occursb
    """
    text = open(f).read()
    l=[]
    for w in text.split():
        w = w.lower()
        w = remove_non_alpha(w)
        l.append(w)
    d = bwcd(l)
    return d

def word_dict(f):
    f = open(f).read()
    words = [remove_non_alpha(w) for w in f.split()]
    d = {}
    print (words)
    for i in range(0,len(words)-1):
        w = words[i]
        wnext = words[i+1]
        if w in d:
            d[w].append(wnext)
        else:
            d[w] = [wnext]
    last = words[len(words)-1]
    if last not in d:
        d[last] = []
    return d

d = bwcff("hamlet.txt")
print(word_dict('hamlet.txt'))