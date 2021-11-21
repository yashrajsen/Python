import os, shutil

# os.unlink('folder\\bacon.txt')

# os.rmdir('C:\\Delicious')   # can delete the directory and for rmdir can only delete empty directory

#to delete a folder and its entire contents
# shutil.rmtree('DeleteFolder')

#program to delete folder contents
os.chdir('C:\\Windows\\Temp')
for filename in os.listdir():
    if filename.endswith('.log'):
        print(filename)
        os.unlink(filename)
        
