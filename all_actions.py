all_pur = []

class Purchase:
    def __init__(self, category, name, date, price, quantity=1):
        self.category = category
        self.name     = name
        self.date     = date
        self.price    = price
        self.quantity = quantity
    def __str__(self):
        """
        Returns a string representation of the Expense object.
        """
        return (f"Expense(Category: {self.category}, Name: {self.name}, "
                f"Date: {self.date}, price: ${self.price:.2f}, Quantity: {self.quantity})")

    def to_dict(self):
        """
        Converts the Expense object to a dictionary.
        """
        return {
            "category": self.category,
            "name": self.name,
            "date": self.date,
            "price": self.price,
            "quantity": self.quantity
        }

def op_purchase():
    category = input ("Category(food, dress, transportion): ")
    name     = input ("Name: ")
    date     = input ("Date(1, 1, 2025): ")
    price    = input ("Price: ")
    quantity = input ("Quantity(Optional): ")
    pur1 = Purchase(category, name, date, price, quantity=quantity if quantity else 1)
    all_pur.append(pur1)


            
