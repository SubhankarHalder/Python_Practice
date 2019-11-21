class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+'/'+str(self.den)

    def __add__(self, otherfraction):

        newnum = self.num*otherfraction.den+self.den*otherfraction.num
        newden = self.den*otherfraction.den

        return Fraction(newnum, newden)

    def __mul__(self, otherfraction):

        newnum = self.num*otherfraction.num
        newden = self.den*otherfraction.den

        return Fraction(newnum, newden)

print(Fraction(3,5)+Fraction(2,7))
print(Fraction(3,5)*Fraction(2,7))
