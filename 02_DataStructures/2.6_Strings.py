# print('This is Alice's cat) #throws error for incorrect syntax
print('This is Alice\'s cat')   # the escape charcter '\' is used to print single quotes
# other syntaxes are
# \" - Double quotes
# \t - Tab
# \n - newline or line break
# \\ - Backlash
print('Hi there! \nHow are  you?')

# Another way is to use raw string that starts from r'
print(r'This is Carol\'s cat.')

# multilline string can be printed using """
print("""Dear Alice,
HOw are you?
Your's Lovingly
John
""")

#Stings can be treated as lists 
spam = "Hello world"
print(spam[0])
print(spam[1:5])
print(spam[-1])
print('W' in spam)

# Stings objects are not mutable
spam.upper()
print(spam) # still results as "Hello World"
spam = spam.upper()
print(spam)
# but we can temporarily change the string with out saving the updated values
print(spam.lower())
print(spam.title()) #prints the Title case as "Hello World"

# can use for prompting inputs from user
answer = input("Provide a String: ")
print(answer)

# check if string is lower or upper case
msg = 'Hello'
print(msg.islower())    #returns false as one letter is in Upper case
print(msg.isupper())
msg = 'hello'
print(msg.islower())
print(msg.istitle())

# datatype methods
print('hello'.isalpha())  #returns true
print('hello123'.isalpha())  #returns false
print('123'.isdecimal())  #returns true
print('  '.isspace())  #returns true
print('Hello World'.isspace())  #returns false

#Sub strings.
print('Hello world!'.startswith('Hello'))    #returns True
print('Hello world!'.startswith('H'))    #returns True
print('Hello world!'.endswith('world'))    #returns False
print('Hello world!'.endswith('world!'))    #returns True

#join method for concatenating the strings with character
print(','.join(['cats','rats','bats']))
print(' '.join(['cats','rats','bats']))
print('\n\n'.join(['cats','rats','bats']))  #prints new line in between the list items

#split method converts a string to a list
print('My name is Anil'.split())
print('My name is Anil'.split('n')) # splits based on certain character

#rjust and ljust methods fill spaces for a string
print('hello'.rjust(10))
print('hello'.ljust(10,'*'))

print('Hello'.center(20))
print('Hello'.center(20,'='))

#strip method removes white spaces
print('    hello    '.strip())
print('    hello    '.lstrip())
print('    hello    '.rstrip())
print('****hello***'.strip('*'))
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'))        # does not remove the Spam present in BaconSpamEggs

#replace method
print('Hello there.'.replace('e','X'))

#Pyperclip module
# install through commandline using pip
# Goto Python folder -> pip.exe install pyperclip
# import pyperclip
# pyperclip.copy('Hello!!!!!!!')
# print(pyperclip.paste())

##String Formatting
name= 'Aadvik'
place = '1st Street'
time = '6 PM'
food = 'parathas'
print( 'Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place,time,food))