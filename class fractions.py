class simple_fraction(object) : 
    """ a fraction of numerator n and denominator d where n and d are integers"""

    def __init__ (self, n, d) : 
        if type(n) != int or type(d) != int : 
            raise ValueError
        self.num = n
        self.denom = d

    def times(self, other) : 
        """ multiply two fraction objects """
        top = self.num * other.num
        bottom = self.denom * other.denom
        return top / bottom
    
    def plus(self, other) : 
        """ add two fraction objects """
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return top / bottom

    def get_inverse(self) : 
        """ returns a float representing 1/self"""
        return self.denom / self.num

    def invert(self) : 
        """ sets self's num to its denom and vice versa 
        returns None"""
        self.num, self.denom = self.denom, self.num 
        

f1 = simple_fraction(3,4) 
f2 = simple_fraction(1,4)

print(f1.num) # 3
print(f1.denom) # 4
print(f1.plus(f2)) # 1.0
print(f1.times(f2)) # 1/16 so 0.1875 
print(f1.get_inverse()) # 4/3 so 1.33333333
print(f1.invert()) # calls to invert f1, f1 becomes 4/3, returns none
print(f1.num, f1.denom) # 4 3 after the invert call 