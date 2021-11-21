#! python3

import re, pyperclip

# TO DO: Create a regex for phone numbers
phoneRegex = re.compile(r'''

# Examples of phone numbers: 415-343-2020, 333-4920 ,(234) 324-2983, 444-2384 ext 23919 , ext. 12343, x23910
(((\d\d\d)|(\(\d\d\d\)))?            # area code (optional) eiyher or the pattern
(\s|-)                              # first separator
(\d\d\d)                              # first 3 digits
-                                   # separator
(\d\d\d\d)                            # last 4 digits
(((ext(\.)?\s)|x)                   # extension word part (optional)
(\d{2,5}))?)                      # extension number part (optional)
''', re.VERBOSE)

# TO DO : Create a regex ofr email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+           #name part
@                         #symbol
[a-zA-Z0-9_.+]+           #domain part
''', re.VERBOSE)

#TO DO : Get the text off the clipboard
text = pyperclip.paste()

#To DO : Extract the email / phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)
# To DO : copy the extracted email /Phone to the clipboard
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
# print('Phone numbers and Email IDs: ' , results)
pyperclip.copy(results)