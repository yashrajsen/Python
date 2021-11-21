# Shulit module allows to copy move file or folders
import shutil
# shutil.copy('bacon.txt','folder\\baconCopy.txt')  # cannot create the folder by itself
# shutil.copytree('folder','folder-backup')   # copies folder and all of ites contents
# shutil.move('bacon.txt','folder')
# rename the file by using move method
shutil.move('folder\\baconCopy.txt','folder\\eggs.txt')