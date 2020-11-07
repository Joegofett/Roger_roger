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
         $poll: <Your question>: option1, option2, option3, (etc) up to 20
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
        emojiCount = organizer.emojis(optiond)
        while emojiCount >= 0:
            #emoji = str(emojiCount)
            await message.add_reaction()
            emojiCount = emojiCount - 1
        #await message.channel.send()



client.run('')


