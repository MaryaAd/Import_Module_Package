from application.db import people as p

from application import salary as s

from datetime import date

from colorama import init, Fore, Back, Style

if __name__ == '__main__':
    init(autoreset=True)
    print(Fore.BLUE + f"Текущаяя дата: {date.today().strftime('%d-%m-%Y')}")

    print(Style.BRIGHT + s.calculate_salary())
    print(Back.WHITE + p.get_employees())


