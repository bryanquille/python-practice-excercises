# A class with two methods

class StringsData:

    def __init__(self, data):
        self.data = data

    def getString(self):
        self.data = str(self.data)
        
    def printString(self):
        print(self.data.upper())


anydata = input('Enter any data: ')
con_str = StringsData(anydata)
con_str.getString()
con_str.printString()
