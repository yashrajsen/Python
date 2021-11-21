def isPhoneNumber(text):
    if len(text) != 12:
         return False   #Not a phone number sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False    #No area code
    if text[3] != '-':
        return False    # missing dash

    for i in range(4,7):
        if not text[i].isdecimal():
            return False    #No first 3 digits
    if text[7] !='-':
        return False    # Missing dash
    
    for i in range(8,12):
        if not text[i].isdecimal():
            return False    #Missing last 4 digits
    return True

print(isPhoneNumber('469-332-1105'))
print(isPhoneNumber('469-33a-1105'))
print(isPhoneNumber('46-9332-1105'))

message = 'Call me at 541-324-4379 tomorrow , or at 23-232-4354 in the weekend.'
foundNumber = False;
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone Number Found: '+ chunk)
        foundNumber = True;
if not foundNumber:
    print('Could Not find any Number')



## Using the Regular Expression

import re       ## re for RegEx Module

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')     ## r is for raw string. \d is for digits
mo = phoneNumRegex.search('Call me at 541-324-4379 tomorrow , or at 823-232-4354 in the weekend.')
print(mo.group())   ## results the first occurance
print(mo)
#findall methods gets all the occurences of the phone numbers in a list
print(phoneNumRegex.findall('Call me at 541-324-4379 tomorrow , or at 823-232-4354 in the weekend.'))
