import discord
import key_file
# To make things easier to read I think we should put the more complicated workings of the bot into a different file
import bot_functions

vmessage = "Achivements!"
client = discord.Client()
discord_key = key_file.external_key
bot_author_id = 975411631863496735
bot_mention_string = ('<@975411631863496735>')



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    async def achivement_message(username, achivement):
        if bot_functions.add_achivement_to_user(username, achivement) == True:
            string = ("> ** Achivement gotten:  "+achivement+"**")
            await message.channel.send(string)


    #adds brackets to turns id into a string to avoid issues with sqlite
    author_id_string = ('['+str(message.author.id)+"]")
    #prints authoername[autherid]:   message    
    author_message_string = (message.author.name+author_id_string+":   "+message.content)
    print(author_message_string)
    if bot_functions.add_user(author_id_string) == True:
        await message.channel.send("This is the first message from you I've ever read")
        await message.channel.send("have fun hunting achivements")    
        await achivement_message(author_id_string, "Welcome!")

#____COMMANDS_____
    
    #HELLO/HEWWO COMMAND-------------------------------
    if message.content.startswith('Hello') or message.content.startswith('hello'):
        await message.channel.send('Hello')
    if message.content.startswith('Hewwo') or message.content.startswith('hewwo'):
        await message.channel.send("Hewwo (。O ω O。)")
        await achivement_message(author_id_string, "OwO Whats this?")
    #ACHIVEMENT COMMANDS
    if message.content.startswith("!ac achivement") or message.content.startswith("!ac Achivement") or message.content.startswith("!ac ACHIVEMENT"):
        await message.channel.send("> "+bot_functions.return_all_achivements(author_id_string))

#____BOT RECOGNISING THINGS____

#Bot recognising @'s        
    if bot_functions.find_string(str(message.content), str(bot_mention_string)) == True:
        await message.channel.send("You mentioned me (。O ω O。)")
        await achivement_message(author_id_string, "Good thing to Mention")
#Bot recognising "Dragon Slayer"
    if bot_functions.find_string(str(message.content), "the dragoon slayer"):
        await achivement_message(author_id_string, "Super-greatbick-dicksowrd")






client.run(discord_key)