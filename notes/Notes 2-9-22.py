"""
Lists and Strings

Strings -
 - Sequence of characters
 - "Hello World"

Lists -
 - Sequence of objects
 - []
 - ["Paul", "John", "Rodrigo"]
 - [3, 4, 1, 5, 8, 0]
 - ["John", 32, 4.0, "Tuesday"]
 - b = [] (variable "b" is now a list)

len() - gets the length of a list or string

+ - Concatenation, "Join together"

slicing - produces a substring or sublist
<str>[<int> : <int> : <int>]  (string name, start, stop, step)

"""

a = "hello world"
for i in a:
    print(i)
print(len(a))
print(a[1: 11: 1])
