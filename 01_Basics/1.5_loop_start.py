##Working with Looping 

def main():
    x = 0

# define a WHILE loop
    # while (x<5):
    #     print(x)
    #     x = x +1

# # define a FOR loop
#     for x in range(5,10):
#         print(x)

# # use a FOR loop over a COLLECTION
#     days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
#     for d in days:
#         print(d)

# # use BREAK and CONTINUE statements
    for x in range(5,15):
        #if(x>8): break  # prints 5,6,7,8 
        if (x%2 == 0): continue # prints 5,7,9,11,13
        print(x)

# use enumerate() to get the index
    # days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    # for i,d in enumerate(days):
    #     print(i, d) #prints the index of the array variable

if __name__ == "__main__":
    main()