from datetime import datetime
from collections import defaultdict
import csv

def filter_by_period(expenses, period: str):
    today = datetime.now()
    if period == "day":
        return [e for e in expenses if e.date == today.strftime("%Y-%m-%d")]
    elif period == "month":
        return [e for e in expenses if e.date.startswith(today.strftime("%Y-%m"))]
    return expenses

def report_by_category(expenses):
    totals = defaultdict(float)
    for e in expenses:
        totals[e.category] += e.amount
    return dict(totals)

def total_sum(expenses):
    return sum(e.amount for e in expenses)

def export_to_csv(expenses, filename="report.csv"):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Дата", "Категория", "Описание", "Сумма"])
        for e in expenses:
            writer.writerow([e.date, e.category, e.desc, e.amount])
    print(f"Отчёт сохранён в {filename}")
