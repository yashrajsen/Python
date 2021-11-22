#  raise Exception('This is my error message')

# create a function to create a box with a symbol and giving width and height

def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width <2) or (height <2):
        raise Exception('the width and height must be at least 2 to draw a box')
    print(symbol*width)

    for i in range(height - 2):
        print(symbol + (' ' * (width -2)) + symbol)
    print(symbol*width)

boxPrint('*',4,13)   # works well and get us a box
# boxPrint('**',8,6)  # doesn't draws a box, hence we need to restrict this input for symbol
# boxPrint('*',8,1)  # doesn't draws a box, hence we need to restrict this input for symbol

# the error message we get is called traceback
# We can log this error message and continue with the program

import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('error_log.txt','a')
    errorFile.write(traceback.format_exc()) # format_exc() function writes the error message 
    errorFile.close()
    print('The traceback info was written in the error_log.txt file.')


# Assertion is a sanity check to check if the program is not doing any thing wrong.
# If assert statment fails, then it can print an error message.

assert False,'This is assert error message'
