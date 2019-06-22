import telebot
import time
bot_token = "325137796:AAHF4qgQBIGa0sKL2RyARfCbySlH8Ga8qac"

user_list_file = "users.txt"
with open(user_list_file, "rb") as f:
    users_files = f.read()

all_users = [int(i) for i in users_files.split("\n")]

bot = telebot.TeleBot(token=bot_token)


def write_user():
    with open(user_list_file, "wb") as f:
        f.write("\n".join([str(i) for i in all_users]))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.id in all_users:
        bot.reply_to(message, "You are in the list my friend")
    else:
        all_users.append(message.chat.id)
        write_user()
        bot.reply_to(message, "Welcome to pokebot!")

@bot.message_handler(commands=['stop'])
def stop_welcome(message):
    if message.chat.id in all_users:
        all_users.remove(message.chat.id)
        write_user()
        bot.reply_to(message, "goodbye")

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
