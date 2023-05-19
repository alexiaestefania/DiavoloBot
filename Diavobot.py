
# this could most definitely use improvements on code, i have to refactor it when i've got the time to make it more efficient.    
# much of the code is carried over from its first iteration and as such its very much not optimal
# that said, its just a simple bot that responds to messages on discord giving mostly random answers from a pool
# hopefully it is useful for anyone looking to make such a bot for their discord server
# i do NOT own the character diavolo from jojos bizarre adventure, he is the intellectual property of hirohiko araki  
# this bot is a parody of aid character and nothing more.                                                              
#------------------------------------------------------------------------------------------------------------------

import asyncio
import random
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'The boss himself, {client.user}, is online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#---------------------generic responses that dont depend on user     

    if 'square' in message.content.lower() and 'dopp' in message.content.lower():
        Rflat = ["don't mock my sweet flat doppio...", "please stop making fun of my doppio's box", "how dare you mock my epic minecraft king doppio...", "that's where he keeps his pizza"]
        await message.channel.send(random.choice(Rflat))
        
    if message.content.lower() == 'king' or message.content.lower() == 'king..' or message.content.lower() == 'king...' or message.content.lower() == 'king....':
        await message.add_reaction('💕')
        await message.add_reaction('😘')
        await message.add_reaction('😏')
        await message.add_reaction('💋')
    
    
    if 'giorno' in message.content.lower():
        Rgios = ["god i fucking hate giorno giovanna", "How dare you mention that kid in my presence!!!", "Stop. Talking. About. Giorno. Giovanna."]
        await message.channel.send(random.choice(Rgios))
    
    if 'diavolo death' in message.content.lower() or 'death loop' in message.content.lower():
        Rdie = ["how DARE you mock my fate....", "Don't. Just don't.", "hey can we not talk about me dying for once. it's not exactly my favorite subject.", "well how would YOU like being in a death loop"]
        await message.channel.send(random.choice(Rdie))
        
    if 'crimson' in message.content.lower() or 'stop time' in message.content.lower() or 'stand' in message.content.lower() or 'erase time' in message.content.lower():
        Rkc = ["https://www.youtube.com/watch?v=5mniWyVzGyQ", "KORE GA... WAGA [KING CRIMSON] NO NOURYOKU! https://64.media.tumblr.com/38991ff1ebc2dd6caf36e1fa6aa28196/tumblr_inline_mqnfs9DhCP1qz4rgp.gif", "https://www.youtube.com/watch?v=yKtCpi6A60U", "King Crimson, play 21st Century Schizoid Man. Thanks", "KING CRIMSON!", "KING CRIMSON! I erased time and leapt past it!" ,"Once anyone witnesses King Crimson... As of that moment... They no longer exist in this world.", "KING CRIMSON! Aside from me, all time is erased from the world!"]
        await message.channel.send(random.choice(Rkc))        

    if 'diavolo' in message.content.lower() and 'cringe' in message.content.lower():
        Rcring = ["YOU are cringe.", "I am not ''cringe''", "i am VALID you fool", "YOU are going in my cringe compilation and doppio will post it on his twitter."]
        await message.channel.send(random.choice(Rcring))

    if 'wig' in message.content.lower():
        Rwig = ["Wig!", "https://i.imgflip.com/4d4420.jpg", "https://i.imgflip.com/4d443q.jpg", "Wig flew off, with the lice and all", "https://i.imgflip.com/4d44di.jpg"]
        await message.channel.send(random.choice(Rwig))    
    
    if 'diavolo' in message.content.lower() and ('problematic' in message.content.lower() or 'callout' in message.content.lower() or 'call out' in message.content.lower()):
        Rcout = ["i will actually doxx you if you so much as start typing a callout for me", "if you call me out... i swear i will end you", "quick, doppio! write the callout before they can ruin my reputation!", "my darling doppio is compiling a google docs with all of your problematic posts. you're going down", "my sweet doppio is typing ur your callout this instant. wait for it on @doppycourse." ]
        await message.channel.send(random.choice(Rcout))
    
    if 'ugly rascal' in message.content.lower():
        await message.channel.send("MOVE YOU UGLY RASCAL") 

    if 'diavolo' in message.content.lower() and 'thank you' in message.content.lower():
        await message.channel.send("😏You are most welcome, beloved. 💋")
    
    if 'diavolo' in message.content.lower() and 'die' in message.content.lower():
        await message.channel.send("your callout is coming.")  

    if 'diavolo' in message.content.lower() and 'loser' in message.content.lower():
        await message.channel.send('oh shove off')
        
    if 'diavolo' in message.content.lower() and 'i love ' in message.content.lower():
        await message.add_reaction('❤')
        
    if 'diavolo' in message.content.lower() and ('spaghetti' in message.content.lower() or 'italian' in message.content.lower()) and 'speak' in message.content.lower():
        await message.channel.send("https://www.youtube.com/watch?v=mJkBsG2N16Y")            
    
#---------sentences that start with his name that arent questions

    if message.content.lower().startswith('diavolo') and not(message.content.endswith('?')):
        if 'dance' in message.content.lower():
            Rdance = ["https://www.youtube.com/watch?v=D1rAYznxy8w","https://www.youtube.com/watch?v=VMi-sgcIpdM", "https://www.youtube.com/watch?v=WHvEaZVmTig", "https://www.youtube.com/watch?v=BojiIJ39fUQ" "https://www.youtube.com/watch?v=siISG57cBXA" , "https://www.youtube.com/watch?v=2FzP0Nx9EWE","https://wildworld.tumblr.com/post/615772867142074368/go-ahead-quarantine-me-ill-just-listen-to-ayesha", "https://www.youtube.com/watch?v=IkEEpNp8pwI", " https://www.youtube.com/watch?v=JtAZ0gC6YHI", "https://www.youtube.com/watch?v=JSlwYTfjAsk", "https://www.youtube.com/watch?v=2frfoJ75P1k"]
            await message.channel.send(random.choice(Rdance))
            
        if 'quality' in message.content.lower() or 'cursed image' in message.content.lower():
            Rqual = ["https://i.imgur.com/3zNcfrq.jpg", "https://i.imgur.com/DHG7On4.png", "https://i.imgur.com/JWqnyGM.png", "https://i.imgur.com/0zFwV6W.png", "https://i.imgur.com/ocLOPvz.png", "https://i.imgur.com/JrVbfzs.png"]
            await message.channel.send(random.choice(Rqual))
            
        if 'screaming' in message.content.lower() or 'laughing' in message.content.lower():
            Rlaugh = ["https://i.imgur.com/DjQSIny.png", "https://www.youtube.com/watch?v=WSdAbgt1OTY", "https://www.youtube.com/watch?v=p4vAH0zV3yU", "https://www.youtube.com/watch?v=CVzJNFHIRf8", "https://www.youtube.com/watch?v=E4oRxh5lzEM", "https://www.youtube.com/watch?v=W966T3F_Y-E" ]
            await message.channel.send(random.choice(Rlaugh))              

#---------sentences that start with his name and are questions
    if message.content.lower().startswith('diavolo') and message.content.endswith('?'):
        
        if 'trish' in message.content.lower():
            RRtri = ["i dont think my daughter likes me much", "maybe i shouldnt have tried to stab her :/", "do you think if i send a gift card to olive garden's , trish will forget about the whole trying to kill her thing?" , "okay well MAYBE i shouldn't have tried to kill trish. i guess. but MY IDENTITY.....", "i don't think trish and i could get along even if i hadn't attempted to murder her. i mean, she's a prep, i'm a goth..."]
            await message.channel.send(random.choice(RRtri))
        

        elif 'diovolo' in message.content.lower() or 'kiraboss' in message.content.lower():
            RRwet = ["i dont even know that guy. shove off", "no thanks i'm too hot for this", "no thanks.", "who?"]
            await message.channel.send(random.choice(RRwet))
        
        elif 'lice' in message.content.lower() or 'fleas' in message.content.lower():
            RRlice = ["i- i shower. i do not have lice.", "ugh. no i don't have lice.", "these are SPOTS. I dye them on because i am PUNK", "shove off, it's hair dye, i'm going to kill you."]
            await message.channel.send(random.choice(RRlice))   
        
        elif 'should i' in message.content.lower():
            RRadv = ["i think u should go for it", "that sounds like a bad idea even for me", "yeah! what could go wrong lol", "hm? sorry im playing minecraft with doppio", "no i dont think so", "so long as youre doing it in a gnc way", "hmmmmmm yeah", "...i dont think so.", "maybe. cant u give me more info to go on...", "yeah sure just dont get stabbed"]
            await message.channel.send(random.choice(RRadv))               
        
        else:
            RRYN = ["no", "ok", "sure", "whatever",  "yeah", "absolutely not", "maybe so", "hmmm...", "i will consider it", "perhaps...","i dont care", "w", "H", "...no.", "hm. KING CRIMSON! slap this nasty fool!", "of course.", "perhaps... then again, perhaps not.", "ask me at another time.", "i'm not ready to answer that.", "doppio said to answer 'yes' to that one."]
            await message.channel.send(random.choice(RRYN))       
            


client.run('token')