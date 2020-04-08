def gcd(m,n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

class Fraction:

    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self, otherFraction):
        newnum = self.num * otherFraction.den + otherFraction.num * self.den
        newden = self.den * otherFraction.den
        common = gcd(newnum, newden)
        return(newnum//common, newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum

    def __sub__(self, other):
        newnum = self.num * otherFraction.den - otherFraction.num * self.den
        newden = self.den * otherFraction.den
        common = gcd(newnum, newden)
        return (newnum // common, newden // common)



x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x ==y )
