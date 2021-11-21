import re       ## re for RegEx Module

#grouping the 1st 23 digits as a group 1 and 2nd 3 digits as group 2 and remaining 4 digits as group 3, add paranthesis in the format
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')     ## r is for raw string. \d is for digits
mo = phoneNumRegex.search('Call me at 541-324-4379 tomorrow , or at 823-232-4354 in the weekend.')
print(mo)
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))

## if the message already has a paranthesis like (408) 332 1043 then
phoneRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
ph = phoneRegex.search('My number is (408) 332-1043. Call Me.')
print(ph.group())

## Pipe character
# when we have same prefix for different words.
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
bt = batRegex.search('Batmobile lost a wheel and Batman got pissed off.')
print(bt.group())
print(batRegex.findall('Batmobile lost a wheel and Batman got pissed off.'))
print(batRegex.search('Batmotorcycle lost a wheel'))
print(bt.group(1))