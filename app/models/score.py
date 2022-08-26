class Score(object):
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
    
    def nm(self):
        return self.name
    
    def ave(self):
        return (self.korean + self.english +self.math) / 3 
          