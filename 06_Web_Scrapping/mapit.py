import webbrowser,sys #, pyperclip

# Copy address and check it in maps
sys.argv # ['mapit.py', '870','Valanca', 'St.']

#check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])  #slice the arguments to take from index 1 and so on till end.
else:
    # address = pyperclip.paste()
    address = input('Please add an address:')

webbrowser.open('https://www.google.com/maps/place/' + address)