class Rectangle:
    def __init__(self, h, w):
        self._h = h
        self._w = w
    
    def __str__(self):
        return f"Rectangle with height {self._h} and width {self._w}"

    def __int__(self):
        """
            Takes returns the perimeter of the rectangle
        """
        return 2*(self._h) + 2*(self._w)
    
    def area(self):
        return self._h*self._w


def test(s):
    i = 0
    while not s[i].isdigit():
        i += 1
    return i

if __name__ == "__main__":
    #obj_rect = Rectangle(4,3)
    #print(obj_rect)

    #x = 5
    #print(x + int(obj_rect))

    #print(obj_rect.area())
    print(test("abc2d"))
    print(test("abcd"))
