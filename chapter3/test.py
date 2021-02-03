class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
    def _width_get(self):
        return self.x2 - self.x1
    def _width_set(self, value):
        self.x2 = self.x1 + value
    def _height_get(self):
        return self.y2 - self.y1
    def _height_set(self, value):
        self.y2 = self.y1 + value
    
    width = property(
        _width_get, _width_set,
        doc = "左辺から測定した矩形の幅"
    )
    height = property(
        _height_get, _height_set,
        doc = "上辺から測定した矩形の高さ"
    )
    def __repr__(self):
        return "{}({}, {}, {}, {})".format(self.__class__.__name__, self.x1, self.y1, self.x2, self.y2)


rectangle = Rectangle(10, 10, 25, 34)
print(rectangle.width, rectangle.height)
rectangle.width = 100
print(rectangle)
rectangle.height = 100
print(rectangle)
print(help(Rectangle))