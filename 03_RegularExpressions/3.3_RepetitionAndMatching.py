import re
from types import NoneType

# ? character for optional and can come 0 or 1 time.
batRegex = re.compile(r'Bat(wo)?man')       # the string with ()? can come 0 or 1 time.
mo = batRegex.search('The adventures of Batman')
print(mo.group())
mo1 = batRegex.search('The adventures of Batwoman')
print(mo1.group())
# mo2 = batRegex.search('The adventures of Batwowoman')
# print(mo2.group())        # THis throws error.

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 444-2383.')
print(mo.group())

## * character for zero or more
batRegex = re.compile(r'Bat(wo)*man')
print(batRegex.search('The adventure of Batwowowoman').group())
print(batRegex.search('The adventure of Batman').group())

## + character for one or more
batRegex = re.compile(r'Bat(wo)+man')
print(batRegex.search('The adventure of Batwowowoman').group())
# print(batRegex.search('The adventure of Batman').group())

## if we literally want to match +*? characters.
regex = re.compile(r'\+\*\?')   #one occurence 
print(regex.search('I learned about +*? regex syntax').group())
regex = re.compile(r'(\+\*\?)+')        #one or more
print(regex.search('I learned about +*?+*?+*?+*? regex syntax').group())


##to get a specific number of occurence of a group, we can use {}
haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('He said "HaHaHa"').group())

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
print(phoneRegex.search('My numbers are 469-332-1105,203-4839,712-213-2374.Call me in any one these.').group())

## {x,y} at least x times and at most y times
haRegex = re.compile(r'(Ha){3,5}')
print(haRegex.search('He said "HaHaHaHa"').group())
# print(haRegex.search('He said "HaHa"').group())   # throws error  
print(haRegex.search('He said "HaHaHaHaHaHa"').group())     #doesnt throw error as it skips the last occurence.

## we can alse mention as {,5} or {3,}
digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('1234567890').group())  # returns 12345 which is longest string possible. This is called a greedy match
digitRegex = re.compile(r'(\d){3,5}?')
print(digitRegex.search('1234567890').group())  # returns 123 which is shortest string possible. This is called a non-greedy match