from discord.ext import commands
import discord
import json
from passlib.hash import cisco_type7

TOKEN_HASHED = "0628150819613D341C3A360814292028710507183B3D1D231A4F6E4E6B51403F4D1127737C5678044652027F37370C6125172F275024375E3469490A"
TOKEN = cisco_type7.decode(TOKEN_HASHED)
bot= commands.Bot(command_prefix='#')
bot_client=discord.Client()
omedeto_count=0
class MauBanOrang():
    def __init__(self,name=None,warning=None):
        self.name=name
        self.warning=warning
orang=MauBanOrang()

def omedeto_spelling_check(text):
    i=0
    text=text.lower()
    char='omedeto'
    text_array=[]
    #convert string to array
    for j in range(len(text)):
        text_array.append(text[j])
    if text=='omedeto':
        return [True, True] #First value : True that it contains 'omedeto'; second value: True if its typed correctly
    limit=len(text_array)
    while (i<limit):
        if text_array[i]!=char[i] and i>0: #If different, checks if the char is repeated
            if text_array[i]==char[i-1]:
                text_array.pop(i)
                limit-=1
            else:
                return [False,None] #Its not omedeto
        else:
            i+=1
    text=""
    for j in range(len(text_array)):
        text+=text_array[j]
    if text=="omedeto":
        return [True,False] #First value : True that it contains 'omedeto'; second value: True if its typed correctly
    else:
        return [False,None]
def cursed_emote_check(text):
    text=text.lower()
    text=text.replace(" ","")
    for i in range (len(text)-1):
        if (text[i]==":" and text[i+1]=="v") or ((text[i]==":" or text[i]=="v") and (text[i+1]==":" or text[i+1]=="v")):
            return True
    return False

@bot.command()
async def rules(ctx):
    await ctx.channel.send('No \':v\' emote. You can go fuck yourself. 5 kali ngono deloken engkok.')
@bot.command()
async def hello(ctx):
    await ctx.channel.send('Opo seh cok '+ctx.author.mention+', nyeluk-nyeluk ae.')

@bot.event
async def on_message(message):
    global bot
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    elif (omedeto_spelling_check(message.content)[0]):
        global omedeto_count
        if not (omedeto_spelling_check(message.content)[1]):
            msg='Ngetik \'omedeto\' seng nggenah titik a cok.'
            omedeto_count=0
        else:
            omedeto_count+=1
            if omedeto_count==3:
                msg='Jancok terusno ae \'omedeto\''
                omedeto_count=0
            else:
                msg='omedeto'
        await message.channel.send(msg)

    elif message.content.startswith('a!ban'):
        msg='Kon lek pingin main kick-kick an kene ambek aku. Tak kick ndogmu sampek pejumu bocor.'
        await message.channel.send(msg)

    elif cursed_emote_check(message.content):
        if orang.name!=message.author:
            orang.name=message.author
            orang.warning=1
        else:
            orang.warning+=1
        if orang.warning==1:
            msg='Ojok nggawe emot \':v\' iku jancok. Cringe bangsat.'
        elif orang.warning==2:
            msg='Loh nggawe \':v\' maneh i.'
        elif orang.warning==3:
            msg='loh diterusno nggawe \':v\'. Karepmu opo cok.'
        elif orang.warning==4:
            msg='Ayo age terusno.'
        elif orang.warning>=5:
            msg='Ayo terusno kene jancoook.'
            target=message.guild.get_member(message.author.id)
            orang.warning=0
            await message.channel.send(msg)
            await target.kick(reason=None)
        if orang.warning!=5:
            await message.channel.send(msg)
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    if message.author==bot.user:
        await message.channel.send(message.content)
    else:
        await message.channel.send(message.author.mention + ' ngebusek message')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)
