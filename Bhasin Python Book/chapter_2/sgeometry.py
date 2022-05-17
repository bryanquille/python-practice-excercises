class SGeometry:
    def __init__(self) -> None:
        pass

    def distance_otc(self, x: float, y: float):
        self.x = x
        self.y = y
        self.d = (self.x**2 + self.y**2)**(1/2)
        return f'The distance from origin to ( {self.x} , {self.y} ) coordinates is {round(self.d, 2)}'

    def distance_p1top2(self, x1: float, y1: float, x2: float, y2: float):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2 
        self.d = ((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)**(1/2)
        return f'The distance from P1( {self.x1} , {self.y1} ) to P2( {self.x2} , {self.y2} ) is {round(self.d, 2)}'

    def collinear(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        
        self.d12 = round(((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)**(1/2), 3)
        self.d13 = round(((self.x1 - self.x3)**2 + (self.y1 - self.y3)**2)**(1/2), 3)
        self.d23 = round(((self.x2 - self.x3)**2 + (self.y2 - self.y3)**2)**(1/2), 3)

        if self.d12>self.d13 and self.d12>self.d23:
            if self.d12 == self.d13 + self.d23:
                return f'P1( {self.x1} , {self.y1} ), P2( {self.x2} , {self.y2} ), and P3( {self.x3} , {self.y3} ) are collinear.'
            else:
                return f'P1( {self.x1} , {self.y1} ), P2( {self.x2} , {self.y2} ), and P3( {self.x3} , {self.y3} ) are not collinear.'

        elif self.d13>self.d12 and self.d13>self.d23:
            if self.d13 == self.d12 + self.d23:
                return f'P1( {self.x1} , {self.y1} ), P2( {self.x2} , {self.y2} ), and P3( {self.x3} , {self.y3} ) are collinear.'
            else:
                return f'P1( {self.x1} , {self.y1} ), P2( {self.x2} , {self.y2} ), and P3( {self.x3} , {self.y3} ) are not collinear.'    

        elif self.d23>self.d12 and self.d23>self.d13:
            if self.d23 == self.d13 + self.d12:
                return f'P1( {self.x1} , {self.y1} ), P2( {self.x2} , {self.y2} ), and P3( {self.x3} , {self.y3} ) are collinear.'
            else:
                return f'P1( {self.x1} , {self.y1} ), P2( {self.x2} , {self.y2} ), and P3( {self.x3} , {self.y3} ) are not collinear.'
        

