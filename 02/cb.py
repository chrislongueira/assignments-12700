#Warmup-2>string_times
def string_times(str, n):
  return str*n

#Warmup-2>front_times
def front_times(str, n):
  return str[0:3]*n

#Warmup-2>string_bits
def string_bits(str):
  result = ''
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

#Logic-2>lone_sum
def lone_sum(a, b, c):
  if a == b == c:
    return 0
  if b == c:
    return a
  if a == c:
    return b
  if a == b:
    return c
  else:
    return a + b + c

#Warmup-2>string_splosion
def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result

#Logic-1>cigar_party
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return (cigars >= 40)
  else:
    return (cigars >= 40 and cigars <= 60)

#Logic-1>caught_speeding
def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5
  if speed <=60:
    return 0
  if speed <=80:
    return 1
  else:
    return 2

first = string_times('Hi', 3)
print(first)

second = front_times('Chocolate', 3)
print(second)

third = string_bits('Hello')
print(third)

fourth = lone_sum(1, 2, 3)
print(fourth)

fifth = string_splosion('Code')
print(fifth)

sixth = cigar_party(30, False)
print(sixth)

seventh = caught_speeding(65, True)
print(seventh)