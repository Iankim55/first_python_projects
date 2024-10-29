from curses.textpad import rectangle


class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    @width.setter
    def width (self,new_width):
        if new_width >0:
            self._width=new_width
    @height.setter
    def height(self,new_heights):
        if new_heights>0:
            self._height=new_heights
        else:
            print("Height must be greater than zero")

    rectangele=Rectangle(3,4)
    print(rectangle._width)
    print(rectangle._height)