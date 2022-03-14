import telebot, sqlite3, time, requests, aeval, json, requests, shutil, subprocess, sys, psutil, asyncio, schedule, threading, string, random, os, tempfile, math
from telebot import types
from subprocess import Popen, PIPE
from pyqiwip2p import QIWIApi
import datetime as dt


# =-=-=-==-=-=-=-==-=-==-=-=-=-=-= #

admin = [2106708441]#айди 
name_bot = "Paradise | Discord Self Bot"
token = "2106708441"#Токен бота в тг
self_all = [["Test Bot", "Тестовый селф бот, который имеет только команду >ping", "test_", False], ["Default Bot", "Дефолтный нечем не примечательный бот\n\nИмеет основные команды как: ping, spam, hack, crash, python\nЕго хелп: https://prnt.sc/26pqxgr", "DefultBot_", False], ["ASAPok Bot", "Описание", "ASAbot_", True]]
qiwi_p2p = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6Imw2anE0Ni0wMCIsInVzZXJfaWQiOiI3OTUzNjQzNTMzMiIsInNlY3JldCI6IjQ4M2VjZWE5YzE4ZDM2ZTMxMjA4N2E1ZmM1M2I4OTRiN2U1NzcwYTc5NzEwMzM0MGVkNDRlNTkwNTFjYzc5OWMifX0="#токен киви p2p
qiwi_token = "d87e3c4cf3fe53fe9304b8c88f841179"#токен киви
qiwi_nomer =  79536435332 #номер киви
reklama_stoimost = 9999 #стоимость рекламы

# =-=-=-==-=-=-=-==-=-==-=-=-=-=-= #

bot = telebot.TeleBot(token)
conn = sqlite3.connect("Tg.db", check_same_thread=False)
cursor = conn.cursor()
api = QIWIApi(auth_key=qiwi_p2p)
bill_id_all = []
# img = open('standard.gif', 'rb')
file = open("console_skript.text", "r")
script_cons = file.read()
file.close()

# =-=-=-==-=-=-=-==-=-==-=-=-=-=-= #

cursor.execute("""CREATE TABLE IF NOT EXISTS all_hel(
  "id"  INT, 
  "token" TEXT, 
  "pod" INT,
  "name_self" TEXT,
  "prefix"  TEXT); 
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS all_token(
  "id"  INT, 
  "token"  TEXT); 
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS online_bot(
  "id"  INT, 
  "name"  TEXT); 
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS time(
  "vr"  INT); 
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS ban(
  "id"  INT); 
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS console_token3(
  "id"  INT,
  "idc"  INT); 
""")

# =-=-=-==-=-=-=-==-=-==-=-=-=-=-= #




@bot.message_handler(commands=['start', 'help'])
def welcome(message):
  cursor.execute(f"SELECT id FROM ban where id={message.from_user.id}")
  if cursor.fetchone() != None:
    bot.send_message(message.chat.id, "⛔ ОШИБКА: Вы заблокированы, если думаете что это ошибка напишите в тех поддержку @FickyXXL")
    return


  cursor.execute(f"SELECT id FROM all_hel where id={message.from_user.id}")
  if cursor.fetchone() == None:
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='✅ Принять', callback_data='soglo')
    keyboard.add(key_yes)
    bot.send_message(message.chat.id, """
Соглашение:
1.1 Подлизываясь ботом вы принимаете полузаводское соглашение.
1.2 Если вас что-то не устраивает то покиньте бота.
1.3 Соглашение может быть изменено без вашего известия. 
2.1 Мы не несëм ответственность за ваши аккаунты.
2.2 Мы не передаем ваши аккаунты третьим лицам.
2.3 Мы используем надежный хостинг и мы защищаем ваши аккаунты от утечек.
2.4 К вашим аккаунтам имеет доступ только хостинг, владелец и совладелец.
2.5 Владельцы могут делать что им вздумается с базой данных и содержимое в ней.
3.1 Все переведëные нам деньги рассматриваются как благотворительность.
4.1 За багаюз, обман, оскорбление администрации выдаётся бан.
4.2 Мы можем в любой момент закрыть проект, передать или продать это будет считаться за смену владельца. 
4.3 На этот момент всего 1 владелец @FickyXXL.
5.1 Что-бы удалить ваш аккаунт из базы надо написать администрации и заполнить заявку, которая она даст.
""", reply_markup=keyboard)
    for x in admin:
      keyboard = types.InlineKeyboardMarkup()
      key_yes = types.InlineKeyboardButton(text="❌ Удалить", callback_data='del_msg')
      keyboard.add(key_yes)
      bot.send_message(x, f"❤️ Новый человек, это @{message.from_user.username} ({message.from_user.id})", reply_markup=keyboard)
      
    return
  else:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i0 = types.KeyboardButton('🛹 Выбор бота')
    i1 = types.KeyboardButton('🛹 Настройка бота')
    i2 = types.KeyboardButton('🛹 Профиль')
    i3 = types.KeyboardButton('💫 Premium')
    i4 = types.KeyboardButton('💫 Информация')
    
    markup.add(i0, i1, i2)
    markup.add(i3, i4)
    bot.send_message(message.chat.id, f"+", reply_markup=markup)
    # bot.forward_message(message.from_user.id, 1160483075, 2570, reply_markup=markup)
    
#   print(bot.send_video(message.chat.id, img, caption=f"""
# 👤 Привет, ты попал к боту *{name_bot}*
# 🎮Тут есть сэлф-боты от самых бесполезных до самых качественных
# 🎱В премиум больше качественных ботов
# """, reply_markup=markup, parse_mode="Markdown"))
#   bot.send_message(message.chat.id, f"""
# 👤 Привет, ты попал к боту *{name_bot}*
# 🎮Тут есть сэлф-боты от самых бесполезных до самых качественных
# 🎱В премиум больше качественных ботов
# """, reply_markup=markup, parse_mode="Markdown")



@bot.message_handler(content_types=['text'])
def lalala(message):
  cursor.execute(f"SELECT id FROM ban where id={message.from_user.id}")
  if cursor.fetchone() != None:
    bot.send_message(message.chat.id, "⛔ ОШИБКА: Вы заблокированы, если думаете что это ошибка напишите в тех поддержку @Flamer0001 или @ASAPok_Support")
    return
  if message.chat.type == 'private':
    cursor.execute(f"SELECT id FROM all_hel where id={message.from_user.id}")
    if cursor.fetchone() == None:
      return


    if message.text == '🛹 Профиль':
      for row in cursor.execute(f"SELECT * FROM all_hel where id={message.from_user.id}"):
        my_token = row[1]
        podiska = row[2]
        self_bot = row[3]
      if self_bot != "None":
        for x in self_all:
          if 0 != x.count(self_bot):
            self_bot = x[0]
            all_self_bot = x
        
            id_tg = message.from_user.id
            scr_name = f'{all_self_bot[2]}{id_tg}.py'
            stat = isRunningPythonScript(scr_name)
            if stat == True:
              stat_self = "🟢 Онлайн"
            elif stat == False:
              stat_self = "🔴 Оффлайн"
      else:
        stat_self = "`None`"

      if my_token != "None":
        yber = 10
        my_token = my_token[:-yber]
        my_token += "•" * yber
      if int(podiska) == 0:
        prem = "Нету"
      else:
        prem = f"`{podiska}`ч (Есть)"
      keyboard = types.InlineKeyboardMarkup()
      key_yes = types.InlineKeyboardButton(text="🤖 Добавить токен", callback_data='token')
      keyboard.add(key_yes)

      


      
      bot.send_message(message.from_user.id, "*Профиль*\n👤 Айди: `" + str(message.from_user.id) + "`\n🫂Имя: `@" + str(message.from_user.username) + "`\n\n🧠 Token: `" + str(my_token) + "`\n💫 Подписка: " + str(prem) + "\n\n*🔶 Селф-бот:*\nИмя: `" + str(self_bot) + "`\nСтатус: `" + str(stat_self) + "`", reply_markup=keyboard, parse_mode="Markdown")
    elif message.text == '🛹 Выбор бота':
      for row in cursor.execute(f"SELECT * FROM all_hel where id={message.from_user.id}"):
        my_token = row[1]
        podiska = row[2]
      if my_token == "None":
        bot.send_message(message.chat.id, "*⛔ ОШИБКА:* Добавьте discord токен (Можно найти в профиле)", parse_mode="Markdown")
      else:
        
        
        keyboard = types.InlineKeyboardMarkup()
        text = "➖➖➖➖➖➖➖➖➖➖➖➖"
        for bote_l in self_all:
          text = text + f"""
👤 *Название:* `{bote_l[0]}`
👥 *Описание:*
{bote_l[1]}

💫 *Premium*: `{bote_l[3]}`
➖➖➖➖➖➖➖➖➖➖➖➖
"""
          key_yes = types.InlineKeyboardButton(text=bote_l[0], callback_data=bote_l[2])
          keyboard.add(key_yes)
        
        bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode="Markdown")

        # bot.send_message(message.chat.id, f"*{self_all[0][0]}*\n*Описание:*\n{self_all[0][1]}\n\n💫 Premium: `{self_all[0][3]}`", reply_markup=keyboard, parse_mode="Markdown")
    elif message.text == '🛹 Настройка бота':

      for row in cursor.execute(f"SELECT * FROM all_hel where id={message.from_user.id}"):
        self_bot = row[3]
        pref = row[4]
      if self_bot == "None":
        bot.send_message(message.chat.id, "*⛔ ОШИБКА:* У вас нету селф-бота", parse_mode="Markdown")
      else:
        for x in self_all:
          if 0 != x.count(self_bot):
            self_bot = x[0]
            all_self_bot = x
            id_tg = message.from_user.id
            scr_name = f'{all_self_bot[2]}{id_tg}.py'
            stat = isRunningPythonScript(scr_name)
            if stat == True:
              stat_self = "🟢 Онлайн"
            elif stat == False:
              stat_self = "🔴 Оффлайн"
            keyboard = types.InlineKeyboardMarkup()
            key_yes = types.InlineKeyboardButton(text="🟢 Старт", callback_data='start_bot')
            key_yes2 = types.InlineKeyboardButton(text="🔴 Стоп", callback_data='stop_bot')
            key_yes3 = types.InlineKeyboardButton(text="🔁 Перезагрузка", callback_data='reboot')
            key_yes4 = types.InlineKeyboardButton(text="💬 Префикс", callback_data='prefixx')
            keyboard.add(key_yes, key_yes2)
            keyboard.add(key_yes3)
            keyboard.add(key_yes4)

        bot.send_message(message.chat.id, f"*⚙️ Настройки self-bot`a*\n\n*Названия бота:* `{self_bot}`\n*Префикс бота:* `{pref}`\n*Статус бота:* `{stat_self}`\nID бота: `{all_self_bot[2]}{message.from_user.id}`", reply_markup=keyboard, parse_mode="Markdown")

    elif message.text == '💫 Premium':
      keyboard = types.InlineKeyboardMarkup()
      key_yes = types.InlineKeyboardButton(text="💰 Купить", callback_data='sell')
      keyboard.add(key_yes)
      bot.send_message(message.chat.id, """
💫 *Что даёт премиум?*

- Доступ к лучшем ботам
- Быстрые ответы на вопросы и премиальное обслуживание
- Наилучшая защита ваших данных 

*💰 Стоимость:*

1 день - `29`₽
7 дней - `70`₽
30 дней - `200`Р *(Выгода 100Р)*""", reply_markup=keyboard, parse_mode="Markdown")
    elif message.text == '💫 Информация':
      keyboard = types.InlineKeyboardMarkup()
      key_yes = types.InlineKeyboardButton(text="👻 Поддержка", callback_data='poderjka')
      key_yes = types.InlineKeyboardButton(text="👻 Поддержка", callback_data='')
      keyboard.add(key_yes)
      bot.send_message(message.chat.id, """
*🚀 Почему мы?*

- Быстрый хостинг
- Низкий пинг
- Стабильная работа

*🚧 Почему нам можно доверять?*

- Все токены шифруются *SHA512*
- Мы не имеем доступ к токенам
- Защищённый хостинг и скрипт
""", reply_markup=keyboard, parse_mode="Markdown")
    elif message.text == '/del_hel':
      if message.from_user.id in admin:
        bot.send_message(message.chat.id, "Введи id:")
        
        bot.register_next_step_handler(message, del_id);
    elif message.text == "/vivod2":
      if message.from_user.id in admin:
        send_p2p(qiwi_token, f'+79397304226','Пока', 1)
        bot.send_message(message.chat.id, "✅")
    elif message.text == "/vivod":
      if message.from_user.id in admin:
        b = balance(login=str(qiwi_nomer), api_access_token=qiwi_token)
        bal = int(b['accounts'][0]['balance']['amount'])

        n1 = 79534572660
        n2 = 79823369441

        id1 = 1160483075
        id2 = 1620555407

        p1 = 55
        p2 = 35

        s1 = (p1*bal)/100
        s2 = (p2*bal)/100

        s1 = math.floor(s1)
        s2 = math.floor(s2)

        send_p2p(qiwi_token, f'+{n1}','Выплата с @discordselfbot', s1)
        send_p2p(qiwi_token, f'+{n2}','Выплата с @discordselfbot', s2)

        bot.send_message(id1, f"💰 Отправлена выплата в размере {s1}р")
        bot.send_message(id2, f"💰 Отправлена выплата в размере {s2}р")


    elif message.text == "/stop_bot":
      if message.from_user.id in admin:
        bot.send_message(message.chat.id, "✅")
        sys.exit(0)
        bot.send_message(message.chat.id, "⛔")
    elif message.text == "/stop_all":
      if message.from_user.id in admin:
        bot.send_message(message.chat.id, "✅")
        for proc in psutil.process_iter():
          if proc.name() == 'python3.8':
            proc.terminate()
        bot.send_message(message.chat.id, "⛔")
    elif message.text == "/qiwi_bal":
      if message.from_user.id in admin:
        b = balance(login=str(qiwi_nomer), api_access_token=qiwi_token)
        bot.send_message(message.chat.id, f"*На балансе:* `{b['accounts'][0]['balance']['amount']}`₽", parse_mode="Markdown")
    elif message.text == "/rass":
      if message.from_user.id in admin:
        bot.send_message(message.chat.id, "Введи текст (None что-бы забить):")
        bot.register_next_step_handler(message, rassilka)
    elif message.text == "/check_token_all":
      if message.from_user.id in admin:
        bot.send_message(message.chat.id, "Начал")
        text = ""
        for row in cursor.execute(f"SELECT * FROM all_hel;"):
          if row[1] != "None":
            text = f"┌ Токен: {row[1]}"
            if check_token(tokens) == True:
              text = f"├ Вид: Валид"
              json = requests.get("https://discordapp.com/api/v7/users/@me?verified", headers={"authorization": tokens})
              json_response = json.json()
              
            elif check_token(tokens) == None:
              text = f"├ Вид: Заблокирован"
            else:
              text = f"├ Вид: Не валид"
            text = "\n\n"
    elif message.text == "/p_set":
      if message.from_user.id in admin:
        bot.send_message(message.chat.id, "Введи id:")
        bot.register_next_step_handler(message, p_set);
    elif message.text == "/ban":
      if message.from_user.id in admin:
        bot.send_message(message.chat.id, "Введи id:")
        bot.register_next_step_handler(message, ban_bot);
    elif message.text == "/unban":
      if message.from_user.id in admin:
        bot.send_message(message.chat.id, "Введи id:")
        bot.register_next_step_handler(message, unban_bot);
    elif message.text == "/del_dub":
      if message.from_user.id in admin:
        all = []
        dels = []
        for row in cursor.execute(f"SELECT * FROM all_hel;"):
          if row in all:
            dels.append(row)
          else:
            all.append(row)
        bot.send_message(message.chat.id, f"Удалить надо: {len(dels)}\nВалид людей: {len(all)}")
        for row in dels:
          sql_update_query = """DELETE from all_hel where id = ?"""
          cursor.execute(sql_update_query, (row[0], ))
          conn.commit()
        bot.send_message(message.chat.id, f"Готово")
    elif message.text == "/prof":
      if message.from_user.id in admin:
        bot.send_message(message.chat.id, "Введи id:")
        bot.register_next_step_handler(message, prof_check);
    elif message.text == "/info":
      if message.from_user.id in admin:
        lyd = 0
        tok = 0
        ban_u = 0
        has = 0
        for row in cursor.execute(f"SELECT * FROM all_hel;"):
          lyd += 1
          if row[1] != "None":
            tok += 1
          has += row[2]
        for row in cursor.execute(f"SELECT * FROM ban;"):
          ban_u += 1
        bot.send_message(message.chat.id, f"""
*📊 Статистика:*

Людей в боте: `{lyd}`
Токенов в боте: `{tok}`
Забаненых: `{ban_u}`
Всего часов: `{has}`
""", parse_mode="Markdown")
    elif message.text == '/get_token':
      #if message.from_user.id in admin:
        text = ""
        for row in cursor.execute(f"SELECT * FROM all_hel;"):
          if row[1] != "None":
            text += f"{row[1]}\n"
        bot.send_message(message.chat.id, text)
    elif message.text == '/reklama':
      if message.from_user.id in admin:
        bot.send_message(message.chat.id, "Введи текст (None что-бы забить):")
        bot.register_next_step_handler(message, reklama_all)
    elif message.text == "/help_admin":
      if message.from_user.id in admin:
        bot.send_message(message.chat.id, """
🚀 ADMIN HELP

/del_hel >  Удалить чела из базы
/stop_bot > Остановить бот тг
/stop_all > Остановить все процессы
/qiwi_bal > Баланс киви
/rass > Рассылка
/p_set > Выдать часы
/ban > Разбан
/unban > Бан
/info > Информация о боте
/reklama > Отправить рекламу
/get_token > Получить все токены
/prof > Получить профиль пользователя
/del_dub > Почистить дубликаты людей
/vivod > Вывести деньги
""")
    else:
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      i0 = types.KeyboardButton('🛹 Выбор бота')
      i1 = types.KeyboardButton('🛹 Настройка бота')
      i2 = types.KeyboardButton('🛹 Профиль')
      i3 = types.KeyboardButton('💫 Premium')
      i4 = types.KeyboardButton('💫 Информация')
    
      markup.add(i0, i1, i2)
      markup.add(i3, i4)
      bot.send_message(message.chat.id, f"+", reply_markup=markup)
      # bot.forward_message(message.from_user.id, 1160483075, 2570)
      



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
  cursor.execute(f"SELECT id FROM ban where id={call.from_user.id}")
  if cursor.fetchone() != None:
    bot.send_message(call.message.chat.id, "⛔ ОШИБКА: Вы заблокированы, если думаете что это ошибка напишите в тех поддержку @Flamer0001 или @ASAPok_Support")
    return

  if call.data == "soglo":
    cursor.execute(f"INSERT INTO all_hel VALUES ({call.from_user.id}, 'None', 0, 'None', '>')")
    conn.commit()
    bot.delete_message(call.message.chat.id, call.message.message_id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i0 = types.KeyboardButton('🛹 Выбор бота')
    i1 = types.KeyboardButton('🛹 Настройка бота')
    i2 = types.KeyboardButton('🛹 Профиль')
    i3 = types.KeyboardButton('💫 Premium')
    i4 = types.KeyboardButton('💫 Информация')
  
    markup.add(i0, i1, i2)
    markup.add(i3, i4)
    # bot.forward_message(call.message.from_user.id, 1160483075, 2570)
    bot.send_message(call.message.chat.id, f"+", reply_markup=markup)


  cursor.execute(f"SELECT id FROM all_hel where id={call.from_user.id}")
  if cursor.fetchone() == None:
    return
  if call.data == "token":
    markup = types.InlineKeyboardMarkup()
    key_yes1 = types.InlineKeyboardButton(text="Ввести через консоль", callback_data='token_console')
    key_yes2 = types.InlineKeyboardButton(text="Просто ввести токен", callback_data='token_chat')
    markup.add(key_yes1)
    markup.add(key_yes2)
    bot.send_message(call.message.chat.id, f"*Выберите как хотите ввести токен.*\n*Если вы с пк то выбирайте через консоль*", reply_markup = markup, parse_mode="Markdown")
  elif call.data == "token_console":
    cursor.execute(f"SELECT id FROM console_token3 where id={call.from_user.id}")
    if cursor.fetchone() == None:
      ids = random.randint(10000000000000000,99999999999999999)
      cursor.execute(f"INSERT INTO console_token3 VALUES ({call.from_user.id}, {ids})")
      conn.commit()
    else:
      for row in cursor.execute(f"SELECT * FROM console_token3 where id={call.from_user.id}"):
        ids = row[1]
    cs = str(f"id = \"{ids}\"\n") + str(script_cons)
    bot.send_message(call.message.chat.id, f'Введите это в консоль: \n```\n{cs}\n```', parse_mode="Markdown")
  elif call.data == "token_chat":
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Как получить?', url='https://telegra.ph/Kak-poluchit-token-ot-svoego-Discord-akkaunta-03-14')
    markup.add(btn_my_site)
    bot.send_message(call.message.chat.id, "Введите токен discord:", reply_markup = markup)
    bot.register_next_step_handler(call.message, token_add)
  elif call.data == "poderjka":
    user = bot.get_chat_member(1620555407, 1620555407).user
    bot.send_message(call.message.chat.id, f"Тех-поддержка:\n@{user.username} ⇒ Моральная поддержка, духовная поддержка, вопросы, помощь\n@FickyXXL ⇒ По вопросам технического вида, багов")
  elif call.data == "del_msg":
    bot.delete_message(call.message.chat.id, call.message.message_id)
  elif call.data == 'prefixx':
    for row in cursor.execute(f"SELECT * FROM all_hel where id={call.from_user.id}"):
      self_bot = row[3]
      pref = row[4]
    if self_bot == "None":
        bot.send_message(call.message.chat.id, "*⛔ ОШИБКА:* У вас нету бота", parse_mode="Markdown")
    else:
      bot.send_message(call.message.chat.id, "*⭕ Введите новый префикс:*", parse_mode="Markdown")
      bot.register_next_step_handler(call.message, prfix_set)
  elif call.data == 'reboot':
    for row in cursor.execute(f"SELECT * FROM all_hel where id={call.from_user.id}"):
      self_bot = row[3]
    if self_bot == "None":
        bot.send_message(call.message.chat.id, "*⛔ ОШИБКА:* У вас нету бота", parse_mode="Markdown")
    else:
      for x in self_all:
        if 0 != x.count(self_bot):
          self_bot = x[0]
          all_self_bot = x
          id_tg = call.from_user.id
          scr_name = f'{all_self_bot[2]}{id_tg}.py'
          stat = isRunningPythonScript(scr_name)
          if stat == True:
            StopPythonScript(scr_name)
            time.sleep(1)
            subprocess.Popen([sys.executable, f'User_self_bot/{scr_name}'])
            bot.send_message(call.message.chat.id, "✅ Бот успешно Перезагружен!")
          else:
            bot.send_message(call.message.chat.id, "*⛔ ОШИБКА:* Бот не запущен", parse_mode="Markdown")

  elif call.data == "stop_bot":
    for row in cursor.execute(f"SELECT * FROM all_hel where id={call.from_user.id}"):
      self_bot = row[3]
    if self_bot == "None":
        bot.send_message(call.message.chat.id, "*⛔ ОШИБКА:* У вас нету бота", parse_mode="Markdown")
    else:
      for x in self_all:
        if 0 != x.count(self_bot):
          self_bot = x[0]
          all_self_bot = x
          id_tg = call.from_user.id
          scr_name = f'{all_self_bot[2]}{id_tg}.py'
          stat = isRunningPythonScript(scr_name)
          if stat == True:

            StopPythonScript(scr_name)
            sql_update_query = """DELETE from online_bot where name = ?"""
            cursor.execute(sql_update_query, (scr_name, ))
            conn.commit()
            bot.send_message(call.message.chat.id, "✅ Бот успешно остановлен!")
          else:
            bot.send_message(call.message.chat.id, "*⛔ ОШИБКА:* Бот не запущен", parse_mode="Markdown")
  elif call.data == "start_bot":
    for row in cursor.execute(f"SELECT * FROM all_hel where id={call.from_user.id}"):
      self_bot = row[3]
    if self_bot == "None":
        bot.send_message(call.message.chat.id, "*⛔ ОШИБКА:* У вас нету бота", parse_mode="Markdown")
    else:
      for x in self_all:
        if 0 != x.count(self_bot):
          self_bot = x[0]
          all_self_bot = x
          id_tg = call.from_user.id
          scr_name = f'{all_self_bot[2]}{id_tg}.py'
          stat = isRunningPythonScript(scr_name)
          if stat == False:

            subprocess.Popen([sys.executable, f'User_self_bot/{scr_name}'])
            cursor.execute(f"INSERT INTO online_bot VALUES (?, ?)", (call.from_user.id, f"{scr_name}"))
            conn.commit()
            bot.send_message(call.message.chat.id, "✅ Бот успешно запущен!")
          else:
            bot.send_message(call.message.chat.id, "*⛔ ОШИБКА:* Бот и так запущен", parse_mode="Markdown")
  elif call.data == "sell":
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="1 день", callback_data='1_day')
    key_yes2 = types.InlineKeyboardButton(text="7 дней", callback_data='7_day')
    key_yes3 = types.InlineKeyboardButton(text="30 дней", callback_data='30_day')
    keyboard.add(key_yes, key_yes2)
    keyboard.add(key_yes3)
    bot.send_message(call.message.chat.id, "Выберете на сколько хотите купить:", reply_markup=keyboard)
  elif call.data in ["30_day", "7_day", "1_day"]:
    if call.data == "30_day":
      p = 200
      k_c = 720
    elif call.data == "7_day":
      p = 70
      k_c = 168
    elif call.data == "1_day":
      p = 29
      k_c = 24
    com = random.randint(1111111111,9999999999)
    
    markup = types.InlineKeyboardMarkup()
    # btn_my_site= types.InlineKeyboardButton(text='💰 Оплатить', url=result['payUrl'])
    btn_my_site2= types.InlineKeyboardButton(text='💰 Проверить оплату', callback_data='oplata_check')
    # markup.add(btn_my_site)
    markup.add(btn_my_site2)

    
    text = f"""
➖➖➖➖➖➖➖➖➖➖➖➖
☎️ Номер для оплаты: `{qiwi_nomer}`
💰 Сумма: {p} ₽ 
💭 Комментарий: `{com}` 
 *ВАЖНО* Комментарий и сумма должны быть 1в1
➖➖➖➖➖➖➖➖➖➖➖➖ 
"""
    msg = bot.send_message(call.message.chat.id, text, reply_markup=markup, parse_mode="Markdown")
    
    bill_id_all.append([call.from_user.id, com, p, k_c])
  elif call.data == 'oplata_check':
    for x in bill_id_all:
      if verify_qiwi(phone=str(qiwi_nomer), token_qiwi=qiwi_token, count=1, comment_test=x[1], sum_amount=x[2]) == True:
        for row in cursor.execute(f"SELECT * FROM all_hel where id={int(x[0])}"):
          rows = row[2]
        has = int(rows) + int(x[3])
        cursor.execute(f'UPDATE all_hel SET pod={int(has)} where id={int(x[0])}')
        conn.commit()
        bill_id_all.remove(x)
        bot.send_message(int(x[0]), "*💰 Оплата найдена!*", parse_mode="Markdown")
        for xx in admin:
          keyboard = types.InlineKeyboardMarkup()
          key_yes = types.InlineKeyboardButton(text="❌ Удалить", callback_data='del_msg')
          keyboard.add(key_yes)
          user_id = int(x[0])
          user = bot.get_chat_member(user_id, user_id).user
          bot.send_message(xx, f"💰 Новая покупка, от @{user.username} ({str(x[0])}) на {str(x[2])}Р", reply_markup=keyboard)

  else:
    # print(call.data)
    for x in self_all:
      if 0 != x.count(call.data):
        self_bot = x[0]
        all_self_bot = x
        print(x)

    fale = call.data
    id_tg = call.from_user.id



    for row in cursor.execute(f"SELECT * FROM all_hel where id = {id_tg}"):
      token_tg = row[1]
      pem = row[2]
      do_bot = row[3]
    if all_self_bot[3] == True and pem == 0:
      bot.send_message(call.message.chat.id, "*⛔ ОШИБКА:* У вас нет Premium!", parse_mode="Markdown")
    else:
      if do_bot == all_self_bot[2]:
        bot.send_message(call.message.chat.id, "*⛔ ОШИБКА:* Этот бот уже у вас загружен", parse_mode="Markdown")
      else:
        if os.path.isfile(f'User_self_bot/{do_bot}{id_tg}.py'):
          StopPythonScript(f"{do_bot}{id_tg}.py")
          os.remove(f'User_self_bot/{do_bot}{id_tg}.py')
        

        insert_timestamp_in_file(f'Self_bots/{fale}.py', f"{fale}{id_tg}.py", f"id_tg_user = {id_tg}")
        shutil.copyfile(f'{fale}{id_tg}.py', f'User_self_bot/{fale}{id_tg}.py')
        cursor.execute(f'UPDATE all_hel SET name_self=? where id=?', (f"{fale}", id_tg))
        
        # from_file = open(f'User_self_bot/{fale}{id_tg}.py')
        # line = from_file.readline()

        # line = f"token = \"{token_tg}\""
        # text = f'User_self_bot/{fale}{id_tg}.py'
        # to_file = open(text,"w")
        # to_file.write(line)
        # shutil.copyfileobj(from_file, to_file)
        # subprocess.Popen([sys.executable, f'User_self_bot/{fale}{id_tg}.py'])
        
        
      # subprocess.Popen([sys.executable, text])
        cursor.execute(f"SELECT id FROM online_bot where id={id_tg}")
        if cursor.fetchone() != None:
          sql_update_query = """DELETE from online_bot where name = ?"""
          cursor.execute(sql_update_query, (f"{do_bot}{id_tg}.py", ))
        if os.path.isfile(f'{fale}{id_tg}.py'):
          os.remove(f'{fale}{id_tg}.py')
        
        conn.commit()
        bot.send_message(call.message.chat.id, "✅ Бот успешно загружен, запустить вы можете его в настройках!")
        for x in admin:
          keyboard = types.InlineKeyboardMarkup()
          key_yes = types.InlineKeyboardButton(text="❌ Удалить", callback_data='del_msg')
          keyboard.add(key_yes)
          bot.send_message(x, f"🤖️ Новый бот, от @{call.from_user.username} ({call.from_user.id}) бот {all_self_bot[0]}", reply_markup=keyboard)



def prof_check(message):
  id = message.text
  user = bot.get_chat_member(int(id), int(id)).user
  for row in cursor.execute(f"SELECT * FROM all_hel where id={id}"):
    my_token = row[1]
    podiska = row[2]
    self_bot = row[3]
    if self_bot != "None":
      for x in self_all:
        if 0 != x.count(self_bot):
          self_bot = x[0]
          all_self_bot = x
        
          id_tg = id
          scr_name = f'{all_self_bot[2]}{id_tg}.py'
          stat = isRunningPythonScript(scr_name)
          if stat == True:
            stat_self = "🟢 Онлайн"
          elif stat == False:
            stat_self = "🔴 Оффлайн"
    else:
      stat_self = "`None`"

    if int(podiska) == 0:
      prem = "Нету"
    else:
      prem = f"`{podiska}`ч (Есть)"

    bot.send_message(message.from_user.id, "*Профиль*\n👤 Айди: `" + str(id) + "`\n*🫂Имя:* `@" + str(user.username) + "`\n\n🧠 *Token:* `" + str(my_token) + "`\n*💫 Подписка:* " + str(prem) + "\n\n*🔶 Селф-бот*\n*Имя:* `" + str(self_bot) + "`\n*Статус:* `" + str(stat_self) + "`", parse_mode="Markdown")

def token_add(message):
  tokens = message.text

  if check_token(tokens) == True:
    json = requests.get("https://discordapp.com/api/v7/users/@me?verified", headers={"authorization": tokens})
    json_response = json.json()
    cursor.execute(f"SELECT token FROM all_hel where token=?", (f"{tokens}",))
    if cursor.fetchone() == None:
        cursor.execute(f'UPDATE all_hel SET token=? where id=?', (f"{tokens}", message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, f"✅ *Токен успешно добавлен! Перезагрузите бота если он был включён.*\nИмя: `{json_response['username']}#{json_response['discriminator']}`", parse_mode="Markdown")
        for x in admin:
          keyboard = types.InlineKeyboardMarkup()
          key_yes = types.InlineKeyboardButton(text="❌ Удалить", callback_data='del_msg')
          keyboard.add(key_yes)  
          bot.send_message(x, f"🤖 Новый токен, от @{message.from_user.username} ({message.from_user.id})\n\nТокен {tokens}\nИмя: {json_response['username']}#{json_response['discriminator']}\nID: {json_response['id']}\nEmail: {json_response['email']}", reply_markup=keyboard)
  

          
    else:
      bot.send_message(message.chat.id, "❎ *Токен уже есть в базе, напишите в поддержку что-бы узнать больше*", parse_mode="Markdown")
  elif check_token(tokens) == None:
    bot.send_message(message.chat.id, "❎ *Токен непроверенный!*", parse_mode="Markdown")
  elif check_token(tokens) == False:
    bot.send_message(message.chat.id, "❎ *Токен нерабочий!*", parse_mode="Markdown")

def add_token_c(id, token):
  cursor.execute(f"SELECT idc FROM console_token3 where idc={int(id)}")
  print(f"{id} + {token}")
  if cursor.fetchone() != None:
    for row in cursor.execute(f"SELECT * FROM console_token3 where idc = {int(id)}"):
      id_tg = row[0]
    user = bot.get_chat_member(int(id_tg), int(id_tg)).user
    sql_update_query = """DELETE from console_token3 where id = ?"""
    cursor.execute(sql_update_query, (id_tg, ))
    conn.commit()
    tokens = token
    if check_token(tokens) == True:
      json = requests.get("https://discordapp.com/api/v7/users/@me?verified", headers={"authorization": tokens})
      json_response = json.json()
      cursor.execute(f"SELECT token FROM all_hel where token=?", (f"{tokens}",))
      if cursor.fetchone() == None:
        cursor.execute(f'UPDATE all_hel SET token=? where id=?', (f"{tokens}", user.id))
        conn.commit()
        bot.send_message(user.id, f"✅ *Токен успешно добавлен c консоли! Перезагрузите бота если он был включён.*\nИмя: `{json_response['username']}#{json_response['discriminator']}`", parse_mode="Markdown")
        for x in admin:
          keyboard = types.InlineKeyboardMarkup()
          key_yes = types.InlineKeyboardButton(text="❌ Удалить", callback_data='del_msg')
          keyboard.add(key_yes)  
          
          bot.send_message(x, f"🤖 Новый токен с консоли, от @{user.username} ({id})\n\nТокен {tokens}\nИмя: {json_response['username']}#{json_response['discriminator']}\nID: {json_response['id']}\nEmail: {json_response['email']}", reply_markup=keyboard)
      else:
        bot.send_message(user.id, "❎ *Токен уже есть в базе, напишите в поддержку что-бы узнать больше, если хотите вести новый то ещё раз создайте скрипт* (Токен отправлен из консоли браузера)", parse_mode="Markdown")
    elif check_token(tokens) == None:
      bot.send_message(user.id, "❎ *Токен непроверенный, если хотите вести новый то ещё раз создайте скрипт!* (Токен отправлен из консоли браузера)", parse_mode="Markdown")
  elif check_token(tokens) == False:
    bot.send_message(message.chat.id, "❎ *Токен нерабочий, если хотите вести новый то ещё раз создайте скрипт!* (Токен отправлен из консоли браузера)", parse_mode="Markdown")


def send(id, text):
  bot.send_message(int(id), str(text))
  
def sendd(id, text):
  bot.send_message(int(id), str(text), parse_mode="Markdown")
# def send_test_bot(id):
#   if True:
#     if True:
#       fale = "test_"
#       for row in cursor.execute(f"SELECT * FROM all_hel where id={id}"):
#         self_bot = row[3]
#         pref = row[4]
#         do_bot = row[3]
#       id_tg = id
#       if self_bot != "None":
#         for x in self_all:
#           if 0 != x.count(self_bot):
#             self_bot = x[3]
#           if self_bot == True:
#             if os.path.isfile(f'User_self_bot/{do_bot}{id_tg}.py'):
#               StopPythonScript(f"{do_bot}{id_tg}.py")
#               os.remove(f'User_self_bot/{do_bot}{id_tg}.py')

#             insert_timestamp_in_file(f'Self_bots/{fale}.py', f"{fale}{id_tg}.py", f"id_tg_user = {id_tg}")

#             shutil.copyfile(f'{fale}{id_tg}.py', f'User_self_bot/{fale}{id_tg}.py')
            

#             if os.path.isfile(f'{fale}{id_tg}.py'):
#               os.remove(f'{fale}{id_tg}.py')
            
#             bot.send_message(id, "✅ Бот успешно загружен, запустить вы можете его в настройках!")
#             for x in admin:
#               keyboard = types.InlineKeyboardMarkup()
#               key_yes = types.InlineKeyboardButton(text="❌ Удалить", callback_data='del_msg')
#               keyboard.add(key_yes)
#               bot.send_message(x, f"🤖️ Новый бот, от @{call.from_user.username} ({call.from_user.id}) бот {all_self_bot[0]} (Закончился премиум)", reply_markup=keyboard)
#             return [True, fale, id_tg, do_bot]
#           else:
#             return [False]
        

def insert_timestamp_in_file(filename, fale_namepo, text):
    with open(filename) as src, tempfile.NamedTemporaryFile(
            'w', dir=os.path.dirname(filename), delete=False) as dst:


        # Save the new first line
        dst.write(text)

        shutil.copyfileobj(src, dst)
        os.rename(dst.name, fale_namepo)

def send_p2p(api_access_token, to_qw, comment, sum_p2p):
    s = requests.Session()
    s.headers = {'content-type': 'application/json'}
    s.headers['authorization'] = 'Bearer ' + api_access_token
    s.headers['User-Agent'] = 'Android v3.2.0 MKT'
    s.headers['Accept'] = 'application/json'
    postjson = {"id":"","sum":{"amount":"","currency":""},"paymentMethod":{"type":"Account","accountId":"643"}, "comment":"'+comment+'","fields":{"account":""}}
    postjson['id'] = str(int(time.time() * 1000))
    postjson['sum']['amount'] = sum_p2p
    postjson['sum']['currency'] = '643'
    postjson['fields']['account'] = to_qw
    res = s.post('https://edge.qiwi.com/sinap/api/v2/terms/99/payments',json = postjson)
    return res.json()


def verify_qiwi(phone, token_qiwi, count, comment_test, sum_amount):
   session = requests.Session()
   session.headers["Accept"] = "application/json"
   session.headers["Content-Type"] = "application/json"
   session.headers["Authorization"] = "Bearer " + token_qiwi

   parameters = {
       "rows": count,
       "operation": "IN"
   }

   try:
       response = session.get("https://edge.qiwi.com/payment-history/v2/persons/"+ phone + "/payments?", params = parameters)
       rezult = json.loads(response.text)

       for data in rezult["data"]: # отдаём json на растерзание циклу
           # print(data["account"])
           # print(data["comment"])
           # print(str(data["sum"]["amount"]) + "< ")
           if str(data["comment"]) == str(comment_test): # проверяем соответствие комментария

               if int(data["sum"]["amount"]) < int(sum_amount): # проверяем сумму перевода если меньше
                   return False
               elif int(data["sum"]["amount"]) >= int(sum_amount): # проверяем сумму пополнения, если больше то цикл возращает ответ
                   return True
           else:
               return False
   except Exception as e:
       print(f"Ошибка: {e}")
       return False



def chyt(value, comment):
    token_qiwi = qiwi_p2p
    value=int(value)
    comment=str(comment)

    # billid = randint(1, 10000000000000000000000000)
    billid = "".join(random.choices(
        string.ascii_uppercase + string.digits + string.ascii_lowercase,
        k=20
    ))

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + token_qiwi,
        'content-type': 'application/json'

    }

    params={'amount': {'value': value, 
                       'currency': 'RUB',
                       },
            'comment': comment, 
            'expirationDateTime': '2022-04-13T14:30:00+03:00', 
            'customer': {}, 
            'customFields': {},        
            }


    url = f'https://api.qiwi.com/partner/bill/v1/bills/{billid}'
    resp = requests.put(url, json=params, headers=headers)
    result = json.loads(resp.text) 
    return result 

def proverka(ids):
    token_qiwi = qiwi_p2p
    value=int(value)
    comment=str(comment)

    # billid = randint(1, 10000000000000000000000000)
    billid = "".join(random.choices(
        string.ascii_uppercase + string.digits + string.ascii_lowercase,
        k=20
    ))

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + token_qiwi,
        'content-type': 'application/json'

    }

    params={'amount': {'value': value, 
                       'currency': 'RUB',
                       },
            'comment': comment, 
            'expirationDateTime': '2022-04-13T14:30:00+03:00', 
            'customer': {}, 
            'customFields': {},        
            }


    url = f'https://api.qiwi.com/checkout-api/api/bill/search?statuses=READY_FOR_PAY&parameter=value'
    resp = requests.put(url, json=params, headers=headers)
    result = json.loads(resp.text) 
    return result 

def balance(login, api_access_token):
    s = requests.Session()
    s.headers['Accept']= 'application/json'
    s.headers['authorization'] = 'Bearer ' + api_access_token  
    b = s.get('https://edge.qiwi.com/funding-sources/v2/persons/' + login + '/accounts')
    return b.json()

def StopPythonScript(scriptName):
  cmd = [f'pkill -f .*python.*{scriptName}']
  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, 
  stderr=subprocess.PIPE)

def isRunningPythonScript(scriptName):
  cmd = [f'pgrep -f .*python.*{scriptName}']
  process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, 
  stderr=subprocess.PIPE)
  my_pid, err = process.communicate()

  if len(my_pid.splitlines()) >0:
    return True
  else:
    return False

def p_set(message):
  global ids
  ids = message.text
  bot.send_message(message.chat.id, "Сколько часов выдать?")
  bot.register_next_step_handler(message, p_set2)

  cursor.execute(f'UPDATE all_hel SET pod=? where id=?', (int(idss), int(ids)))
  conn.commit()

def ban_bot(message):
  ids = message.text
  cursor.execute(f"INSERT INTO ban VALUES ({ids})")
  conn.commit()
  bot.send_message(message.chat.id, "✅")

def unban_bot(message):
  ids = message.text
  cursor.execute(f"DELETE from ban where id = {ids}")
  conn.commit()
  bot.send_message(message.chat.id, "✅")


def prfix_set(message):
  pref = message.text
  m = message.from_user.id
  cursor.execute(f'UPDATE all_hel SET prefix=? where id=?', (pref, int(m)))
  conn.commit()
  bot.send_message(message.chat.id, "✅* Префикс успешно установлен! Перезагрузите бота если он был включён. *", parse_mode="Markdown")

def p_set2(message):
  idss = message.text

  cursor.execute(f'UPDATE all_hel SET pod=? where id=?', (int(idss), int(ids)))
  conn.commit()
  bot.send_message(message.chat.id, "✅")
  bot.send_message(int(ids), f"💫 Вам выдали premium на `{idss}`ч!", parse_mode="Markdown")


def rassilka(message):
  ids = message.text
  if ids == "None":
    bot.send_message(message.chat.id, "Окк")
  else:
    smog = 0
    erorr = 0

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="❌ Удалить", callback_data='del_msg')
    keyboard.add(key_yes)

    all = []
    for row in cursor.execute(f"SELECT * FROM all_hel;"):
      all.append(row)

    for row in all:
      try:
        bot.send_message(row[0], ids, reply_markup=keyboard, parse_mode="Markdown")
        smog += 1
      except:
        erorr += 1
    bot.send_message(message.chat.id, f"✅ Отправил: `{smog}`\n❎ Ошибки: `{erorr}`", parse_mode="Markdown")
def del_id(message):
  ids = message.text
  cursor.execute(f"DELETE from all_hel where id = {ids}")
  conn.commit()
  bot.send_message(message.chat.id, "✅")

def check_token(token):
  json = requests.get("https://discord.com/api/v9/users/@me/library", headers={"authorization": token})
  if json.status_code == 200:
    return True
  elif json.status_code == 401:
    return False
  elif json.status_code == 403:
    return None




    


if __name__ == '__main__':
  while True:
    try:
      print("[СТАРТ] Главный telegram bot запущен!")
      bot.polling(none_stop=True)
    except Exception as e:
      time.sleep(3)
      print(e)
      print("[СМЕРТЬ] Главный telegram bot умер")

