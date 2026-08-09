class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date.today()

    def __str__(self):
        return(
            f"Description: {self.description} | "
            f"Amount: {self.amount} | "
            f"Category: {self.category} | "
            f"Date: {self.date}"
        )
import csv
from datetime import date
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

        for category, total in categories.items():
            print(f"{category}: {total}")
    
    def save_expenses(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["description", "amount", "category", "date"])

            for expense in self.expenses:
                writer.writerow([
                    expense.description,
                    expense.amount,
                    expense.category,
                    expense.date
                ])

    def load_expenses(self):
        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)

                next(reader, None)

                self.expenses.clear()

                for row in reader:
                    expense = Expense(
                        row[0],
                        float(row[1]),
                        row[2]
                    )
                    self.expenses.append(expense)
        except FileNotFoundError:
            pass

def main():
    manager = ExpenseManager()
    manager.load_expenses()
    while True:
        print("\n***** expense manager *****")
        print("1. Add expense")
        print("2. Remove expense")
        print("3. Search expense")
        print("4. Show all expense")
        print("5. Show total expense")
        print("6. Show expense by category")
        print("7. save & exit")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter description: ")
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Invalid chioce! enter number")
                continue

            category = input("Enter category: ")
            expense = Expense(description, amount, category)
            manager.add_expense(expense)
            print("Expense added successfully")

        elif choice == "2":
            manager.show_expenses()
            number = input("Enter expense number: ")
            manager.remove_expense(number)

        elif choice == "3":
            manager.search_expense()

        elif choice == "4":
            manager.show_expenses()

        elif choice == "5":
            manager.total_expenses()

        elif choice == "6":
            manager.expenses_by_category()

        elif choice == "7":
            manager.save_expenses()
            print("Save expenses")
            print("GOOD BYE!")
            break
        else:
            print("Please enter number")

if __name__ == "__main__":
    main()