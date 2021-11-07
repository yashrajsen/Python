# Dictionary is an object that has a key value pair

myCat = {'size': 'fat','color': 'gray', 'disposition':'loud'}
print(myCat['size'])

# items in Dictionary are unordered 
#print(myCat[1])     # throws error
print([1,2,3]== [3,2,1])    # List is ordered, hence returns False
print({1,2,3}== {3,2,1})    # List is unordered, hence returns True

#both the key ansd values have to be same but unordered
person = {'name': 'Anil', 'age': 33,'city':'Bangalore'}
employee = {'city': 'Bangalore','name':'Anil','age':33}
print(person==employee)

print('name' in person) # can check the key in a dictionary
print('Anil' in person) # cannot check the keyvalue in a dictionary

# Methods to get the keys and values from the dictionary
print(list(person.keys()))
print(list(person.values()))
print(list(person.items()))

# use the for loop
for k in employee.keys():
     print(k)
for v in employee.values():
    print(v)

for k,v in employee.items():
    print(k,v)      # returns as city Bangalore

for i in employee.items():
    print(i)        #returns the items as tuples like ('name','Anil')

# get method extracts the key value and returns a default value there is no key found
print(person.get('mobile'),'9876543210')

#setDefault method
if 'mobile' not in person:
    person.setdefault('mobile','9998887776')
print(person)

##character counting program
# to use a huge string we can use 
message = ''' Twinkle, twinkle, little star,
How I wonder what you are,
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is set,
And the grass with dew is wet,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
He could not see where to go
If you did not twinkle so.

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.
'''
#get each character as key in dictionary with their count as the value
count ={}
for character in message.upper():       # to count a character in any case
    count.setdefault(character ,0)
    count[character] = count[character] + 1

print(count)

## to display the dictionary or list items in a cleaner way. we can import pprint module

import pprint   ##pretty print

pprint.pprint(count)

# pformat method returns the dictionary items in a string format

text = pprint.pformat(count)
print(text)