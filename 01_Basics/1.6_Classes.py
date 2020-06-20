## Working with Classes

class classA():
    def methodA1(self):
        print("Class A Method 1")

    def methodA2(self, someString):
        print("Class A Method 2 " + someString)

class classB(classA):
    def newMethodB1(self):
        classA.methodA1(self)
        print("Class B Method 1")

    def newMethodB2(self,someString):
        print("Class B Method 2")

def main():
    c1 = classA()
    c2 = classB()

    c1.methodA1()
    c1.methodA2("This has String arguments")

    c2.newMethodB1()
    c2.newMethodB2("This String doesn't show up")

if __name__ == "__main__":
    main()
