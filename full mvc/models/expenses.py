class Expenses:
    def __init__(self, name, description, amount, id=None):
        self.id = id
        self.name = name
        self.type = type
        self.amount = amount
    
    def to_tuple(self):
        return (self.name, self.description, self.amount)
    
