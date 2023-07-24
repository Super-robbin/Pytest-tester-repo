class StringBuilder():
    def __init__(self):
        self.str = ""

    def add(self, string):
        self.str += string

    def size(self):
        return len(self.str)
    
    def output(self):
        return self.str
    
