import random

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

def generate_text(d,start_word,length=50):
    wordlist = ""
    next = start_word
    for i in range(length):
        if next not in d:
            break
        wordlist.append(next)
        next = random.choice(d[next])
    return " ".join(wordlist)
    

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

def build_trigram(file):
    text = open(file).read()
    ret_dic = {}
    w_list = text.split()
    for i in range(len(w_list)-1):
        w = w_list[i].lower()
        w = remove_non_alpha(w)
        w2 = w_list[i+1].lower()
        w2 = remove_non_alpha(w2)
        #print (w,w2)
        ret_dic.setdefault((w,w2),[])
        for x in range(3):
            if (x+i < len(w_list)):
                w3 = w_list[i+x].lower()
                w3 = remove_non_alpha(w3)
                ret_dic[(w,w2)].append(w3)
    return ret_dic


hamlet = bwcff("hamlet.txt")
psalms = bwcff("psalms.txt")

p = build_trigram("hamlet.txt")
print(p)
sonnets = bwcff("sonnets.txt")