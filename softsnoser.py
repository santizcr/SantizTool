import requests
import time
from datetime import datetime
import colorama
import os
import socket
from colorama import Fore, Style, init
from pystyle import Colors, Colors, Center, Colorate, Box

green = colorama.Fore.LIGHTGREEN_EX
white = colorama.Fore.WHITE
blue = colorama.Fore.BLUE
red = colorama.Fore.RED

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
device_name = socket.gethostname()
r = requests.get("https://pastebin.com/u3syD3F2")
if str(device_name) in r.text:
    current_time = datetime.now()
    login = input(green + "[?] Введите ваш логин -> ")
    password = input(green + "[?] Введите ваш пароль -> ")
    account = str(login) + str(password) + str(device_name)
    print(green + "\n[!] Ваш логин -> ",login)
    print(green + "[!] Ваш пароль -> ",password)
    print(green + "[!] Ваше устройство -> ",device_name)
    print(green + "[!] Время запуска -> ",current_time)
    r = requests.get("https://pastebin.com/u3syD3F2")
    if str(account) in r.text:
        print(green + "[!] Доступ разрешен")
        time.sleep(1)
        clear_console()
    else:
        print(red + "[!] Доступ запрещен, ваше устройство: " + device_name + " обратитесь к разработчику с просьбой выдать доступ!")
        colorama.Fore.RESET
        exit()

banner=  """

     █████╗ ██████╗  █████╗ ███████╗██╗   ██╗ ██████╗███╗  ██╗ █████╗  ██████╗
    ██╔══██╗██╔══██╗██╔══██╗╚════██║╚██╗ ██╔╝██╔════╝████╗ ██║██╔══██╗██╔════╝
    ██║  ╚═╝██████╔╝███████║  ███╔═╝ ╚████╔╝ ╚█████╗ ██╔██╗██║██║  ██║╚█████╗
    ██║  ██╗██╔══██╗██╔══██║██╔══╝    ╚██╔╝   ╚═══██╗██║╚████║██║  ██║ ╚═══██╗
    ╚█████╔╝██║  ██║██║  ██║███████╗   ██║   ██████╔╝██║ ╚███║╚█████╔╝██████╔╝
     ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝ ╚═╝  ╚══╝ ╚════╝ ╚═════╝

   ┌───────────────────────────────────────────────────────────────────────────────┐
   │               Разработчик: @Fr31zep // ТГК: t.me/crazytoolsoft                │
   └───────────────────────────────────────────────────────────────────────────────┘
   ┌───────────────────────────────────────────────────────────────────────────────┐
   │[1] Снос аккаунта                             [5] Бомбер входами в аккаунт     │
   │[2] Снос сессии                               [6] Сообщить об ошибке           │
   │[3] Снос ТГК                                  [7] Информация                   │
   │[4] Разбан номера                             [8] Выйти                        │
   └───────────────────────────────────────────────────────────────────────────────┘      
"""

clear_console()
print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, banner)))

choice = input(Colorate.Vertical(Colors.white_to_blue, "\n[+] Введите номер опции:  "))

if choice == "1":
    clear_console()
    os.system("python account.py")
elif choice == "2":
    clear_console()
    os.system("python sessions.py")
elif choice == "3":
    clear_console()
    os.system("python snostgk.py")
elif choice == "4":
    clear_console()
    os.system("python unban.py")
elif choice == "5":
    clear_console()
    os.system("python bomber.py")
elif choice == "6":
    clear_console()
    os.system("python report.py")
elif choice == "7":
    clear_console()
    os.system("python info.py")
elif choice == "8":
    clear_console()
    print(green + "[!] Завершаю работу...")
    time.sleep(1)
    print(green + "[!] Работа завершена...")
else:
    clear_console()
    input(green + "[!] Ошибка, вы ввели неверное значение, нажмите ENTER для возврата в главное меню\n")
    os.system("python main.py")