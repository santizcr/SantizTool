import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import random
import colorama
import os
green = colorama.Fore.LIGHTGREEN_EX
cyan = colorama.Fore.CYAN
senders = { #почты и пароли от них, с этих почт отправляються запросы
    "leha.savichev.85@mail.ru": "yYYsxcpWcaiik2e4Zxft",
    "vasina.darya.2000@mail.ru": "pv3AtV0J8m0gw2nnR2YW",
    "milana.nikitina.2006@mail.ru": "8RqjzVxG5ezQxxiPqWbG",
    "anna-volkova-1987-volkova@mail.ru": "HhgGgSVC4Usq3kuneDze",
    "alya.andriyevskikh@mail.ru": "yk4AqeNrggudH9X943yu",
    "darina.naraykina@mail.ru": "EUXWUR8Vfz0vmg6AE2RU",
    "danil.shutenko.82@mail.ru": "DqLsXiz8i0xfXSN30APh",
    "vitya.mzhelskiy.03@mail.ru": "JLL0FrbYQhhXedgXY6v9",
    "brashnikov012@mail.ru": "rq5r2J9ALsCHmg7HdM6p",
    "viktoro111@mail.ru": "KZQDvvivuGgc0esmA2S0",
    "daryia017@mail.ru": "G0ERbunCY6eUpnhpdAUw",
    "andreevma075@mail.ru": "BRkjGfau16hUmzw3ZhZ5",
    "kydishkun001@mail.ru": "bs9XdzHV3i9mTKfNeTyv",
    "shkil120@mail.ru": "ufkpr7dLX4n6dmyXuvWk",
    "raterov911@mail.ru": "M00a9DRwXqafxS0sxfwd"
}
recievers = { #получатели
    "support@telegram.org",
    "dmca@telegram.org",
    "security@telegram.org",
    "sms@telegram.org",
    "info@telegram.org",
    "marta@telegram.org",
    "spam@telegram.org",
    "alex@telegram.org",
    "abuse@telegram.org",
    "pavel@telegram.org",
    "durov@telegram.org",
    "elies@telegram.org",
    "ceo@telegram.org",
    "mr@telegram.org",
    "levlam@telegram.org",
    "perekopsky@telegram.org",
    "recover@telegram.org",
    "germany@telegram.org",
    "hyman@telegram.org",
    "qa@telegram.org",
    "Stickers@telegram.org",
    "ir@telegram.org",
    "vadim@telegram.org",
    "shyam@telegram.org",
    "stopca@telegram.org",
    "support@telegram.org",
    "ask@telegram.org",
    "125support@telegram.org",
    "me@telegram.org",
    "enquiries@telegram.org",
    "api_support@telegram.org",
    "marketing@telegram.org",
    "ca@telegram.org",
    "recovery@telegram.org",
    "http@telegram.org",
    "corp@telegram.org",
    "corona@telegram.org",
    "ton@telegram.org",
    "sticker@telegram.org"
}
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def send_email(receiver, sender_email, sender_password, subject, body):
    for sender_email, sender_password in senders.items():
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.mail.ru', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver, msg.as_string())
            time.sleep(3)
            server.quit()
            return True
        except Exception as e:
            continue
    return False


def handle_complaint(senders, receivers):
    total_emails = len(senders) * len(receivers)
    sent_emails = 0
id = input(cyan + "[?] Введите ID -> ")
number = input(cyan + "[?] Введите номер -> ")
complaint_texts = {
                    "1": f"Здравствуйте, мой аккаунт с номером:" + str(number) + "ID аккаунта:" + str(id) + "взломали и при заходе на аккаунт мою сессию постоянно завершают, поэтому прошу вас обнулите все сессии или вовсе деактивируйте мой аккаунт"
                    }
for sender_email, sender_password in senders.items():
     for receiver_email in recievers:
        complaint_text = complaint_texts
        complaint_body = complaint_text.format(number=number.strip(), id=id.strip())
        sender_email, sender_password = random.choice(list(senders.items()))
        receiver = random.choice(receiver_email)
        send_email(receiver_email, sender_email, sender_password, "Взлом аккаунта telegram", complaint_body)
        print(cyan + "[!] Успешно отправлено")
        sent_email = 0
if __name__ == "__main__":
    handle_complaint(senders, recievers)