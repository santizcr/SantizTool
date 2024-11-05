import os
import colorama
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
green = colorama.Fore.LIGHTGREEN_EX
cyan = colorama.Fore.CYAN
print(cyan + "CrazySnos - это премиум инструмент для сноса аккаунтов telegram от @Tbl_HUKT0\nв данном инструменте вы можете сносить аккаунты, сносить сессии, спамить входами в аккаунт\nОТВЕТСТВЕННОСТЬ ЗА ВАШИ ДЕЙСТВИЯ НЕСЕТЕ ИСКЛЮЧИТЕЛЬНО ВЫ")
input(cyan + "[!] Нажмите ENTER для возврата в главное меню\n")

clear_console()
os.system("python main.py")