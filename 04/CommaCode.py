spam = ['apples', 'bananas', 'tofu', 'cats']

def commacode(List):
    List.insert(-1, 'and')
    together = List[0]
    for i in range(len(List) - 2):
        together = together + ', ' + List[i + 1]
    together = together + ' ' + List[-1]
    return together
    
print(commacode(spam))