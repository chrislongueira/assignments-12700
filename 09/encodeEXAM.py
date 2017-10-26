def encode(s):
  first = ''
  times = 1
  l = []
  for letter in s:
    if letter != first:
      if first:
        value = (times, first)
        l.append(value)
      else:
        times += 1
    else:
      value = (first, times)
      l.append(value)
  return l
        
  
print(encode("aaaa"))
print(encode("bbaaa"))
print(encode("aabccccdeeeeaaa"))