import argparse
from commands import cmd_add, cmd_view, cmd_report, cmd_sum

parser = argparse.ArgumentParser(description="CLI-трекер расходов")

parser.add_argument("--add", nargs=3, metavar=("DESC", "AMOUNT", "CATEGORY"), help="Добавить расход")
parser.add_argument("--view", nargs="?", choices=["day", "month"], help="Просмотр расходов за день/месяц")
parser.add_argument("--report", nargs="?", choices=["day", "month"], help="Отчёт по категориям")
parser.add_argument("--sum", nargs="?", choices=["day", "month"], help="Сумма расходов")
parser.add_argument("--export", action="store_true", help="Выгрузить отчёт в CSV")

args = parser.parse_args()

if args.add:
    desc, amount, cat = args.add
    cmd_add(desc, amount, cat)
elif args.view:
    cmd_view(args.view)
elif args.report:
    cmd_report(args.report, export=args.export)
elif args.sum:
    cmd_sum(args.sum)
else:
    parser.print_help()
