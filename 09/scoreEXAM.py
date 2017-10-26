value_1 = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't']
value_2 = ['d', 'g']
value_3 = ['b', 'c', 'm', 'p']
value_4 = ['f', 'h', 'v', 'w', 'y']
value_5 = ['k']
value_8 = ['j', 'x']
value_ten = ['q', 'z']

def score(w):
  w.split()
  total = 0
  for i in value_1:
    total += 1
  for i in value_2:
    total += 2
  for i in value_3:
    total += 3
  for i in value_4:
    total += 4
  for i in value_5:
    total += 5
  for i in value_8:
    total += 8
  for i in value_ten:
    total += 10
  return total
  
print(score("hello"))