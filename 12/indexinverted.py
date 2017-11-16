#Write a routine that will build an inverted index.

import csv

def remove_nonalpha(w):
    letters = ""
    for l in w:
        if l.isalpha() or l=="'":
            l = l.lower()
            letters += l
    return letters


def make_dict(f):
    info = open(f)
    info = csv.DictReader(info)
    data = []
    for line in info:
        data.append(line)
    dict = {}
    for offender in data:
        statement = offender['Last Statement']
        number = offender['TDCJ Number']
        for word in statement.split(' '):
            word = remove_nonalpha(word)
            if word in dict:
                if number not in dict[word]:
                    dict[word].append(number)
            else:
                dict[word] = [number]
    return dict


def search_offenders(s):
    words = make_dict('offenders-clean.csv')
    return words[s]


print(make_dict('offenders-clean.csv'))
print("Numbers of inmates saying 'sorry' in their last statements: " + str(search_offenders('sorry')))