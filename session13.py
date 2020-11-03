import math

class Polygon:
    def __init__(self, n_edges, circumradius):
        self.n_edges = n_edges
        self.circumradius = circumradius

    def area(self): # pylint: disable=E0202
        edge_length = self.edgelength()
        apothem = self.apothem()
        self.area =  1/2*(edge_length*self.n_edges*apothem)
        return round(self.area,2)

    def interior_angle(self): # pylint: disable=E0202
        self.interior_angle = (self.n_edges - 2)*(180/self.n_edges)
        return self.interior_angle

    def edgelength(self):
        self.edge_length = 2*self.circumradius*(math.sin(math.pi/self.n_edges))
        return self.edge_length
    
    def apothem(self): # pylint: disable=E0202
        self.apothem = self.circumradius*(math.cos(math.pi/self.n_edges))
        return self.apothem
    
    def perimeter(self): # pylint: disable=E0202
        self.perimeter = self.edge_length*self.area
        return self.perimeter

    def __eq__(self, other):
        if isinstance(other,Polygon):
            if self.n_edges == other.n_edges and self.circumradius == other.circumradius:
                return True
            else:
                return False
        else:
            raise ValueError('Error!!.. Only Polygon objects')

    def __gt__(self, other):
        if isinstance(other,Polygon):
            if self.n_edges > other.n_edges:
                return True
            else:
                return False
        else:
            raise ValueError('Error!!.. Only Polygon objects')
    
    def __repr__(self):
        return f'Polygon of side {self.n_edges} and circumradius {self.circumradius}'