class polygon:
    __width=None
    __height=None
    def set_values(self,widht,height):
        self.__width=widht
        self.__height=height
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    
class Rectangle(polygon):
    def area(self):
        return self.get_height()*self.get_width()
rect=Rectangle()
rect.set_values(40,50)
print(rect.area())