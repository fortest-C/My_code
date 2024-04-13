### to play ###
# discord mods
import discord
from discord.ext import commands

# other mods
import json

# my mods
from core.classes import myCog

class HelpCommands(myCog):
    @commands.command()
    async def help(self, ctx):
        help_em = discord.Embed(title="help", description="a new help")
        help_em.add_field(name="em1", value="a embed")
        help_em.set_footer(text=f"i am <@{ctx.author}>", icon_url=ctx.author.avatar)
        
        await ctx.send(embed=help_em)


async def setup(bot):
    await bot.add_cog(HelpCommands(bot))