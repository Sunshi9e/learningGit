from datetime import datetime

class Transaction:
    def __init__(self, date, category, amount):
        if isinstance(date, str):
            self.date = datetime.strptime(date, "%Y-%m-%d").date()
        else:
            self.date = date
        self.category = category
        self.amount = float(amount)

    def to_dict(self):
        return {
            "date": self.date.strftime("%Y-%m-%d"),
            "category": self.category,
            "amount": self.amount
        }
