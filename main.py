import discord
from discord.ext import commands
import music

cogs = music

client = commands.Bot(command_prefix="!", intends = discord.Intents.all())

cogs.setup(client)

client.run("OTA5MjIwMjQxOTM3MTU4MjM0.YZBHVg.9nohMtet4UcCdZ-GayAlfvEHxTo")