import discord
import asyncio
import youtube_dl
from discord.ext import commands

TOKEN_DIS = "YOURE TOKEN"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='+', case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    print(f"""{bot.user} Bot has ben launched, have fan :) 
          \nif you want support me https://www.donationalerts.com/r/faltonik""")

@bot.command()
async def time(ctx, time):
    author = ctx.message.author
    try:
        minute = int(time[:-2])
        sec = time[2:]
        output = f'Время спавна рошана:\nобычная {minute + 8}:{sec} - {minute + 11}:{sec}\nтурбо - {minute + 5}:{sec}'
        await ctx.send(output)
        await asyncio.sleep(1)
        await ctx.send(f"{author.mention} Эгида распылится в {minute + 5}:{sec}")
        
        # Set the waiting time before the reminder
        await asyncio.sleep(15)
        
        await ctx.send(f"{author.mention} Эгида распылилась в {minute + 5}:{sec}")
        
        # Entering the voice channel and playing the sound
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
        source = discord.FFmpegPCMAudio("PATH TO sound.mp3",executable="PATH TO ffmpeg.exe  ") # if you do not have ffmpeg installed in your PATH environment variable, 
        # then specify the path to the ffmpeg.exe file in your code. otherwise leave \\\\\source = discord.FFmpegPCMAudio("PATH TO sound.mp3")/////


        voice_client.play(source)                                                                          
        await asyncio.sleep(15)  # Sound playing time                                            
        await voice_client.disconnect()
        
    except ValueError:
        output = 'Подумай головой:\nя не понимаю ваши эти "{time.upper()}", ты мне скажи 1700 и все'
        await ctx.send(output)
    except asyncio.TimeoutError:
        await ctx.send('Превышено время ожидания.')

@bot.command()
async def sos(ctx):
    await ctx.send("""\nКоманда +Time и время падения рошана без ":", покажет тайминг рошана.
После того как эгида упадет, в чат выведется время, когда она упала.""")

bot.run(TOKEN_DIS)