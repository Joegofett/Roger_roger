import requests
import discord
import organizer 

client = discord.Client()


@client.event
async def on_message(message):

    if message.content.startswith('$help'):
        await message.channel.send("""Roger_roger \n 
         What do I do?
         Currently I make Polls\n
         How do I do this?
         $poll: <Your question>: option1, option2, option3, (etc) up to 10
         Where is my code?
         https://github.com/Joegofett/Roger_roger/tree/master
         """)

    #TODO Fix this so that it does something. I mean Help all is nice but maybe but
    if message.content.startswith('$emoji'):
        data     = message.content
        #optiond  = organizer.pollOptions(data)
        await message.add_reaction("one")
    
    
    #    data = message.content
    #    cd   = organizer.clean(data)
    #    await message.channel.send(f'sending new thing {cd[0]}')



    if message.content.startswith('$poll:'):
        data       = message.content
        questionid = organizer.question(data)
        optiond    = organizer.pollOptions(data)
        ns         = organizer.pollPrinter(questionid=questionid, optiond=optiond)
        await message.channel.send(ns)
        #await message.channel.send(          )

    if message.author == client.user:
        if message.content.startswith('Roger_roger'):
            pass
        data = message.content
        optiond = organizer.pollOptions(data)
        emojiCount = organizer.emojis(optiond)
        while emojiCount > 0:
            if emojiCount == 10:
                await message.add_reaction('0️⃣')
            elif emojiCount == 9:
                await message.add_reaction('9️⃣')
            elif emojiCount == 8:
                await message.add_reaction('8️⃣')
            elif emojiCount == 7:
                await message.add_reaction('7️⃣')
            elif emojiCount == 6:
                await message.add_reaction('6️⃣')
            elif emojiCount == 5:
                await message.add_reaction('5️⃣')
            elif emojiCount == 4:
                await message.add_reaction('4️⃣')
            elif emojiCount == 3:
                await message.add_reaction('3️⃣')       
            elif emojiCount == 2:
                await message.add_reaction('2️⃣')
            elif emojiCount == 1:
                await message.add_reaction('1️⃣') 
            emojiCount = emojiCount - 1 


client.run('')


