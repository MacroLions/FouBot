#bot.py
from pynput.keyboard import Key, Controller
import time
import random
import os #for importing env vars to the bot to use
from twitchio.ext import commands
import time


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
#fou fou kyu
#    fouMsjRand=int(random.random()*10)
#    if fouMsjRand==0 :
#        await ctx.channel.send("FOU")
#    elif fouMsjRand==1:
#        await ctx.channel.send("Fou fou!")
#    else:
#        await ctx.channel.send("Fou fou kyu!")
         

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
    await ctx.send('Skipping!') 

@bot.command(name='close')
async def test(ctx):
    keyboard.press('}')
    keyboard.release('}')
    await ctx.send('Closing!') 

@bot.command(name='cs')
async def test(ctx):
    keyboard.press('¿')
    keyboard.release('¿')
    await ctx.send('Command Spells!')

@bot.command(name='bm')
async def test(ctx):
    keyboard.press('0')
    keyboard.release('0')
    await ctx.send('Battle menu!') 

#Arrastrar
@bot.command(name='up')
async def test(ctx):
    keyboard.press(Key.up)
    time.sleep(0.6)
    keyboard.release(Key.up)
    await ctx.send('up!')
    
@bot.command(name='down')
async def test(ctx):
    keyboard.press(Key.down)
    time.sleep(0.6)
    keyboard.release(Key.down)
    await ctx.send('down!')
    
@bot.command(name='right')
async def test(ctx):
    keyboard.press(Key.right)
    time.sleep(0.6)
    keyboard.release(Key.right)
    await ctx.send('right!')
    
@bot.command(name='left')
async def test(ctx):
    keyboard.press(Key.left)
    time.sleep(0.6)
    keyboard.release(Key.left)
    await ctx.send('left!')

#NPs

@bot.command(name='np1')
async def test(ctx):
    keyboard.press('q')
    keyboard.release('q')
    await ctx.send('np1!')
    
@bot.command(name='np2')
async def test(ctx):
    keyboard.press('w')
    keyboard.release('w')
    await ctx.send('np2!')
    
@bot.command(name='np3')
async def test(ctx):
    keyboard.press('e')
    keyboard.release('e')
    await ctx.send('np3!')


#Y&N
@bot.command(name='y')
async def test(ctx):
    keyboard.press('y')
    keyboard.release('y')
    await ctx.send('yes!')

#n is f por posición    
@bot.command(name='n')
async def test(ctx):
    keyboard.press('f')
    keyboard.release('f')
    await ctx.send('no!')
    
#skills
    
#Servant 1
@bot.command(name='a1')
async def test(ctx):
    keyboard.press('a')
    keyboard.release('a')
    await ctx.send('Servant A Skill 1!')
    
@bot.command(name='a2')
async def test(ctx):
    keyboard.press('s')
    keyboard.release('s')
    await ctx.send('Servant A Skill 2!')
    
@bot.command(name='a3')
async def test(ctx):
    keyboard.press('d')
    keyboard.release('d')
    await ctx.send('Servant A Skill 3!')

#Servant 2
@bot.command(name='b1')
async def test(ctx):
    keyboard.press('f')
    keyboard.release('f')
    await ctx.send('Servant B Skill 1!')
    
@bot.command(name='b2')
async def test(ctx):
    keyboard.press('g')
    keyboard.release('g')
    await ctx.send('Servant B Skill 2!')
    
@bot.command(name='b3')
async def test(ctx):
    keyboard.press('h')
    keyboard.release('h')
    await ctx.send('Servant B Skill 3!')

#Servant 3
@bot.command(name='c1')
async def test(ctx):
    keyboard.press('j')
    keyboard.release('j')
    await ctx.send('Servant C Skill 1!')
    
@bot.command(name='c2')
async def test(ctx):
    keyboard.press('k')
    keyboard.release('k')
    await ctx.send('Servant C Skill 2!')
    
@bot.command(name='c3')
async def test(ctx):
    keyboard.press('l')
    keyboard.release('l')
    await ctx.send('Servant C Skill 3!')

#Master
@bot.command(name='m')
async def test(ctx):
    keyboard.press('m')
    keyboard.release('m')
    await ctx.send('Master skill menu open!')
        
@bot.command(name='m1')
async def test(ctx):
    keyboard.press('i')
    keyboard.release('i')
    await ctx.send('Master Skill 1!')
    
@bot.command(name='m2')
async def test(ctx):
    keyboard.press('o')
    keyboard.release('o')
    await ctx.send('Master Skill 2!')
    
@bot.command(name='m3')
async def test(ctx):
    keyboard.press('p')
    keyboard.release('p')
    await ctx.send('Master Skill 3!')

#Menu Principal
@bot.command(name='a')
async def test(ctx):
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    await ctx.send('Menu Option 1!')
    
@bot.command(name='b')
async def test(ctx):
    keyboard.press(Key.f2)
    keyboard.release(Key.f2)
    await ctx.send('Menu Option 2!')
    
@bot.command(name='c')
async def test(ctx):
    keyboard.press(Key.f3)
    keyboard.release(Key.f3)
    await ctx.send('Menu Option 3!')
    
@bot.command(name='d')
async def test(ctx):
    keyboard.press(Key.f4)
    keyboard.release(Key.f4)
    await ctx.send('Menu Option 4!')
    
@bot.command(name='e') 
async def test(ctx):
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)
    await ctx.send('Menu Option 5!')
    
@bot.command(name='f') 
async def test(ctx):
    keyboard.press(Key.f6)
    keyboard.release(Key.f6)
    await ctx.send('Menu Option 6!')

@bot.command(name='id') 
async def test(ctx):
    await ctx.send('132,384,577!')

@bot.command(name='sq') 
async def test(ctx):
    keyboard.press('e')
    keyboard.release('e')
    await ctx.send('Saint Quartz!')

#zoom
@bot.command(name='zoom') 
async def test(ctx):
    keyboard.press('+')
    time.sleep(0.2)
    keyboard.release('+')
    await ctx.send('Zoom!')

@bot.command(name='reduce') 
async def test(ctx):
    keyboard.press('-')
    time.sleep(0.2)
    keyboard.release('-')
    await ctx.send('reduce!')


#class supp
@bot.command(name='all') 
async def test(ctx):
    keyboard.press('z')
    keyboard.release('z')
    await ctx.send('all!')

@bot.command(name='saber') 
async def test(ctx):
    keyboard.press('x')
    keyboard.release('x')
    await ctx.send('saber!')

@bot.command(name='archer') 
async def test(ctx):
    keyboard.press('c')
    keyboard.release('c')
    await ctx.send('archer!')

@bot.command(name='lancer') 
async def test(ctx):
    keyboard.press('v')
    keyboard.release('v')
    await ctx.send('lancer!')


@bot.command(name='rider') 
async def test(ctx):
    keyboard.press('b')
    keyboard.release('b')
    await ctx.send('rider!')

@bot.command(name='caster') 
async def test(ctx):
    keyboard.press('n')
    keyboard.release('n')
    await ctx.send('caster!')

@bot.command(name='assassin') 
async def test(ctx):
    keyboard.press(',')
    keyboard.release(',')
    await ctx.send('assassin!')
    
@bot.command(name='berserker') 
async def test(ctx):
    keyboard.press('.')
    keyboard.release('.')
    await ctx.send('berserker!')

@bot.command(name='extra') 
async def test(ctx):
    keyboard.press('{')
    keyboard.release('{')
    await ctx.send('extra')

    
if __name__ =="__main__":
    bot.run()
