#bot.py
from pynput.keyboard import Key, Controller
import time
import random
import os #for importing env vars to the bot to use
from twitchio.ext import commands

keyboard = Controller()

bot=commands.Bot(
    #set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
    )

@bot.event
async def event_ready():
    'called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has venido!")

# bot.py, below event_ready
@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    #bot.py, in event_message, below the bot ignore stuffs
    await bot.handle_commands(ctx)
    
    # bot.py, in event_message, below the bot-ignoring stuff
    fouMsjRand=int(random.random()*10)
    if fouMsjRand==0 :
        await ctx.channel.send("FOU")
    elif fouMsjRand==1:
        await ctx.channel.send("Fou fou!")
    else:
        await ctx.channel.send("Comands are !1,!2,!3,!4,!5,!skip !attack !")
         

@bot.command(name='1')
async def test(ctx):
    await ctx.send('Carta #1!')
    keyboard.press('1')
    keyboard.release('1')
    time.sleep(0.12)

@bot.command(name='2')
async def test(ctx):
    await ctx.send('Carta #2!')
    keyboard.press('2')
    keyboard.release('2')
    time.sleep(0.12)
    
@bot.command(name='3')
async def test(ctx):
    await ctx.send('Carta #3!')
    keyboard.press('3')
    keyboard.release('3')
    time.sleep(0.12)
    
@bot.command(name='4')
async def test(ctx):
    await ctx.send('Carta #4!')
    keyboard.press('4')
    keyboard.release('4')
    time.sleep(0.12)

@bot.command(name='5')
async def test(ctx):
    await ctx.send('Carta #5!')
    keyboard.press('5')
    keyboard.release('5')
    time.sleep(0.12)

@bot.command(name='attack')
async def test(ctx):
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    await ctx.send('Ataque!') 

@bot.command(name='skip')
async def test(ctx):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press('4')
    keyboard.release('4')
    await ctx.send('Skipping!') 

#Arrastrar
@bot.command(name='up')
async def test(ctx):
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    await ctx.send('up!')
    
@bot.command(name='down')
async def test(ctx):
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    await ctx.send('down!')
    
@bot.command(name='right')
async def test(ctx):
    keyboard.press.key(Key.right)
    keyboard.release(Key.right)
    await ctx.send('right!')
    
@bot.command(name='left')
async def test(ctx):
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    await ctx.send('left!') 
    
if __name__ =="__main__":
    bot.run()
