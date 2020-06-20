##Working with Variables

# #Declare a variable and initialize it
f=0
print(f)

# redeclaring a variable and initialize it
f="anil"
print(f)

#Error: Variable of different types cannot be combined
#print("this is a string" + 124)
print("this is a string" + str(124))

#Global vs Local variables
def someFunction():
    #re-define f variable as global
    global f
    f="def"
    print(f)

someFunction()
print(f)

#Delete the variable at runtime
del f
print(f)
