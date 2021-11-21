##Plaintext and binary files
#binary files are .doc, .pdf, images, spreadsheet, .exe, etc 

#Open method is for the read mode by default

helloFile = open('C:\\Users\\yashrajsen\\Desktop\\hello.txt')
print(helloFile.read())
helloFile.close()       #we need to close a file after it is open and read / write actions are performed

#readlines method will read all lines and stores them in a list
helloFile = open('C:\\Users\\yashrajsen\\Desktop\\hello.txt')
print(helloFile.readlines())

helloFile = open('C:\\Users\\yashrajsen\\Desktop\\hello.txt','w')
helloFile.write('I am good. How about You?\n')
helloFile.close()

baconFile =open('bacon.txt','w')
baconFile.write('Bacon is not a vegetable')
baconFile.close()


baconFile =open('bacon.txt','a')        #append mode
baconFile.write('\n \nBacon is not delicious')
baconFile.close()

## SHELVE MODULE

import shelve
shelfFile = shelve.open('myShelf')
shelfFile['cats'] = ['Zohpie','Pooka','Simon','Fat-tail','Cleo']
print(shelfFile['cats'])
print(shelfFile.keys())
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()