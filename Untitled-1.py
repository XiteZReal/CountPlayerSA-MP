import discord
from discord.ext import commands, tasks
import asyncio
from samp_client.client import SampClient

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
NeedIP = ' ' # IP Server
NeedPort = 7777 # Port Server
TokenBot = ' ' # Token Bot

@tasks.loop(seconds=60.0)
async def zahir():
    with SampClient(address=NeedIP, port=NeedPort) as client:
        NeedPlayer = "Players: {info.players}/{info.max_players}".format(info=client.get_server_info())
        print(NeedPlayer)
    ActiveTime = discord.Activity(name = NeedPlayer, type = discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.do_not_disturb, activity = ActiveTime)               

@bot.listen()
async def on_ready():
    zahir.start()

bot.run(TokenBot)