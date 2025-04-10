# Expense Tracker

This is a simple Python-based expense tracker with a graphical user interface (GUI) built using Tkinter. It helps users to track their expenses, set budgets for different categories, and view reports on spending and budgeting.

## Features

- **Add Expenses**: Record expenses with details such as amount, description, date, and category.
- **Set Budgets**: Set and update budgets for categories like Food, Transport, and Entertainment.
- **View Reports**: Generate spending reports for a specific month, compare the expenses against the budget, and get notifications if the budget is exceeded.
- **Customizable Categories**: Add new categories to the tracker with a default budget.

---

## Installation

To run this project on your local machine, follow the steps below:

### Prerequisites

- Python 3.x
- Tkinter (usually comes with Python by default)

### Steps

1. **Clone the repository**:
   
   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   ```

2. **Install any required dependencies**:

   This project only requires the standard Python library, so no additional installation of external libraries is necessary. However, make sure you have Python 3.x installed, and Tkinter is available (it usually comes bundled with Python).

   You can verify that Tkinter is installed by running:

   ```bash
   python -m tkinter
   ```

   If a window opens, Tkinter is correctly installed.

---

## Usage

1. **Run the Expense Tracker application**:

   Navigate to the project directory and run the script:

   ```bash
   python expense_tracker.py
   ```

   The Tkinter window will open, where you can interact with the application.

---

## Features Walkthrough

### 1. Adding Expenses

To add an expense, click on the "Add Expense" button:

- **Amount**: Enter the amount of the expense.
- **Description**: Add a short description of the expense.
- **Date**: Enter the date of the expense in the format `YYYY-MM-DD`.
- **Category**: Select the appropriate category for the expense (e.g., Food, Transport, Entertainment).

After entering the details, click "Submit" to add the expense. If the category's budget is exceeded, a warning message will pop up.

### 2. Setting a Budget for Categories

Click the "Set Budget" button to set a budget for a category:

- Enter the category name (e.g., Food, Transport, or Entertainment).
- Enter the budget amount you wish to set for that category.

The budget for that category will be updated, and the expense tracker will notify you if the expenses exceed the set budget.

### 3. Viewing Reports

Click the "Show Reports" button to view monthly reports:

- Enter the month and year for which you want to view the total spending.
- The application will display the total amount spent in the given month and a summary of spending vs. budget for each category.

---

## Modifying the Budget

To change the budget for an existing category, follow these steps:

1. Click the **"Set Budget"** button.
2. In the dialog box that appears, enter the **category** you want to modify (e.g., Food).
3. Enter the **new budget amount** for that category.
4. The budget will be updated and displayed on the main screen.

---

## Reports

Reports show the total spending in a given month, and the status of each category compared to its budget.

To view reports:

1. Click the **"Show Reports"** button.
2. Enter the **month (1-12)** and **year** (e.g., 2025).
3. The app will display:
   - The **total spending** for that month.
   - A comparison of the **budget vs. spending** for each category (Food, Transport, Entertainment, etc.).

---

## Customizing Categories

To add a new category:

1. Click the **"Set Budget"** button.
2. Enter a new **category name** (e.g., "Shopping").
3. The new category will be added with a default budget of **$0.00**.
4. You can then set a budget for the new category by following the steps above.

---

## Contact

For any issues or suggestions, feel free to contact [harshitha2252004@gmail.com].

---
