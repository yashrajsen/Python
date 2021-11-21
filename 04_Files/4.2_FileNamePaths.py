#Filename and Paths
print('C:\\Users\\yashr')
# print('C:\Users\yashr')       throws error as python cannot decode \
print(r'C:\Users\yashr')    # does not throw error with raw string.

print('\\'.join(['folder1','folder2','folder3','file.png']))

## OS module
import os
print(os.path.join('folder1','folder 2','folder3','file.png'))      # displays the separator based on the OS on which the program is running.
print(os.sep)   # returns \ for windows and / for linux and mac
print(os.getcwd())  # returns current working directory


## Absolute and Relative File Paths
# single dot represents current folder
# double dot represents parents folder 

os.chdir('C:\\Users\\yashrajsen\\Desktop')
print(os.path.abspath('Grid Card.png'))
print(os.path.isabs('..\\..\\Grid Card.png'))
print(os.path.isabs('C:\\Users\\yashrajsen'))
print(os.path.relpath('C:\\Users\\yashrajsen\\Desktop\\Grid Card.png','C:\\Users'))

## dirname and basename
print(os.path.dirname('C\\Users\\yashrajsen\\Desktop\\Grid Card.png'))  # returns the directory path name for the file
print(os.path.basename('C\\Users\\yashrajsen\\Desktop\\Grid Card.png'))     # returns the file name for the file or folder
print(os.path.basename('C\\Users\\yashrajsen\\Desktop'))

# exists() method
print(os.path.exists('C:\\Users\\yashrajsen\\Desktop\\Grid Card.png'))
print(os.path.exists('C:\\Users\\yashrajsen\\Desktop\\GridCard.png'))

#isfile and isdir methods
print(os.path.isfile('C:\\Users\\yashrajsen\\Desktop\\GridCard.png'))
print(os.path.isfile('C:\\Users\\yashrajsen\\Desktop'))
print(os.path.isdir('C:\\Users\\yashrajsen'))

print(os.path.getsize('C:\\Users\\yashrajsen\\Desktop'))
print(os.listdir('C:\\Users\\yashrajsen'))

totalSize = 0
for filename in os.listdir('C:\\Program Files'):
    if not os.path.isfile(os.path.join('C:\\Program Files',filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Program Files',filename))
print(totalSize)

# makedirs method

os.makedirs('C:\\Users\\Yashrajsen\\Desktop')
