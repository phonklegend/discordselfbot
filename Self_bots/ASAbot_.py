

import asyncio
import discord
from discord.ext import commands
from random import randint
import time
import requests as rq
import os
import random
from random import choice
import discord
from discord.ext import commands
from random import randint
import time
import requests as rq
import os
import random
from random import choice

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/runner/TgSelf')
import bot

# =-=-=-==-=-=-=-==-=-==-=-=-=-=-= #
import sqlite3, sys
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
tkn = rows
prefix = pref
# =-=-=-==-=-=-=-==-=-==-=-=-=-=-= #


# импортируем важные библы
crashed = []
v = 'v0.1b'


client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), self_bot=True)
# создаем переменную бота
client.remove_command('help')


global spam
spam = True



@client.event
async def on_ready():
  print(f'[СТАРТ] Self Bots \"{sys.argv[0]}\" запущен!')
  await client.change_presence(status=discord.Status.online)



@client.command()
async def help(ctx):
    await ctx.send(f"♥️ Self bot by ASAPok (remade) ♥️\n\n`{prefix}help_mod` - команды модерации \n`{prefix}help_crash` - команды для краша, рейда и т.д.\n`{prefix}help_status` - команды красивого статуса\n`{prefix}help_fun` - команды весёлости и развлечения.\n")
      

@client.command()
async def help_mod(ctx):
    await ctx.send(f' Команды модерации\n\n `>ban [участник] [причину]` - что бы выдать бан  \n `kick [участник] [причину]` - что бы кикать \n `>clear [количество]`- чтобы очистить канал от сообщений')


@client.command()
async def help_status(ctx):
    await ctx.send(f'Команды красивого статуса\n\n`>status stream [название]` - стрим статус\n`>status watch [название]` - статус смотрит \n `>status listen [название]` - статус слушает \n`>status play [название]` - статус играет')


@client.command()
async def help_fun(ctx):
    await ctx.send(f'Команды весёлости и развлечения.\n\n`>poxui` - что бы узнать текст песни SSaSke Нарезки, iiRN, 5opka - Какая разница \n`>calculator [число 1 (+,-,*,:) число 2` - что бы считать\n`>avatar [айди или пинг]` - что бы узнать аватарку\n`>say [текст]` - что бы отправить сообщение в виде эмбед\n`>echo [текст]` - что бы отправить эмбед с рандомным цветом\n`>ping` - что бы узнать задержку сэлф-бота\n`>popit` - что бы отправить в чат ПоПиТ\n`>ball [вопрос]` - что бы задать вопрос шару\n')


@client.command()
async def help_crash(ctx):
    await ctx.send(f'Команды команды для краша, рейда и т.д.\n\n`>create_guild [название]` - что бы создать новый сервер\n`>delguild` - что бы удалить сервер\n`>crash` - что бы наверное крашить\n`>hack` - что бы скопировать сервер\n`>spam [текст]` - что бы спамить без остановки (>stop что бы остановить)\n`>spamv2 [количество] [текст]` - что бы спамить обход большинство анти спам систем\n`>killchat [количество]` - что бы убить чат\n`>autoraid` - автоматический рейд')

@client.command()
async def ban(ctx, member: discord.Member, *, reason="без причины.",):
    if type(member) == discord.Member:
        await ctx.guild.ban(member, reason=reason, delete_message_days=0)
    else:
        await ctx.guild.ban(
            discord.Object(member), reason=reason, delete_message_days=0
        )
    await ctx.send(f'**Модерация**\n\nУчастник {member.mention} был забанен\nПричина: {reason}')


@client.command()
async def kick(ctx, member: discord.Member, *, reason="без причины.",):
    if type(member) == discord.Member:
        await ctx.guild.kick(member, reason=reason)
    else:
        await ctx.guild.kick(
            discord.Object(member), reason=reason 
        )
    await ctx.send(f'**Модерация**\n\nУчастник {member.mention} был кикнут\nПричина: {reason}')
    

@client.command()
async def say(ctx, *, text=''):
    if text == '':
        msg = await ctx.send(f'Укажите текст!')
        time.sleep(1)
        await msg.delete()
        await ctx.message.delete()
    else:
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(description=text))

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, purge: int):
    await ctx.channel.purge(limit=purge)
    await ctx.send(f'Очистка сообщений💬\n\n✅Было очищено {purge} сообщений')


@client.command()
async def calculator(ctx, number1, znak, number2):
    result = 0
    if znak == '+':
       result = int(number1) + int(number2)
    elif znak == '-':
       result = int(number1) - int(number2)
    elif znak == ':':
       result = int(number1) / int(number2)
    elif znak == '*':
       result = int(number1) * int(number2)
    await ctx.send(f'💻Калькулятор\n\nОтвет: {result}')

@client.command()
async def ping(ctx): # Объявление асинхронной функции __ping с возможностью публикации сообщения
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

    message = await ctx.send('Пожалуйста, подождите. . .') # Переменная message с первоначальным сообщением
    await message.edit(content = f'Понг! {ping_emoji} `{ping * 1000:.0f}ms` :ping_pong:') # Редактирование первого сообщения на итоговое (на сам пинг)

@client.command()
async def create_guild(ctx, *, nameg='@discordselfbot guild'):
    new = await client.create_guild(name=nameg)
    listc = await new.fetch_channels()
    for c in listc:
        await c.delete()

    await new.create_text_channel('made-by-discordselfbot')

    embed = discord.Embed(
        title = 'Готово :white_check_mark:',
        description = f'Был создан сервер {nameg}',
        colour = discord.Colour.from_rgb(randint(0,255), randint(0,255), randint(0,255))
    )
    await ctx.send(embed=embed)

@client.command()
async def delchannel(ctx):
  for c in ctx.guild.channels:
        try:
            await c.delete()
        except:
             pass
  for c in ctx.guild.channels:
        try:
            await c.create('test')
        except:
            pass


@client.command()
async def crash(ctx):
    await ctx.guild.edit(name='Crashed by @discordselfbot')
    for r in ctx.guild.roles:
        try:
            await r.delete()
        except:
            pass

    for c in ctx.guild.channels:
        try:
            await c.delete()
        except:
            pass

    for i in range(50):
        await ctx.guild.create_role(name='Crash By @discordselfbot')
        ch = await ctx.guild.create_text_channel('crash-by-discordselfbot')
        await ch.create_webhook(name='crash4d')

@client.event
async def on_guild_channel_create(channel):
    if channel.name == 'crash-by-discordselfbot':
        for i in range(100):
            hooks = await channel.webhooks()
            for hook in hooks:
                await hook.send('@everyone @here Данный сервер крашится селф-ботом @discordselfbot')


@client.command()
async def delguild(ctx):
    try:
        await ctx.guild.delete()
    except Exception as e:
        embed = discord.Embed(
            title = 'Ошибка :x:',
            description = f'Произошла ошибка при удалении сервера | `{e}`',
            colour = discord.Colour.from_rgb(133,228,61)
        )
        await ctx.send(embed=embed)

@client.command()
async def spam(ctx, *, text=None):
    embederr = discord.Embed(
        title = 'Ошибка :x:',
        description = 'Укажите текст спама!',
        colour = discord.Colour.from_rgb(228,0,111)
    )
    embed = discord.Embed(
        title = 'Успешно :white_check_mark:',
        description = 'Спам запущен! Для остановки напишите >stop',
        colour = discord.Colour.from_rgb(228,0,111)
    )
    if text == None:
        await ctx.send(embed=embederr)
    else:
        global spam
        spam = True
        while spam == True:
            await ctx.send(text)

@client.command()
async def stop(ctx):
    global spam
    spam = False
    await ctx.message.add_reaction('✅')

@client.command()
async def spamv2(ctx, num=0, *, text=''):
    if num == 0 or text in ['']:
        await ctx.send('Правильное использование команды: `>spamv2 [кол-во сообщений] [текст]`')
    else:
        for spam in range(int(num)):
            await ctx.send(f'{text}\n||{randint(0,1000000000)}||')

@client.command()
async def killchat(ctx, count=5):
    for i in range(int(count)):
        text = f'||{randint(0,1918177181)}|| die...:hot_face: :hot_face: \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ndie...:hot_face: :hot_face:'
        await ctx.send(text)
    await ctx.message.delete()

async def sendhook(ctx, channelm):
        for i in range(100):
            hooks = await channelm.webhooks()
            for hook in hooks:
                await hook.send('@everyone @here raid by @discordselfbot')

@client.command()
async def autoraid(ctx):
    await ctx.message.delete()
    for i in range(6):
        text = f'{randint(0,999)} | Raid by @discordselfbot ! @everyone @here\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n||{randint(0,1338)}||'
        await ctx.send(text)
    for c in ctx.guild.text_channels:
        try:
            await c.create_webhook(name='Raid By @discordselfbot')
        except Exception as e:
            print(e)

    try:
            for c in ctx.guild.text_channels:
                asyncio.create_task(sendhook(ctx, channelm=c))
                hooks = await c.webhooks()
                for hook in hooks:
                    await hook.send(f'{randint(0,999)} | Raid by @discordselfbot @everyone @here')
    except Exception as e:
            print(e)

    for c in ctx.guild.text_channels:
        try:
            await c.send(f'{randint(0,999)} | Raid by @discordselfbot! @everyone @here\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n||{randint(0,1338)}||')
        except:
            pass

@client.command()
async def status(ctx, arg='', *, names=''):
    bll = [''] # не смейтесь ебать, просто not == '' не работало, а искать решение лень
    if arg == 'stream' and names not in bll:
        await client.change_presence(activity = discord.Streaming(name=names, url="https://www.twitch.tv/asap_ok"))
        await ctx.message.add_reaction('✅')
    elif arg == 'watch' and names not in bll:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=names))
        await ctx.message.add_reaction('✅')
    elif arg == 'listen' and names not in bll:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=names))
        await ctx.message.add_reaction('✅')
    elif arg == 'play' and names not in bll:
        await client.change_presence(activity=discord.Game(name=names))
        await ctx.message.add_reaction('✅')
    

#cтарый код матвея, досихпор работает

@client.command()
async def python(ctx, *, code):
  msg = await ctx.send(":white_check_mark: Выполняю ваш код...")
  time.sleep(1)
  
  await msg.edit(content=f'Подключение к серверу 57%')
  time.sleep(1)
  await msg.edit(content=f'Подключение к серверу 97%')
  time.sleep(1)
  await msg.edit(content=f'Подключён!') 

  time.sleep(2)
  await msg.edit(content=f'Код успешно выполнен! :white_check_mark:\nЯзык: `Python`\nОшибок: `0`\nСам код:\n```py\n{code}```')

@client.command()
async def edit(ctx, amount = int(0), *, text: str):
        channel = ctx.channel
        await ctx.send(":white_check_mark: Начинаю редактирование сообщений!")

        async for message in channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.edit(content=text)
            except:
                pass




@client.command()
async def popit(ctx):
    await ctx.send(f'Поп-ит\n\n||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||\n||:blue_square:|| ||:blue_square:|| ||:blue_square:|| ||:blue_square:|| ||:blue_square:||\n||:green_square:|| ||:green_square:|| ||:green_square:|| ||:green_square:|| ||:green_square:||\n||:red_square:|| ||:red_square:|| ||:red_square:|| ||:red_square:|| ||:red_square:||\n||:yellow_square:|| ||:yellow_square:|| ||:yellow_square:|| ||:yellow_square:|| ||:yellow_square:||')
  
@client.command()
async def ball(ctx, *, question):
    answers = ['Конечно же да :ok_hand:', 'Я считаю, что нет :x:', 'Весьма сомнительно, но правда :astonished:', 'Конечно же нет! :poop:', 'Шар не знает что на это ответить :robot:', 'Очень крутой вопрос, я его не понял :grin:']
    answer = random.choice(answers)
    msg = await ctx.send('Шар == говнище залупа пенис хер давалка :timer:\n\nЯ думаю, что ответить на `{question}`...')
    time.sleep(1.5)
    msg = await msg.edit('Шар ответил на ваш вопрос :magic_wand:\n\nОтвет: {answer}')

@client.command()
async def poxui(ctx):
    await ctx.send(f'Текст песни SSaSke Нарезки, iiRN, 5opka - Какая разница\n\n```Ахуеть как же мне пох*й бл*ть\nКакая нах*й разница\nЁбанный наср*л блять\nИрн\n\nАхуеть как пох*й бл*ть\nКакая нах*й разница\nЁбанный наср*л сука\nЁб твою мать бл*ть\n\nЁбанный *бать\nАхуеть как пох*й бл*ть\nКакая нах*й разница\nЁбанный наср*ть сука\n\nВсё за*бал бл*ть\nЁбанный *бать```')

@client.command()
async def hack(ctx):
    if not ctx.guild: return
    timel = time.time()
    guild = ctx.guild
    msglog=ctx.message
    new_guild = await client.create_guild(name=guild.name)
    for channel in new_guild.channels:
        try:
            await channel.delete()
        except:
            pass
    await msglog.edit(content=f'Создан сервер с именем {guild.name}, начинаю создание ролей')
    roles = {}
    r = guild.roles
    r.reverse()
    for role in r:
        if role.is_bot_managed() or role.is_default() or role.is_integration() or role.is_premium_subscriber(): continue
        new_role=await new_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
        roles[role] = new_role
    everyone = guild.default_role
    roles[everyone] = new_guild.default_role
    await new_guild.default_role.edit(permissions=everyone.permissions, color=everyone.color, hoist=everyone.hoist, mentionable=everyone.mentionable)
    await msglog.edit(content=f'Создание ролей завершено, начинаю создание каналов')
    for dc in await new_guild.fetch_channels():
        await dc.delete()
    channels = {None: None}
    for cat in guild.categories:
        new_c = await new_guild.create_category(name=cat.name, position=cat.position)
        channels[cat] = new_c
    for catt in guild.by_category():
        cat = catt[0]
        chs = catt[1]
        if cat != None:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=channels[c.category], position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                channels[c] = new_c
        else:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=None, position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                channels[c] = new_c
    await msglog.edit(content=f'Создание каналов завершено, начинаю настройку оверврайтов')
    for c in guild.channels:
        overs = c.overwrites
        over_new = {}
        for target,over in overs.items():
            if isinstance(target, discord.Role):
                try:
                    over_new[roles[target]] = over
                except:
                    pass
        await channels[c].edit(overwrites=over_new)
    await new_guild.edit(verification_level=guild.verification_level, default_notifications=guild.default_notifications, explicit_content_filter=guild.explicit_content_filter, system_channel=channels[guild.system_channel], system_channel_flags=guild.system_channel_flags, afk_channel=channels[guild.afk_channel], afk_timeout=guild.afk_timeout)#это не оверврайт, но лучше его делать перед эмодзи
    await msglog.edit(content=f'Настройка оверврайтов завершена, начинаю создание эмодзи...')
    countem = 0
    for emoji in guild.emojis:
        try:
            if int(countem) == 50:
                break
            else:
                url = f'https://cdn.discordapp.com/emojis/{emoji.id}.{"gif" if emoji.animated else "png"}'
                await new_guild.create_custom_emoji(name=emoji.name, image=rq.get(url).content)
                countem +=1
        except:
            print('не могу скопировать эмодзю')
            break
    times = int(time.time() - timel)
    await msglog.edit(content=f'Завершено клонирование сервера. Операция заняла {times} сек.')



try:
  client.run(tkn, bot =False)
except Exception as e:
  print(e)
  bot.sendd(id_tg_user, f"*⛔ ОШИБКА В БОТЕ:* {e}")
  