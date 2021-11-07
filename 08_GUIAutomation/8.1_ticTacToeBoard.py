import pprint

theBoard = {'top-L':'','top-M':'O','top-R':'','mid-L':'','mid-M':'X','mid-R':'','low-L':'','low-M':'','low-R':''}
pprint.pprint(theBoard)

# print the values in a tic tac toe board format

def printBoard(board):
    print(board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
    print('-------' )
    print(board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'] )
    print('-------' )
    print(board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'] )
    print('-------' )

printBoard(theBoard)