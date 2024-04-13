### to play ###
# discord mods
import discord
from discord.ext import commands
from discord.ui import Select,View,Button

# other mods
import json

# my mods
from core.classes import myCog

async def ch_to_1():
    embed = discord.Embed(title="test1", description="for test 1")
    embed.add_field(name="name1",value="name for test 1")
    button = Test_Bt1()

async def ch_to_2():
    embed = discord.Embed(title="test2", description="for test 2")
    embed.add_field(name="name2",value="name for test 2")
    button = Test_Bt2()

class Test_Bt1(View):
    @Button(label="change to 2")
    async def back(self ,interaction: discord.Integration ,button: discord.Button):
        await ch_to_2()

class Test_Bt2(View):
    @Button(label="change to 1")
    async def back(self ,interaction: discord.Integration ,button: discord.Button):
        await ch_to_1()


class Test_Help(myCog):
    @commands.command()
    async def t_help(self, ctx):
        embed = discord.Embed(title="test1", description="for test 1")
        embed.add_field(name="name1",value="name for test 1")
        ctx.send(embed=embed, button=Test_Bt2())









async def setup(bot):
    await bot.add_cog(Test_Help(bot))