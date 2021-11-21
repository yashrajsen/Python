import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = ''' My numbers is 122-438-4387. I work in CTS.
You can also reach out to my office numbers 203-234-3482 or 203-458-3291.
If you still could not find me then call 911-020-2938. '''

print(phoneRegex.findall(resume))       # returns a list of phone numbers strings 
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')      # grouping the first 3 numbers and remaining numbers.
print(phoneRegex.findall(resume))        # returns a list of tuples having the strings of the groups.
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume))        # returns a list of tuples having the strings of the combination of the groups.

# \d character class is short cut for (0|1|2|3|4|5|6|7|8|9)
# \D is for any character that is not a numeric digit from 0 to 9.
# \w is any letter, numeric digit, or underscore character.
# \W is any character that is not a letter, numeric digit or the underscore character.
# \s is any space ,tab or new line character.
# \S is any character that is not a space, tabl or newline.

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords  a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 parrridge in a pear tree.'
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))
xmasRegex = re.compile(r'\D+\S\W+')
print(xmasRegex.findall(lyrics)) 

## the [] syntax
# vowelRegex = re.compile(r'[aeiou]') # this is same as a|e|i|o|u
# letterRegex = re.compile(r'[a-z]')  # this can have a range by specifying a '-'
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoBoCOP eats BABY foOD'))
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('RoBoCOP eats BABY foOD'))

## Negative character classes by adding a ^. it does an opposite of the 
consonantsRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantsRegex.findall('RoBoCOP eats BABY foOD'))