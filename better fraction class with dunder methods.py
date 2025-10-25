class better_fraction(object) : 

    def __init__ (self, n, d): 
        if type(n) != int or type(d) != int : 
            raise ValueError
        self.num = n
        self.denom = d

    def __str__ (self) : 
        if self.denom == 1 :
            return str(self.num) # pour une fraction de type n/1 autant retourner n directement
        else : # else facultatif : si on tombe dans le if, on return directement 
            return f"{self.num} / {self.denom}"
    
    def __mul__ (self, other) : 
        """ dunder method so that self * other gives an object of class better_fraction that matches the mathematical formula """
        top = self.num * other.num
        bottom = self.denom * other.denom
        return better_fraction(top,bottom) # calls the __mul__ method now the star operator between two betterfractions also returns a betterfraction 

    def __float__ (self) : 
        return self.num / self.denom
    
    def reduce_fraction(self) : 
        """ reduces the fraction to its simplest form"""
        def gcd(n,d) : 
            """helper function to find the greatest common denominator"""
            while d != 0 : 
                (d,n) = (n%d, d)
            return n  

        if self.denom == 0 : 
            return None 
        elif self.denom == 1 : 
            return better_fraction(self.num,1)
        else : 
            greater_common_denominator = gcd(self.num, self.denom)
            top = int(self.num / greater_common_denominator)
            bottom = int(self.denom / greater_common_denominator)
            return better_fraction (top, bottom)    


f1 = better_fraction(3,4)
f2 = better_fraction(1,4)
f3 = better_fraction(5,1)
print(f1)
print(f2)
print(f3)

print(f1*f2) # calls the __str__ method 
print(f1.__mul__(f2))  # equivalent
print(better_fraction.__mul__(f1,f2)) # equivalent

print(float(f1)) # 0.75

to_be_reduced = f1 * f2 * better_fraction(4,3)
print(to_be_reduced) # 12/48
print(to_be_reduced.reduce_fraction()) # 1/4 incroyable ptn trop interessant

