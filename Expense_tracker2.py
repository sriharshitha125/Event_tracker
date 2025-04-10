import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = {'Food', 'Transport', 'Entertainment'}
        self.budgets = {category: 0.0 for category in self.categories}

    def add_expense(self, amount, description, date, category):
        if category not in self.categories:
            messagebox.showerror("Error", f"Category '{category}' does not exist.")
            return

        expense = {
            'Amount': amount,
            'Description': description,
            'Date': date,
            'Category': category
        }

        self.expenses.append(expense)
        if self.check_budget_exceeded(category):
            messagebox.showwarning("Budget Exceeded", f"You've exceeded your budget for '{category}'!")
        else:
            messagebox.showinfo("Success", "Expense added successfully.")

    def add_category(self, category):
        if category not in self.categories:
            self.categories.add(category)
            self.budgets[category] = 0.0
            messagebox.showinfo("Success", f"Category '{category}' added with default budget $0.00.")
        else:
            messagebox.showinfo("Info", f"Category '{category}' already exists.")

    def set_budget(self, category, amount):
        if category in self.categories:
            self.budgets[category] = amount
        else:
            messagebox.showerror("Error", "Category not found.")

    def check_budget_exceeded(self, category):
        total_spent = sum(exp['Amount'] for exp in self.expenses if exp['Category'] == category)
        return total_spent > self.budgets.get(category, float('inf'))

    def get_spending_summary(self):
        summary = {}
        for category in self.categories:
            spent = sum(exp['Amount'] for exp in self.expenses if exp['Category'] == category)
            budget = self.budgets.get(category, 0.0)
            summary[category] = {"spent": spent, "budget": budget}
        return summary

    def get_total_spending_for_month(self, month, year):
        total_spent = 0.0
        for expense in self.expenses:
            expense_date = datetime.strptime(expense['Date'], "%Y-%m-%d")
            if expense_date.month == month and expense_date.year == year:
                total_spent += expense['Amount']
        return total_spent

# GUI
def show_main_window(tracker):
    def refresh_budget_display():
        for widget in budget_frame.winfo_children():
            widget.destroy()

        for category in tracker.categories:
            summary = tracker.get_spending_summary()
            spent = summary[category]["spent"]
            budget = summary[category]["budget"]
            status = "✅" if spent <= budget else "❌"
            label = tk.Label(budget_frame, text=f"{category}: Spent ${spent:.2f} / Budget ${budget:.2f} {status}",
                             anchor="w", width=50)
            label.pack(anchor="w")

    def refresh_expense_table():
        for widget in expense_table_frame.winfo_children():
            widget.destroy()

        # Adding table headers
        headers = ["Amount", "Description", "Date", "Category"]
        for header in headers:
            header_label = tk.Label(expense_table_frame, text=header, font=("Helvetica", 10, "bold"), width=20)
            header_label.grid(row=0, column=headers.index(header), padx=10, pady=5)

        # Adding expense rows
        for i, expense in enumerate(tracker.expenses):
            tk.Label(expense_table_frame, text=f"${expense['Amount']:.2f}", width=20).grid(row=i+1, column=0, padx=10, pady=5)
            tk.Label(expense_table_frame, text=expense['Description'], width=20).grid(row=i+1, column=1, padx=10, pady=5)
            tk.Label(expense_table_frame, text=expense['Date'], width=20).grid(row=i+1, column=2, padx=10, pady=5)
            tk.Label(expense_table_frame, text=expense['Category'], width=20).grid(row=i+1, column=3, padx=10, pady=5)

    def set_category_budget():
        cat = simpledialog.askstring("Set Budget", "Enter category:")
        if not cat:
            return
        try:
            amount = float(simpledialog.askstring("Set Budget", f"Enter budget amount for '{cat}':"))
            tracker.add_category(cat)
            tracker.set_budget(cat, amount)
            refresh_budget_display()
        except:
            messagebox.showerror("Error", "Invalid amount entered.")

    def add_expense_gui():
        try:
            amount = float(simpledialog.askstring("Add Expense", "Enter amount:"))
            description = simpledialog.askstring("Add Expense", "Enter description:")
            date = simpledialog.askstring("Add Expense", "Enter date (YYYY-MM-DD):")
            category = simpledialog.askstring("Add Expense", "Enter category:")
            tracker.add_expense(amount, description, date, category)
            refresh_budget_display()
            refresh_expense_table()
        except:
            messagebox.showerror("Error", "Invalid input for expense.")

    def show_reports():
        month = simpledialog.askinteger("Month", "Enter month (1-12):")
        year = simpledialog.askinteger("Year", "Enter year (e.g., 2025):")

        if not month or not year:
            messagebox.showerror("Error", "Invalid input for month or year.")
            return

        total_spent = tracker.get_total_spending_for_month(month, year)
        messagebox.showinfo("Monthly Total Spending", f"Total spending for {month}/{year}: ${total_spent:.2f}")

        summary = tracker.get_spending_summary()
        report_text = "Spending vs Budget per Category:\n"
        for category, data in summary.items():
            spent = data["spent"]
            budget = data["budget"]
            status = "✅" if spent <= budget else "❌"
            report_text += f"{category}: Spent ${spent:.2f} / Budget ${budget:.2f} {status}\n"

        messagebox.showinfo("Category Comparison", report_text)

    window = tk.Tk()
    window.title("Expense Tracker")
    window.geometry("600x500")

    tk.Label(window, text="Expense Tracker", font=("Helvetica", 16, "bold")).pack(pady=10)

    budget_frame = tk.Frame(window)
    budget_frame.pack(pady=10)

    expense_table_frame = tk.Frame(window)
    expense_table_frame.pack(pady=10)

    refresh_budget_display()
    refresh_expense_table()

    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Set Budget", width=15, command=set_category_budget).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Add Expense", width=15, command=add_expense_gui).grid(row=0, column=1, padx=10)
    tk.Button(button_frame, text="Show Reports", width=15, command=show_reports).grid(row=0, column=2, padx=10)

    window.mainloop()

if __name__ == "__main__":
    tracker = ExpenseTracker()

    # Pre-set sample budgets (optional)
    tracker.set_budget("Food", 300)
    tracker.set_budget("Transport", 150)
    tracker.set_budget("Entertainment", 100)

    show_main_window(tracker)