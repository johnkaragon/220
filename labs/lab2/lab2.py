import math

print("This program will allow you to find the averages of a set of numbers")
size = eval(input("How large will this set of numbers be? "))
rms_avg = 0
harmonic_avg = 0
geo_avg = 1
exceptions = 0
for i in range(0, size):
    num = eval(input("Enter a new number of the set: "))
    rms_avg = rms_avg + (num ** 2)
    #if num != 0:
    harmonic_avg = harmonic_avg + (1 / num)
    #else:
    #    exceptions = exceptions + 1
    geo_avg = geo_avg * num
print(math.sqrt(rms_avg / size))
print((size - exceptions) / harmonic_avg)
print(geo_avg ** (1 / size))
