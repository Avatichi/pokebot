import telebot
import schedule
import urllib
bot_token = "325137796:AAHF4qgQBIGa0sKL2RyARfCbySlH8Ga8qac"

user_list_file = "users.txt"
with open(user_list_file, "rb") as f:
    users_files = f.read()

all_users = []
for user in users_files.split("\n"):
    if user != "":
        all_users.append(int(user))

bot = telebot.TeleBot(token=bot_token)

POKE_INDEX = 477
pokemon_file = "pokemon-svg/svg/*-{}.jpg"

a = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/{}.png"



def send_pokemon():
    global POKE_INDEX
    # print pokemon_file.format(str(POKE_INDEX))
    # photo = open(pokemon_file.format(str(POKE_INDEX)), 'rb')
    urllib.urlretrieve(a.format(str(POKE_INDEX)), "tmp.png")
    photo = open("tmp.png", 'rb')

    for user in all_users:
        bot.send_photo(user, photo)
    POKE_INDEX = POKE_INDEX - 1



schedule.every().day.at("08:00").do(send_pokemon)

while True:
    schedule.run_pending()




