import requests
import discord
import organizer 


client = discord.Client()



@client.event
async def on_message(message):
    #if message.content.startswith('$help'):
    #    await message.channel.send('Just send something')
    """
    organizer.clean.data example below 

    Message: Hello all this is a message 

    final = {0: 'Hello', 1 : 'All', 2 : 'this', 3 : 'is', 4 : 'a', 5 : 'message' }

    """

    mc = message.content

    if mc.startswith('$helpAll'):
        await message.channel.send("""Roger_roger \n 
         What do I do?
         Currently I make Polls\n
         How do I do this?
         $poll <Your question: 
         Where is my code?
         https://github.com/Joegofett/Roger_roger/tree/master
         """)


    if mc.startswith('$help'):
        data = mc
        cd   = organizer.clean(data)
        await message.channel.send(f'sending new thing {cd[0]}')



    if mc.startswith('$poll'):
        data = mc
        cd = organizer.question(data)
        await message.channel.send(f'Question: {cd[2]}')

    discord.Spotify()





client.run('')





    # if message.author == client.user and message.content.startswith('$poll'):
    #     await message.add_reaction('1️⃣')
    #     await message.add_reaction('2️⃣')
    #     await message.add_reaction('3️⃣')
    #     return

    #     
    # if message.content.startswith('$poll'):
    #     pollCreation = message.content
    #     question, option1, option2, option3= pollCreation.split(';')
    #     # Improvement in the future us use a while or a for loop here to pull out all of the options and create variables for them. 
    #     # for var in poll:
    #     #   poll.split(':') this is where I'm stuck but will think about it some more. trying to avoid a nested loop  
        


    #     await message.channel.send("""{}, {}:one:, {}:two:, {}:three:""".format(question, option1, option2, option3 ))
    


