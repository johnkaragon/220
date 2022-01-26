# Guide to for loops
"""
Again, when working with any problem, use the 6 steps od problem-solving

Problem: Calculate balance of bank account after 10 years of accruing interest

Analysis: Find how much money is in the account after 10 years of interest

"""
principal = eval(input("Enter the starting balance: "))
apr = eval(input("Enter the interest rate: "))
for i in range(10):
    principal = principal * (1+apr)
print(principal)