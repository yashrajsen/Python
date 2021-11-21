import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave secret documents to Agent Bob'))

#find the words and replace it with another string, we use sub () method
print(namesRegex.sub('Redacted','Agent Alice gave secret documents to Agent Bob'))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave secret documents to Agent Bob')) # returns A and B
print(namesRegex.sub(r'Agent \1****','Agent Alice gave secret documents to Agent Bob'))     # \1 means first group.
# returns Agent A**** gave secret documents to Agent B****


##Verbose method - can include spaces  and comments and allow mutli line string.
phoneRegex = re.compile (r'''
(\d\d\d-) |      # area code (without parenthesis , with dash)  | is OR condition
(\(\d\d\d\))     # - or - area code with parenthesis and no dash
 \d\d\d\         # first 3 digits
 -               # second dash
 \d\d\d\d        # last 4 digits
 \sx\d{2,4}      # extension like x1234
 ''',re.VERBOSE)

## if we need to add more arguments to the compile method
re.compile(r'[aeiou]',re.DOTALL | re.IGNORECASE | re.VERBOSE)