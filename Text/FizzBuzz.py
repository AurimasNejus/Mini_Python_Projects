#Program that prints the numbers from 1 to 100, but for multiples of 3 prints Fuzz instead, multiples of 5 prints Buzz, multiples of both - 3 and 5 prints FizzBuzz
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    
    