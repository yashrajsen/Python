# Woking with files
def main():
    #opening a file for writing
    # f = open("textfile1.txt","w+")
    
    #oepning a file and append the content with new string
    # f = open("textfile1.txt", "a")

    #open the file in read mode
    f = open("textfile1.txt", "r")

    #write some lines
    # for i in range(10):
    #     f.write("This is string "+ str(i) + "\r\n")

    #read the contents of the file
    if f.mode == 'r':
        # contents = f.read()
        # print(contents)
        fl = f.readlines()
        for x in fl:
            print(x)
            
    #Close the file
    # f.close()

if __name__=="__main__":
    main()
