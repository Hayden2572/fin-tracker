from dataclasses import dataclass
from datetime import datetime

@dataclass
class Category:
    name: str

@dataclass
class Expense:
    desc: str
    amount: float
    category: str
    date: str = datetime.now().strftime("%Y-%m-%d")
