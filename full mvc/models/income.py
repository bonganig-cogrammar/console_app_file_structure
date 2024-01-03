class Income:
    def __init__(self, name, type, amount, id=None):
        self.id = id
        self.name = name
        self.type = type
        self.amount = amount
    
    def to_tuple(self):
        return (self.name, self.type, self.amount)
    
    
