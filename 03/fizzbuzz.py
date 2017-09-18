#Write a program that prints the integers from 1 to 100 (inclusive).
#multiples of three = fizz, multiples of five = buzz, multiples of three and five = fizzbuzz

for x in range (1,101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)