import math

print(abs(-10))
print(abs(20.24))

# dot notation
result = math.sqrt(45)
print(result)
result = math.pow(2, 3)  # Parameters / Argument
print(result)
print(math.pi)

my_range = range(10)
print(list(my_range))
my_range = range(2, 21)  # start, stop
print(list(my_range))
my_range = range(3, 10, 2)  # Start, stop, step
print(list(my_range))

#  Accumulator pattern
my_sum = 0
for i in range(101):
    my_sum += i
print(my_sum)


def fact():
    num = eval(input("enter the number you would like to find the factorial of: "))
    starter = 1
    for j in range(num, 0, -1):
        starter = starter * j
    print(starter)


fact()
