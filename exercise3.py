def same(obj1, obj2):
    return obj1 is obj2
    

class Square:
    def __init__(self):
        pass

shape1 = Square()
shape2 = Square()

print(same(shape1, shape2))