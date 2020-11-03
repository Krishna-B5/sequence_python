#seq_polygon.py

from session13 import Polygon

class Polysequence:
    def __init__(self, vertices, circumradius):
        self.vertices = vertices
        self.circumradius = circumradius

    def __len__(self):
        return self.vertices

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 4 or s >=self.vertices:
                raise IndexError
            else:
                area_dict =  Polysequence._area_perimeter_ratio(s, self.circumradius)
                max_efficient_area = sorted(area_dict, key= lambda k: area_dict[k], reverse=True)[0]
                check_area =f'area/perimeter ratios\n {area_dict}'
                check_max_area = f'Maximum efficient polygon is of side {max_efficient_area}'
                return check_area, check_max_area

    def __repr__(self):
        return f'maximum area for Polygon of highest vertices are {self.vertices} num and circumradius {self.circumradius}'

    @staticmethod
    def _area_perimeter_ratio(n, circumradius):
        cnt = 3
        efficiency_dict = dict()
        while (cnt <= n):
            obj = Polygon(cnt, circumradius)
            area = obj.area()
            perimeter = obj.perimeter()
            efficiency_dict[cnt] = (round(area/perimeter,6))
            cnt += 1
        return efficiency_dict