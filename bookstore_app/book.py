class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = round(float(price), 2)
        self.stock = int(stock)

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "stock": self.stock
        }
    
    def update_stock(self, amount):
        self.stock += amount
