# discord mods
import discord
from discord.ext import commands

# other mods
import os
import json
import asyncio

# my mods
with open('setting.json', 'r') as s:
    jset = json.load(s)

bot = commands.Bot(command_prefix='+/', intents=discord.Intents.all())

@bot.event
async def on_command_error(ctx, err):
    print(err)

@bot.event
async def on_ready():
    print("ready!")
    await bot.get_channel(YOUR_CHANNEL).send(">>Ready from werewolf<<")


# load mode in cmds and run bot
async def load_file():
    for file in os.listdir("./cmds"):
        if file.endswith(".py"):
            await bot.load_extension(f"cmds.{file[:-3]}")
            print(f"load {file} successfully")
            
    for file in os.listdir("./menu"):
        if file.endswith(".py"):
            await bot.load_extension(f"menu.{file[:-3]}")
            print(f"load {file} successfully")
async def online():
    await load_file()
    await bot.start(jset['TOKEN'])
asyncio.run(online())
