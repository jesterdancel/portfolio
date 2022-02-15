class Square:
    def __init__(self, s):
        self.sides = s
        self.ans = ("{} by {} by {} by {}".format(self.sides, self.sides, self.sides, self.sides))
    
    
    def __repr__(self):
        return self.ans
    
print(Square(24))
