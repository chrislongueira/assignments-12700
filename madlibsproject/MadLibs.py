import random

story = '''
A noun went to a noun and verb. The noun was adjective. adverb, the noun verb the noun.
'''

l = []

nouns = ['dog', 'cat', 'house', 'restaurant']
nouns2 = ['dog.', 'cat.', 'house.', 'restaurant.']
verbs = ['ate', 'walked', 'robbed', 'murdered']
verbs2 = ['ate.', 'walked.', 'robbed.', 'murdered.']
adjective = ['large.', 'thoughtful.', 'hungry.', 'friendly.']
adverb = ['Quickly,', 'Surprisingly,', 'Wildly,', 'Courageously,']

newstory = story.split()

for i in newstory:
    if i == 'noun':
        l.append(nouns[random.randrange(0, 4)])
    elif i == 'noun.':
        l.append(nouns2[random.randrange(0, 4)])
    elif i == 'verb':
        l.append(verbs[random.randrange(0, 4)])
    elif i == 'verb.':
        l.append(verbs2[random.randrange(0, 4)])
    elif i == 'adjective.':
        l.append(adjective[random.randrange(0, 4)])
    elif i == 'adverb,':
        l.append(adverb[random.randrange(0, 4)])
    else:
        l.append(i)

print(' ' .join(l))