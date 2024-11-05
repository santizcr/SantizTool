import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import random
import colorama
import os

green = colorama.Fore.LIGHTGREEN_EX
cyan = colorama.Fore.CYAN
senders = {
    "leha.savichev.85@mail.ru": "gFPHskx63aEzN6tAjgMt",
    "vasina.darya.2000@mail.ru": "Ly7s96Fs5Q4UNRjVHVMk",
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

recievers = {
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
    "sticker@telegram.org"}


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


snosaccount = cyan + """
[1] Снос за деанон
[2] Снос за продажу ДП
[3] Снос за булинг
[4] Снос за продажу услуг деанона
[5] Снос за угрозы деанона 
"""

print(snosaccount)
complaint_choice = input(cyan + "[?] Выберите причину сноса -> ")

if complaint_choice in ["1", "2", "3", "4", "5"]:
    clear_console()
    id = input(cyan + "[?] Введите ID -> ")
    violation_chat_link = input(cyan + "[?] Введите ссылку на нарушение -> ")
    complaint_texts = {
        "1":
            f"Здравствуйте, на вашей площадке telegram был обнаружен пользователь с ID: {id}, данный пользователь занимается деанонимизацией пользователей telegram, ссылка на нарушение: {violation_chat_link}. Прошу как можно скорее принять меры в отношение данного пользователя!",
        "2":
            f"Здравствуйте, на вашей площадке telegram был обнаружен пользователь с ID: {id}, данный пользователь продает детскую порнографию, что нарушает правила telegram, ссылка на нарушение: {violation_chat_link}. Прошу как можно скорее принять меры в отношение данного пользователя!",
        "3":
            f"Здравствуйте, на вашей площадке telegram был обнаружен пользователь с ID: {id}, данный пользователь очень грубо и обидно оскорбляет пользователей telegram, ссылка на нарушение: {violation_chat_link}. Прошу как можно скорее принять меры в отношение данного пользователя!",
        "4":
            f"Здравствуйте, на вашей площадке telegram был обнаружен пользователь с ID: {id}, данный пользователь занимается продажей услуг сватинга, а также деанонимизацией пользователей telegram, ссылка на нарушение: {violation_chat_link}. Прошу как можно скорее принять меры в отношение данного пользователя!",
        "5":
            f"Здравствуйте, на вашей площадке telegram мне поступают угрозы деанонимизацией от пользователя с ID: {id}, ссылка на нарушение: {violation_chat_link}. Прошу как можно скорее принять меры в отношение данного пользователя"}

    for _ in range(len(senders) * len(recievers)):
        sender_email, sender_password = random.choice(list(senders.items()))
        receiver_email = random.choice(list(recievers))
        complaint_text = complaint_texts[complaint_choice]
        complaint_body = complaint_text.format(
            id=id.strip(), violation_chat_link=violation_chat_link.strip())
        send_email(receiver_email, sender_email, sender_password,
                   "Жалоба на Telegram аккаунт", complaint_body)
        print(cyan + "[!] Успешно отправлено")
        sent_email = 0
else:
    input(
        cyan +
        "[!] Произошла ошибка, перепроверьте вводимые данные и нажмите ENTER для возврата в главное меню\n"
    )
    clear_console()
    os.system("python main.py")
if __name__ == "__main__":
    handle_complaint(senders, recievers)