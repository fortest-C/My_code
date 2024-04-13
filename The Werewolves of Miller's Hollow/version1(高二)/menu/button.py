### to play ###
# discord mods
import discord
from discord.ext import commands
from discord.ui import Select,View,Button

# other mods
import json

# my mods
from core.classes import myCog


class mView(View):
    @discord.ui.button(label="1111", style=discord.ButtonStyle.red)
    async def callback(self, interaction):
        await interaction.response.send_message(conyent="oh!")


class button(myCog):
    @commands.command()
    async def button(self, ctx):

        view=mView()
            
        await ctx.send("test bt", view=view)




async def setup(bot):
    await bot.add_cog(button(bot))