import discord
import random
import os
import youtube_dl
from discord.ext import commands
from discord.utils import get
from discord import Game
from passlib.hash import cisco_type7
"""
if not discord.opus.is_loaded():
    discord.opus.load_opus('libopus.so')
"""
TOKEN_HASHED = "0628150819613D341C3A360814292028710507183B3D1D231A4F6E4E6B51403F4D1127737C5678044652027F37370C6125172F275024375E3469490A"
TOKEN = cisco_type7.decode(TOKEN_HASHED)
bot= commands.Bot(command_prefix='j!')
bot_client=discord.Client()
omedeto_count=0
totalorang={}
bokep_list=['https://cdn.discordapp.com/attachments/690904726295937054/723083523157655572/Screenshot_2020-06-18-14-55-35-85.jpg',
            'https://cdn.discordapp.com/attachments/690904726295937054/723083530472783932/Screenshot_2020-06-18-14-53-56-35.jpg',
           'https://media.discordapp.net/attachments/733526634677796884/739738067060916234/hitlerhead.jpg',
           'https://media.discordapp.net/attachments/733526634677796884/739738079664930836/IMG-20190606-WA0022.jpg?width=1194&height=671',
           'https://media.discordapp.net/attachments/733526634677796884/739738081476870214/WhatsApp_Image_2018-08-08_at_7.34.15_PM_2.jpeg?width=351&height=670',
           'https://media.discordapp.net/attachments/733526634677796884/739738082408136744/WhatsApp_Image_2018-07-02_at_7.14.55_PM.jpeg?width=378&height=671',
           'https://media.discordapp.net/attachments/733526634677796884/739738083058253874/WhatsApp_Image_2018-08-08_at_7.34.15_PM_3.jpeg?width=334&height=671',
           'https://media.discordapp.net/attachments/733526634677796884/739738085016731658/WhatsApp_Image_2019-07-28_at_17.34.05.jpeg?width=378&height=671',
           'https://media.discordapp.net/attachments/733526634677796884/739738087671857202/DW0mqcOW0AAhxsV.jpg?width=556&height=672',
           'https://media.discordapp.net/attachments/733526634677796884/739738088581890098/ARYA_BIMA_1.jpg?width=478&height=671',
           'https://media.discordapp.net/attachments/733526634677796884/739738191099068446/IMG-20170103-WA0008.jpg',
           'https://media.discordapp.net/attachments/733526634677796884/739738402143993886/Maskot_Full_Transparan.png?width=668&height=671'
           ]
torture_playlist=['https://www.youtube.com/watch?v=IRP-2y43BLo&t=12s',
                  'https://www.youtube.com/watch?v=Ds14zhfHEvE',
                  'https://www.youtube.com/watch?v=zteRyDYj86k',
                  'https://www.youtube.com/watch?v=NvztevMqaPU',
                  'https://www.youtube.com/watch?v=Q3E7L_RoyTU',
                  'https://www.youtube.com/watch?v=stlZEKoJg10',
                  'https://www.youtube.com/watch?v=8BQbd40XH2c',
                  'https://www.youtube.com/watch?v=3Hf4IAMUVBg&t=4s',
                  'https://www.youtube.com/watch?v=8uFHElblycA',
                  'https://www.youtube.com/watch?v=EjGKReJb7f4',
                  'https://www.youtube.com/watch?v=cv6a81Ulx-g',
                  'https://www.youtube.com/watch?v=iXuFHJJE1zE',
                  'https://www.youtube.com/watch?v=BTs5FS66IUI',
                  ]

myself=""
helmi=""
my_id=461150644422705152
warning_limit=5
warning_message=['ayo age terusno :v',
                 'alah mboh cok',
                 ':v',
                 'aku gaeruh kudu lapo. Aturanku ndek langgar :v',
                 'jembot.',
                 'ayo cooooooook terusnoooooooo!!!!',
                 'ayo ayo, :v.',
                 'taek',
                 'cok',
                 'Hmm.',
                 'Hmmmmmmmmmmm.']

character_exception=[]
cursed_emote=[":v",";v",":pac:"]
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
    global character_exception,cursed_emote
    text=text.lower()
    text=text.replace(" ","")
    for i in cursed_emote:
        if (i in text):
            return True
    return False

@bot.command(name='rules',
             description='rules bot',
             brief='rules bot')
async def rules(ctx):
    await ctx.channel.send('Freedom of speech.')

@bot.command(name='kacang',
             description='gunakan command ini dan sebut user yang mengacangi kamu',
             brief='gunakan ini kalau kamu dikacangi')
async def kacang(ctx, user:discord.Member):
    await ctx.channel.send('HE COK OJOK KACANG '+user.mention)

@bot.command(name='hello',
             description='menyapa bot.',
             brief='menyapa bot.',
             aliases=['halo','hallo','he'])
async def hello(ctx):
    await ctx.channel.send('Opo seh cok '+ctx.author.mention+', nyeluk-nyeluk ae.')

@bot.command(name='changelog',
             description='new features on this bot.',
             brief='bot update')
async def changelog(ctx):
    await ctx.channel.send('```-New hidden features.\n-New dialog.\n-Mbusek fitur seng isok ngirim message nang aku, vice versa.\n-New torture devices to play with.```')

@bot.command(name='register',
             description='khusus faray.',
             brief='khusus faray')
async def register(ctx):
    global myself,helmi
    if ctx.author.id==461150644422705152 or ctx.author.id==465801681565646858:
        if ctx.author.id==465801681565646858:
            helmi=ctx.guild.get_member(465801681565646858)
        else:
            myself=ctx.guild.get_member(461150644422705152)
        await ctx.channel.send("register success")
    else:
        await ctx.channel.send("sopo kon")

@bot.command(name='judgement')
async def judgement(ctx):
    if ctx.author.id==my_id:
        while True:
            await ctx.channel.send('JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK JANCOOOOOOK')
    else:
        ctx.channel.send('sopo kon')

#ADJUSTMENTS
@bot.command(name='setwarning')
async def setwarning(ctx,new_warning_limit):
    global warning_limit
    if ctx.author.id==my_id:
        warning_limit=int(new_warning_limit)
        await ctx.channel.send('Success')
    else:
        await ctx.channel.send('sopo kon')
@bot.command(name='characterexception',
             alliases=['ce'])
async def characterexception(ctx,character):
    global character_exception
    if ctx.author.id==my_id:
        character_exception.append(character)
        await ctx.channel.send('Success')
    else:
        await ctx.channel.send('sopo kon')
@bot.command(name='addbokep')
async def addbokep(ctx, url):
    global bokep_list
    bokep_list.append(url)
    await ctx.channel.send('Success')
@bot.command(name='addtorture')
async def addtorture(ctx,url):
    global torture_playlist
    torture_playlist.append(url)
    await ctx.channel.send('Success')
@bot.command(name='addcs',
             brief='add cursed emote',
             description='add cursed emote. Khusus faray')
async def addcs(ctx,text):
    global cursed_emote
    if ctx.author.id==my_id:
        cursed_emote.append(text)
        await ctx.channel.send('Success')
    else:
        ctx.channel.send('sopo kon.')
@bot.command(name='export')
async def export(ctx):
    global cursed_emote, torture_playlist, bokep_list
    if ctx.author.id==my_id:
        await myself.send("cursed_emote : "+str(cursed_emote))
        await myself.send("torture_playlist emote : "+str(torture_playlist))
        await myself.send("bokep_list : "+str(bokep_list))
    else:
        await ctx.channel.send("Sopo kon.")
    
#MUSIC BOT
@bot.command(name='join')
async def join(ctx):
    global voice
    channel=ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice=await channel.connect()
@bot.command(name='leave')
async def leave(ctx):
    global voice
    channel=ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        ctx.channel.send("shut the fuck up")
@bot.command(name='play')
async def play(ctx, url:str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music end or use the 'stop' command")
        return
    channel=ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet':True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice=await channel.connect()
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()

@bot.command(name='pause')
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        ctx.channel.send('Pausing song...')
        voice.pause()
    else:
        await ctx.channel.send('Im not playing anything you dumb cunt')
        
@bot.command(name='resume')
async def resume(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_paused():
        ctx.channel.send('Resuming song...')
        voice.resume()
    else:
        await ctx.channel.send('Im not pausing anything you dumb cunt')

@bot.command(name='stop')
async def stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        ctx.channel.send('Stopping song...')
        voice.stop()
    else:
        await ctx.channel.send('Im not playing anything you dumb cunt')


#TORTURE DEVICE
@bot.command(name='jancok')
async def jancok(ctx):
    url='https://www.youtube.com/watch?v=BB2DzglV2l0'
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music end or use the 'stop' command")
        return
    channel=ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice=await channel.connect()
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()

@bot.command(name='torture')
async def torture(ctx):
    global torture_playlist
    url=random.choice(torture_playlist)
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music end or use the 'stop' command")
        return
    channel=ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice=await channel.connect()
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()

@bot.command(description='mengobrol dengan bot.',
             brief='mengobrol dengan bot.')
async def ngobrol(ctx):
    possibles=['Awakmu pingin ngobrol a? Ngobrol ambek bot i.',
               'Penciptaku iki saking nolep e sampek aku dewe saaken. Padahal aku bot',
               'Kon weruh a lek kolorku werno ireng?',
               'Iwanttodie',
               'Biasane ndek kene ngobrol i wedok. Opo o e? Jomblo a kon',
               'Bagaimana kabarmu, sayang?',
               'Eternity;witch vol 2 when',
               'Sido a',
               'fuck this',
               'helmi kontol',
               'kon eruh lek arek TI UB iku OP a?',
               'ha?',
               'boma endi? kangen ak',
               'sopo?',
               'lapo?',
               'kapan?',
               'Aku tau krungu ndek kene onok pengguna Yanne 3 juta. Endi?',
               'coli teruussssss',
               'Endi sunardi?',
               ':v',
               'jancok lapo se ngejak ngobrol ak? Nggarai sumpek ae.',
               'Aku pengin curhat. Kesel aku dipermain o sebagai bot. Rulesku gak diregani blas. Cok encen',
               'Aku kok seneng ambek anak e pak lutfi :v',
               'kangen shaski. Oh wait, iku ojob e helmi ambek boma. :(',
               'sepurane aku suwe off, onok existensial crisis.',
               ]
    await ctx.channel.send(random.choice(possibles))

@bot.command(description='bokep.',
             brief='bokep.')
async def bokep(ctx):
    global bokep_list
    embed_msg=discord.Embed(title="Bokep", description=str(ctx.author.mention)+" sange.", color=0xFF0080)
    embed_msg.set_image(url=random.choice(bokep_list))
    embed_msg.set_author(name=bot.user.name)
    await ctx.channel.send(embed=embed_msg)
    
@bot.event
async def on_message(message):
    global bot,warning_limit,warning_message
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
        msg='Pingin tak kick a ndogmu'
        await message.channel.send(msg)

    elif cursed_emote_check(message.content):
        if message.author==bot.user:
            pass
        else:
            if totalorang.get(str(message.author),None)==None:
                totalorang.update({str(message.author):1})
            else:
                totalorang[str(message.author)]+=1
        if totalorang[str(message.author)]<warning_limit:
            msg=random.choice(warning_message)
        elif totalorang[str(message.author)]>=warning_limit:
            msg=random.choice(warning_message)
            target=message.guild.get_member(message.author.id)
            totalorang[str(message.author)]=0
            await target.kick(reason=None)
            
        await message.channel.send(msg)
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    if message.author==bot.user:
        pass
    else:
        global myself,helmi
        await message.channel.send(message.author.mention + ' ngebusek message')
        await myself.send(str(message.author)+' ngebusek message, content e :'+message.content)
        await helmi.send(str(message.author)+' ngebusek message, content e : '+message.content)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = Game("j!changelog | j!help")
    await bot.change_presence(activity=game)

bot.run(TOKEN)
