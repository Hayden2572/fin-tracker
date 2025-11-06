import json
from pathlib import Path
from models import Expense

class JsonStorage:
    def __init__(self, filename="expenses.json"):
        self.filename = Path(filename)

    def _load(self) -> dict:
        if not self.filename.exists():
            return {}
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Ошибка формата JSON, создаётся новый файл.")
            return {}

    def _save(self, data: dict):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_expense(self, expense: Expense):
        data = self._load()
        cat = expense.category

        if cat not in data:
            data[cat] = []

        data[cat].append({
            "desc": expense.desc,
            "amount": expense.amount,
            "date": expense.date
        })
        self._save(data)

    def get_all(self) -> dict:
        return self._load()

    def get_all_as_list(self) -> list[Expense]:
        data = self._load()
        expenses = []
        for cat, items in data.items():
            for e in items:
                expenses.append(Expense(
                    desc=e["desc"],
                    amount=float(e["amount"]),
                    category=cat,
                    date=e["date"]
                ))
        return expenses
