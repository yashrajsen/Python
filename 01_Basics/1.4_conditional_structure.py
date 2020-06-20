##Working with Conditional Structures

def main():
    x, y = 101, 100

    # conditional flows uses if, elif and else
    if (x < y):
        st = "x is less than y"
    elif (x == y):
        st = "x is same as y"
    else:
        st="x is greater than y"
    print(st)

    #conditional statements lets you use "a if C else b"
    st = "x is less than y" if(x<y) else "x is greater than y or same as y"
    print(st)

if __name__=="__main__": # this statement is requried for Main function
    main()
    # print(main()) # this execution does not happen

#prints "x is less than y" for x=10, y=100
#prints "x is greater than y" for x=210, y=100
#prints "x is greater than y" for x=100, y=100 when elif is not present
#prints "x is same as y" for x=100, y=100 with elif statement