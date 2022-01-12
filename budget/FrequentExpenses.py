
import collections
from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses(data/spending_data.csv)

spendingCategories = []

for Expense in expenses:
    spendingCategories.append(expenses.category)

spendingCounter = collections.Counter(spendingCategories)

print(spendingCategories)
print(spendingCounter)