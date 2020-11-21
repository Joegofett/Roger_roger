import requests
import discord
import organizer 

client = discord.Client()


@client.event
async def on_message(message):

    if message.content.startswith('$help'):
        await message.channel.send("""Roger_roger \n 
         What do I do?
         Currently I make quick Polls using Emoji's \n
         How do I do this?
         Here are the different ways to interact with the bot\n
         Your input: $poll: <Your question>: option1, option2, option3 (up to 10.)
         Response: Poll: Testing: option 1 option 2 option3
         Emojis: 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 0️⃣ \n
         Your Input: $day 
         Response: Check in! What day do you want to play this week?(Question about the emojis? message $help)
         Emojis: 🇺 🇲 🇹 🇼 🇷 🇫 🇸 \n
         Your Input: $time 
         Response: Free time! What time works best for you to play?(All times Eastern time)
         Emojis: 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ \n
         Where is my code?
         https://github.com/Joegofett/Roger_roger/tree/master
         """)



    if message.content.startswith('$poll:'):
        data       = message.content
        questionid = organizer.question(data)
        optiond    = organizer.pollOptions(data)
        ns         = organizer.pollPrinter(questionid=questionid, optiond=optiond)
        await message.channel.send(ns)

    if message.author == client.user and message.content.startswith('Poll'):
        data = message.content
        optiond = organizer.pollOptions(data)
        emojiCount = organizer.emojis(optiond)
        if message.content.startswith('Roger_roger'):
            pass 
        elif message.content.startswith('Poll'):
            while emojiCount > 0:
                if emojiCount == 1:
                    await message.add_reaction('1️⃣') 
                elif emojiCount == 2:
                    await message.add_reaction('2️⃣')
                elif emojiCount == 3:
                    await message.add_reaction('3️⃣')
                elif emojiCount == 4:
                    await message.add_reaction('4️⃣')
                elif emojiCount == 5:
                    await message.add_reaction('5️⃣')
                elif emojiCount == 6:
                    await message.add_reaction('6️⃣')
                elif emojiCount == 7:
                    await message.add_reaction('7️⃣')
                elif emojiCount == 8:
                    await message.add_reaction('8️⃣')          
                elif emojiCount == 9:
                    await message.add_reaction('9️⃣')
                elif emojiCount == 10:
                    await message.add_reaction('0️⃣')
                emojiCount = emojiCount - 1 

    if message.content.startswith('$day'):
        await message.channel.send("Check in! What day do you want to play this week?(Question about the emojis? message $help)")

    if message.author == client.user and message.content.startswith("Check in!"):
        await message.add_reaction('🇺')
        await message.add_reaction('🇲')
        await message.add_reaction('🇹')
        await message.add_reaction('🇼')
        await message.add_reaction('🇷')
        await message.add_reaction('🇫')
        await message.add_reaction('🇸')


    if message.content.startswith('$time'):
        await message.channel.send("Free time! What time works best for you to play?(All times Eastern time)")

    if message.author == client.user and message.content.startswith("Free time!"):
        await message.add_reaction('5️⃣')
        await message.add_reaction('6️⃣')
        await message.add_reaction('7️⃣')           
        await message.add_reaction('8️⃣')
        await message.add_reaction('9️⃣')


client.run('')