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

    def search_expense(self):
        search_term = input("Description or Category: ")
        found = False

        for expense in self.expenses:
            if search_term.lower() in expense.description.lower():
                print(expense)
                found = True

            elif search_term.lower() in expense.category.lower():
                print(expense)
            found = True
        if not found:
            print("Expense not found")

    def show_expenses(self):
        if not self.expenses:
            print("Expense list is empty")
            return
        
        print("Expense list: ")
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense}")

    def total_expenses(self):
        total = 0

        for expense in self.expenses:
            total += expense.amount

        print(f"Total expense: {total}")

    def expenses_by_category(self):
        categories = {}

        for expense in self.expenses:
            if expense.category not in categories:
                categories[expense.category] = 0

            categories[expense.category] += expense.amount

            for category, total in categories.item():
                print(f"{category}: {total}")
                