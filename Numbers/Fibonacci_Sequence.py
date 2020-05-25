# Generates specified length of fibonacci sequence 
def fibonacci_sequence(n):
    a = 1
    b = 1
    for x in range(n):
        yield a 
        a,b = b, a+b
for num in fibonacci_sequence(20):
    print(num)