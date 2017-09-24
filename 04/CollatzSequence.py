def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

print(collatz(4))
print(collatz(6))
print(collatz(521))
print(collatz(21))
print(collatz(63))
print(collatz(43))
print(collatz(1130))