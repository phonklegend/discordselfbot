




import discord
from discord import channel
from discord.ext import commands, tasks
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/runner/TgSelf')
import bot


# =-=-=-==-=-=-=-==-=-==-=-=-=-=-= #
import sqlite3
conn = sqlite3.connect("Tg.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS all_hel(
  "id"  INT, 
  "token" TEXT, 
  "pod" INT,
  "name_self" TEXT,
  "prefix"  TEXT); 
""")
for row in cursor.execute(f"SELECT * FROM all_hel where id={id_tg_user}"):
  rows = row[1]
  pref = row[4]
token = rows
# =-=-=-==-=-=-=-==-=-==-=-=-=-=-= #


client = commands.Bot(command_prefix = pref, self_bot = True, intents=discord.Intents.all())

@client.event
async def on_ready():
  print(f"[СТАРТ] Self Bots \"{sys.argv[0]}\" запущен!")
  await client.change_presence(activity = discord.Streaming(name="Создано в @discordselfbot (telegram)", url="https://www.twitch.tv/forgottenxyz"))

@client.command(aliases = ['Ping', 'PING', 'pING', 'ping', 'Пинг', 'ПИНГ', 'пИНГ', 'пинг', 'Понг', 'ПОНГ', 'пОНГ', 'понг'])
#@client.command - объявление команды | (aliases = ['Ping', 'PING' ...]) - Альтернативное название команды
async def __ping(ctx): # Объявление асинхронной функции __ping с возможностью публикации сообщения
    message = await ctx.send('Пожалуйста, подождите. . .') # Переменная message с первоначальным сообщением
    ping = client.ws.latency # Получаем пинг клиента

    ping_emoji = '🟩🔳🔳🔳🔳' # Эмоция пинга, если он меньше 100ms

    if ping > 0.10000000000000000:
        ping_emoji = '🟧🟩🔳🔳🔳' # Эмоция пинга, если он больше 100ms

    if ping > 0.15000000000000000:
        ping_emoji = '🟥🟧🟩🔳🔳' # Эмоция пинга, если он больше 150ms

    if ping > 0.20000000000000000:
        ping_emoji = '🟥🟥🟧🟩🔳' # Эмоция пинга, если он больше 200ms

    if ping > 0.25000000000000000:
        ping_emoji = '🟥🟥🟥🟧🟩' # Эмоция пинга, если он больше 250ms

    if ping > 0.30000000000000000:
        ping_emoji = '🟥🟥🟥🟥🟧' # Эмоция пинга, если он больше 300ms

    if ping > 0.35000000000000000:
        ping_emoji = '🟥🟥🟥🟥🟥' # Эмоция пинга, если он больше 350ms

    
    await message.edit(content = f'Понг! {ping_emoji} `{ping * 1000:.0f}ms` :ping_pong:') # Редактирование первого сообщения на итоговое (на сам пинг)

try:
  client.run(token, bot =False)
except Exception as e:
  print(e)
  bot.sendd(id_tg_user, f"*⛔ ОШИБКА В БОТЕ:* {e}")

