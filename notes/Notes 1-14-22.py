"""
Steps for problem-solving
1.) Analysis
    - understand the problem
2.) Specifications
    - What will you need in your program (inputs, outputs, etc...)
3.) Design ... "Pseudocode"
    -y
4.) Implementation
5.) Test
6.) Maintain
"""


def convert():
    celsius = eval(input("What is the temp in celsius? "))
    fahrenheit = celsius * (9 / 5) + 32
    print("That temp is ", fahrenheit, " in degrees fahrenheit")


literal = 3  # literal variable: a variable whose value is strictly defined. ie, not calculated or inputted
for i in range(0,10,2):
    print(i*literal, "\n")