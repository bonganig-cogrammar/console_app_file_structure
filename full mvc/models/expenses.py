class Expense:
    def __init__(self, name, description, amount, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.amount = amount
    
    def to_tuple(self):
        return (self.name, self.description, self.amount)
    
