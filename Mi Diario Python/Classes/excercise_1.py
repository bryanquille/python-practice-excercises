class Entero_Romano:

    i = 0
    numeral = ''
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerales = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    def __init__(self, entero: int):
        self.entero = entero
        while self.entero > 0:
            for _ in range(self.entero//self.numeros[self.i]):
                self.numeral += self.numerales[self.i]
                self.entero -= self.numeros[self.i]
            
            self.i += 1
        print(self.numeral)
        # return self.numeral
        
rom = Entero_Romano(1235)