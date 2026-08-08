class Expense:
    def __init__(self, description, amount, category, date):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return(
            f"Description: {self.description} | "
            f"Amount: {self.amount} | "
            f"Category: {self.category} | "
            f"Date: {self.date}"
        )

class ExpenseManager:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        try:
            index = int(index) -1
        except ValueError:
            print("invalid index! enter number...")
            return
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"{removed.description} deleted")
            return
        else:
            print("Expense not found")
            

    