import asyncio
import discord
import re
from discord.ext import commands
from urllib.request import urlopen

BOT_TOKEN = 'MTA5Nzk1MjM4NDMxMjk1NTAwMA.Gpqu9w.MC4b8tcTBqpbzVjoJhJ1PpZ3Irc7628oMc5hvU'
CHANNEL_ID = 1095333367014248453

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():

    # Get word of the day
    def get_word_of_the_day():
        start_index = html.find("<title>") + len("<title>")
        end_index = html.find("</title>")
        word = html[start_index:end_index]
        return word

    # Get definition
    def get_definition_of_the_day():
        start_index = html.find("<p>") + len("<p>")
        end_index = html.find("</p>")
        definition = html[start_index:end_index]
        definition = re.sub(r'<.*?>', '', definition)
        return definition

    last_word = ''
    print("Hello! WoTD Bot is ready!")

    while True:
        url = "https://www.merriam-webster.com/word-of-the-day"

        page = urlopen(url)

        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        get_word_of_the_day()
        get_definition_of_the_day()

        word = get_word_of_the_day()
        definition = get_definition_of_the_day()

        if last_word != word:
            channel = bot.get_channel(CHANNEL_ID)
            await channel.send(word + "\n" + definition)
            last_word = word
            print(word + "\n" + definition)


        await asyncio.sleep(3600)



bot.run(BOT_TOKEN)