#Write a function called fizz_buzz that takes an integer, N
# print each number, from 0 to N, on a new line
# if the number is evenly divisible by 3, print "Fizz"
# if the number is evenly divisible by 5, print "Buzz"
# if the number is evenly divisible by BOTH 3 and 5, print "FizzBuzz"

def fizz_buzz(number):
    for i in range(0, number):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} FizzBuzz")
        elif i % 3 == 0:
            print(f"{i} Fizz")
        elif i % 5 == 0:
            print(f"{i} Buzz")
        else: 
            print(i)


fizz_buzz(63)