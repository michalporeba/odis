class B:
    def __init__(self):
        self.content = {}

class X: 
    def init_x(self):
        self.content['x'] = 10

class Y: 
    def init_y(self):
        self.content['y'] = 20

class T(X, Y, B):
    def __init__(self):
        super().__init__()
        self.init_y()
        self.init_x()
        
        
t = T()
print(dir(t))
