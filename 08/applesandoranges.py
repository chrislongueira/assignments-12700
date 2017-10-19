d_apple = [-2, 2, 1]
d_orange = [5, -6]
s_house = 7
t_house = 11

a_tree = 5
o_tree = 15

def apple_position(a, d, s, t):
    apple = 0
    for i in range(len(d)):
        x = a + d[i]
        if s <= x <= t:
            apple += 1
    
    return apple

def orange_position(b, d, s, t):
    orange = 0
    for i in range(len(d)):
        x = b + d[i]
        if s <= x <= t:
            orange += 1
    
    return orange

print(apple_position(a_tree, d_apple, s_house, t_house))
print(orange_position(o_tree, d_orange, s_house, t_house))