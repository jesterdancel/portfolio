class Square:
    square_list = []
    def __init__(self, s):
        self.size = s * 4
        self.square_list.append((self.size))
    
square1 = Square(2)
square2 = Square(4)
square3 = Square(3)
print(Square.square_list)
    
class Square:
    square_list = []
    def __init__(self):
        self.square_list.append(self)
