import re
# ^ symbol is to start a string with
beginsWith = re.compile(r'^Hello')
print(beginsWith.search('Hello there!!'))

# $ symbol is used to end a string with
endsWith = re.compile(r'world!$')
print(endsWith.search('Hello world!'))

# ^ both $ means the pattern must match the entire string.
allDigitRegex = re.compile(r'^\d+$')
print(allDigitRegex.search('132324394854823789'))
print(allDigitRegex.search('1323243948x054823789'))

# '.' dot character means any character except new line
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))   # returns ' cat', ' hat', ' sat', 'flat' , ' mat'.. it has space in the first character.


## If we need to find firstname and last name from a string like below
## "First Name : Anil Last Name: Dev", we will use (.*)
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Anil Last Name: Dev'))     # returns [('Anil','Dev')]

## greedy and non greedy match
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))


prime = 'Serve the public trust. \nProtect the innocent. \nUpload the law.'
print(prime)
dotStar = re.compile(r'.*')
print(dotStar.findall(prime))

print(dotStar.search(prime))    # only get the string untill the new line character
# to get all the string including new line character , we can pass an arugument to the compile method
dotStar = re.compile(r'.*',re.DOTALL)
print(dotStar.search(prime).group())

# another argument for ignoring Case sensitivity
vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Hey Hi, How are you, GEORGE?'))   # doesnt return the UPPER CASE E and O from GEORGE
vowelRegex = re.compile(r'[aeiou]',re.IGNORECASE)       # shorthand is also re.I for re.IGNORECASE
print(vowelRegex.findall('Hey Hi, How are you, GEORGE?')) 