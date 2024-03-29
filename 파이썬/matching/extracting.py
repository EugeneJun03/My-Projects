import re
# re.search() returns a True/False depending on whether the string matches the regular expression
x = "My 2 favorite numbers are 19 and 47"
y = re.findall('[0-9]',x)
print(y)
"""
>>> ['2', '1', '9', '4', '7']
"""

# + means one or more digits
z = re.findall("[0-9]+", x)
print(z)
"""
['2', '19', '47']
"""

# you could also do the same with alphabets
a = re.findall("[abeF]+", x)
print(a)
"""
['a', 'e', 'be', 'a', 'e', 'a']
"""

"""The Greedy Matching: The repeat characters(* and +) push
outward in both directions(greedy) to match tha largest possible string"""
x = "From: Using the : character"
y = re.findall("^F.+:", x)
# ^F first character in the match is an F
# .+ one or more characters
# : last character in the match is a ":"
print(y)
"""
['From: Using the :']
"""
# if you want an None-Greedy Matching you just need to and "?"
y = re.findall("^F.+?:", x)
print(y)
"""
['From:']
"""


"""Fine-Tuning String Extraction: you can refine the match for re.findall()
and separately determine which portion of the match is to be 
extracted by using parentheses"""
x = "From stepthan.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('\S+@\S+', x) # \S+@\S+ at least one non-whitespace character
print(y)
y = re.findall("^From (\S+@\S+)", x) # you can add some informations to specify what you want to print
print(y)

