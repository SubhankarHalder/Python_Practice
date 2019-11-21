class StringOperations:
    def __init__(self):
        self.x = ""
    def getString(self):
        self.x = input("Input String:")

    def printString(self):
        print(self.x.upper())


p1 = StringOperations()
p1.getString()
p1.printString()
