#EY3LE55² BOT 2018 

#IMPORT CHALK
from termcolor import colored


#IMPORT DISCORD
import discord
from discord.ext import commands
import asyncio
import random

#LOADS OPUS LIB
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')


bot = commands.Bot(command_prefix=';')

def prRed(skk): 
    print(colored(skk, 'red'))
def prGreen(skk): 
    print(colored(skk, 'green'))
def prYellow(skk): 
    print(colored(skk, 'yellow'))
def prCyan(skk): 
    print(colored(skk, 'cyan'))



#variables here
count = 0
eqcount = 0


#when ready (welcome message)
@bot.event
async def on_ready():
    #welcome message
    prGreen('\n// Thank you for using the EY3LE55 Discord Bot //\n\n')
    prCyan('Get ready for some sexy commands <3\nReady!\n\n')
    prYellow("My name is " + bot.user.name)
    prYellow("My ID is " + bot.user.id)
    prGreen('\n\n// Logs //\n')

    #starting values
    await bot.change_presence(game=discord.Game(name='with your mom.'))


#on message event
@bot.event
async def on_message(message):
    if not(message.content.startswith(';')):
        #global variables called here
        global count
        global eqcount

        #checks if message is not from bot
        if message.author != bot.user:

            #counts number of messages
            count += 1
            if count == 8:

                #EY3QUOTE Messages
                try:
                    with open("logs/EY3Q.txt", "r") as eyequotes:
                        eyequote_list = eyequotes.read().splitlines()
                        eyequote = eyequote_list[random.randint(0, len(eyequote_list)-1)]
                        await bot.send_message(message.channel, '```css\n' + eyequote + '\n```')
                        prYellow('Random EY3QUOTE Sent!')
                        prCyan('    "' + eyequote + '"\n')
                except:
                    prRed('No Message Found in EY3Q.txt\n')
                count = 0


        #logs messages from EY3LE55
        if message.author.id == '118038099187073032':
            eqcount +=1
            if eqcount == 5:
                try:
                    with open("logs/EY3Q.txt", "a") as equ:
                        equ.write(message.content + '\n')
                    prGreen('EY3QUOTE Logged!')
                    prCyan('    "' + message.content + '"\n')
                except:
                    prRed('Error Opening EY3Q.txt\n')
                eqcount = 0
    await bot.process_commands(message)

#command list

#says what are you gay in vc
@bot.command(pass_context=True)
async def gay(ctx):
    try:
        author = ctx.message.author
        voice_channel = author.voice_channel
        vc = await bot.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('audio/gay.mp3')
        player.start()
        prYellow('Gay Command')
        prCyan('    From // ' + str(ctx.message.author.id) + ' Nick // ' + str(ctx.message.author.nick)+ '\n    In // ' + str(ctx.message.author.server) + '\n')
        await asyncio.sleep(2)
        await vc.disconnect()
    except:
        prRed('Gay Command // Already in voice channel!\n')

#says I rip the skin
@bot.command(pass_context=True)
async def skin(ctx):
    try:
        author = ctx.message.author
        voice_channel = author.voice_channel
        vc = await bot.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('audio/skin.mp3')
        player.start()
        prYellow('Skin Command')
        prCyan('    From // ' + str(ctx.message.author.id) + ' Nick // ' + str(ctx.message.author.nick)+ '\n    In // ' + str(ctx.message.author.server) + '\n')
        await asyncio.sleep(6)
        await vc.disconnect()
    except: 
        prRed('Skin Command // Already in voice channel!\n')

#says im sorry
@bot.command(pass_context=True)
async def imsorry(ctx):
    try:
        author = ctx.message.author
        voice_channel = author.voice_channel
        vc = await bot.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('audio/imsorry.mp3')
        player.start()
        prYellow('Im Sorry Command')
        prCyan('    From // ' + str(ctx.message.author.id) + ' Nick // ' + str(ctx.message.author.nick)+ '\n    In // ' + str(ctx.message.author.server) + '\n')
        await asyncio.sleep(2)
        await vc.disconnect()
    except:
        prRed('Im Sorry Command // Already in voice channel!\n')

#says thats macabre
@bot.command(pass_context=True)
async def macabre(ctx):
    try:
        author = ctx.message.author
        voice_channel = author.voice_channel
        vc = await bot.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('audio/macabre.mp3')
        player.start()
        prYellow('Macabre Command')
        prCyan('    From // ' + str(ctx.message.author.id) + ' Nick // ' + str(ctx.message.author.nick)+ '\n    In // ' + str(ctx.message.author.server) + '\n')
        await asyncio.sleep(4)
        await vc.disconnect()
    except:
        prRed('Macabre Command // Already in voice channel!\n')

#omae wa mou shindeiru
@bot.command(pass_context=True)
async def nani(ctx):
    try:
        author = ctx.message.author
        voice_channel = author.voice_channel
        vc = await bot.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('audio/nani.mp3')
        player.start()
        prYellow('Nani Command')
        prCyan('    From // ' + str(ctx.message.author.id) + ' Nick // ' + str(ctx.message.author.nick)+ '\n    In // ' + str(ctx.message.author.server) + '\n')
        await asyncio.sleep(5)
        await vc.disconnect()
    except:
        prRed('Nani Command // Already in voice channel!\n')

#gimme the succ
@bot.command(pass_context=True)
async def succ(ctx):
    try:
        author = ctx.message.author
        voice_channel = author.voice_channel
        vc = await bot.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('audio/succ.mp3')
        player.start()
        prYellow('Succ Command')
        prCyan('    From // ' + str(ctx.message.author.id) + ' Nick // ' + str(ctx.message.author.nick)+ '\n    In // ' + str(ctx.message.author.server) + '\n')
        await asyncio.sleep(2)
        await vc.disconnect()
    except:
        prRed('Succ Command // Already in voice channel!\n')

#says its wednesday my dudes
@bot.command(pass_context=True)
async def wednesday(ctx):
    try:
        author = ctx.message.author
        voice_channel = author.voice_channel
        vc = await bot.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('audio/wednesday.mp3')
        player.start()
        prYellow('Wednesday Command')
        prCyan('    From // ' + str(ctx.message.author.id) + ' Nick // ' + str(ctx.message.author.nick)+ '\n    In // ' + str(ctx.message.author.server) + '\n')
        await asyncio.sleep(5)
        await vc.disconnect()
    except:
        prRed('Wednesday Command // Already in voice channel!\n')

#says again
@bot.command(pass_context=True)
async def again(ctx):
    try:
        author = ctx.message.author
        voice_channel = author.voice_channel
        vc = await bot.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('audio/again.mp3')
        player.start()
        prYellow('Again Command')
        prCyan('    From // ' + str(ctx.message.author.id) + ' Nick // ' + str(ctx.message.author.nick)+ '\n    In // ' + str(ctx.message.author.server) + '\n')
        await asyncio.sleep(4)
        await vc.disconnect()
    except:
        prRed('Again Command // Already in voice channel!\n')

#says m stain
@bot.command(pass_context=True)
async def mstain(ctx):
    try:
        author = ctx.message.author
        voice_channel = author.voice_channel
        vc = await bot.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('audio/stain.mp3')
        player.start()
        prYellow('M Stain Command')
        prCyan('    From // ' + str(ctx.message.author.id) + ' Nick // ' + str(ctx.message.author.nick)+ '\n    In // ' + str(ctx.message.author.server) + '\n')
        await asyncio.sleep(2)
        await vc.disconnect()
    except:
        prRed('M Stain Command // Already in voice channel!\n')

#says diabetic wolf
@bot.command(pass_context=True)
async def tdw(ctx):
    try:
        author = ctx.message.author
        voice_channel = author.voice_channel
        vc = await bot.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('audio/tdw.mp3')
        player.start()
        prYellow('TDW Command')
        prCyan('    From // ' + str(ctx.message.author.id) + ' Nick // ' + str(ctx.message.author.nick)+ '\n    In // ' + str(ctx.message.author.server) + '\n')
        await asyncio.sleep(2)
        await vc.disconnect()
    except:
        prRed('TDW Command // Already in voice channel!\n')

#help command
@bot.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(description="Command List", color=0x00ff00)
    embed.set_author(name='EY3LE55² BOT', icon_url='https://i.imgur.com/8Z4GVQ0.jpg')

    embed.add_field(name="**;gay**", value="*:gay_pride_flag: VC Command - What are you f*cking gay?!*", inline=False)
    embed.add_field(name="**;skin**", value="*:eggplant: VC Command - I rip the skin*", inline=False)
    embed.add_field(name="**;imsorry**", value="*:cry: VC Command - Oh sh*t I'm sorry*", inline=False)
    embed.add_field(name="**;macabre**", value="*:thinking: VC Command - I can't believe this story...*", inline=False)
    embed.add_field(name="**;nani**", value="*:open_mouth: VC Command - NANI?!*", inline=False)
    embed.add_field(name="**;succ**", value="*:sweat_drops: VC Command - Succ!*", inline=False)
    embed.add_field(name="**;wednesday**", value="*:regional_indicator_w: VC Command - It's Wednesday my dudes*", inline=False)
    embed.add_field(name="**;again**", value="*:weary: VC Command - Agaaaaaain*", inline=False)
    embed.add_field(name="**;mstain**", value="*:poop: VC Command - No the one with the stain on them*", inline=False)
    embed.add_field(name="**;tdw**", value="*:wolf: VC Command - The Diabetic Wolf*", inline=False)

    embed.set_footer(text="Discord Bot Created by @EY3LE55#9291")

    await bot.send_message(ctx.message.channel, embed=embed)
    prYellow('Help Command')
    prCyan('    From // ' + str(ctx.message.author.id) + ' Nick // ' + str(ctx.message.author.nick)+ '\n    In // ' + str(ctx.message.author.server) + '\n')

bot.run('MzI3NTU2MTM4ODM5MDQ4MjA0.DSg5FQ.2QocHvBNAkCzDov8xWGxJxyaJfg')