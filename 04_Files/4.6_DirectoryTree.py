import os ,shutil
for folderName, subFolders, filenames in os.walk('C:\\Users\\Yashrajsen\\OneDrive\\Documents'):
    print('The folder is : ' + folderName)
    print('The sub Folders in '+ folderName +' are: ' + str(subFolders))
    print('The file names in '+ folderName +' are: ' + str(filenames))
    print()

    for subfolder in subFolders:
        if 'fish' in subFolders:
            os.rmdir(subfolder)
    
    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(folderName, file), os.join(folderName ,file + '.backup'))