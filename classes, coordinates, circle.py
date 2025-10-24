class Coordinates(object) : 
    """coordinates of a point in a 2D grid"""

    def __init__ (self, xval, yval) : 
        """initializes the coordinates of the point"""
        self.x = xval
        self.y = yval

    def distance(self, other) : 
        """ returns the euclidian distance between two coordinates objects"""
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    
    def to_origin(self) :
        """ resets the coordinates to 0,0 """
        self.x = 0 
        self.y = 0 

A = Coordinates(3,4)
origin = Coordinates(0,0)
print(A.distance(origin))

class Circle(object) : 
    """ a circle characterized by the coordinates of his center, and his integer radius """

    def __init__ (self, center, radius): 
        if type(center) != Coordinates or type(radius) != int :
            raise ValueError
        self.center = center
        self.radius = radius 
    
    def is_inside(self, point) : 
        """ returns True if point is in self, False otherwise"""
        return self.center.distance(point) < self.radius # effectue la méthode distance entre le centre et le point pour vérifier si le point est a l'interieur
    def is_inside2(self, point) : 
        """ fonctionnellement équivalent """
        return point.distance(self.center) < self.radius
    
moncentre = Coordinates(2,2)
# moncercleraté = Circle(2,2) # RAISE A VALUE ERROR car le centre choisi n'est pas de type Coordinates
moncercle = Circle(moncentre, 2)

point_en_dehors = Coordinates(1000,2000)
point_dans_moncercle = Coordinates(2,3)
print(moncercle.is_inside(point_en_dehors))
print(moncercle.is_inside(point_dans_moncercle))