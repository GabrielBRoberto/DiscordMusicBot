import discord
from discord.ext import commands
import music

cogs = music

client = commands.Bot(command_prefix="!", intends = discord.Intents.all())

cogs.setup(client)

client.run("OTA5MjIwMjQxOTM3MTU4MjM0.YZBHVg.b8d8U7ywuvZMa-Y4YgesacUPboo")