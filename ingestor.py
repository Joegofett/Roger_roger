import requests
import discord
import organizer 


client = discord.Client()




@client.event
async def on_message(message):

    if message.content.startswith('$helpAll'):
        await message.channel.send("""Roger_roger \n 
         What do I do?
         Currently I make Polls\n
         How do I do this?
         $poll: <Your question>: (option1) (option2) (option3) (etc) up to 20
         Where is my code?
         https://github.com/Joegofett/Roger_roger/tree/master
         """)


    if message.content.startswith('$help'):
        data = message.content
        cd   = organizer.clean(data)
        await message.channel.send(f'sending new thing {cd[0]}')



    if message.content.startswith('$poll:'):
        data       = message.content
        questionid = organizer.question(data)
        optiond    = organizer.pollOptions(data)
        ns         = organizer.pollPrinter(questionid=questionid, optiond=optiond)
        await message.channel.send(ns)
        #await message.channel.send()


client.run('Not today junior')










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
    


