##Working with Functions

# define basic function
def func1():
    print("I am a function")

# functions that take arguments
def func2(args1, args2):
    print(args1, " ", args2)

#function that returns a value
def cube(x):
    return x*x*x

#function that takes a default value for the arguments
def power(num,x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result + 2;
    
#
# function with variable number of arguments
def multi_add(*args):
    result = 0
    for j in args:
        result = result + j
    return result

## Executions##

# func1() # Output: I am a function
# print(func1()) # output: Prints "I am a function" and returns a "None" (for no return statement in the function)
# print(func1)    #output: <function func1 at 0x042479C0>

# func2(10,30)    # prints "10  30"
# print(func2(10,40)) #prints "10  40" and "None" (for no return statement in the function)
# print(cube(4)) #prints "64" 

power(4)    #prints nothing
print(power(4)) #prints 4
power(2,3) #prints nothing
print(power(2,3)) #prints 8
print(power(x= 6, num=3 ))

print(multi_add(12,34,56,6)) # prints 108
print(multi_add()) # prints 0