from models import Expense
from storage import JsonStorage
from report import (
    filter_by_period,
    report_by_category,
    total_sum,
    export_to_csv
)

db = JsonStorage("expenses.json")

def cmd_add(desc, amount, category):
    expense = Expense(desc=desc, amount=float(amount), category=category)
    db.add_expense(expense)
    print(f"Добавлен расход: {desc} ({amount}₽, {category})")

def cmd_view(period=None):
    expenses = db.get_all_as_list()
    expenses = filter_by_period(expenses, period) if period else expenses

    if not expenses:
        print("Нет расходов за выбранный период.")
        return

    print("Список расходов:")
    for e in expenses:
        print(f"{e.date} — {e.category}: {e.desc} ({e.amount}₽)")

def cmd_report(period=None, export=False):
    expenses = db.get_all_as_list()
    expenses = filter_by_period(expenses, period) if period else expenses
    totals = report_by_category(expenses)

    if not totals:
        print("Нет данных для отчёта.")
        return

    print("Отчёт по категориям:")
    for cat, total in totals.items():
        print(f"{cat}: {total}₽")

    if export:
        export_to_csv(expenses)

def cmd_sum(period=None):
    expenses = db.get_all_as_list()
    expenses = filter_by_period(expenses, period) if period else expenses
    total = total_sum(expenses)
    print(f"Общая сумма расходов{f' за {period}' if period else ''}: {total}₽")
