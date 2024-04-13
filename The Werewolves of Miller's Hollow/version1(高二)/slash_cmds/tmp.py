### to play ###
# discord mods
import discord
from discord import app_commands
from discord.ext import commands

# other mods
import json

# my mods
from core.classes import myCog

class Tmp(myCog):
    pass
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()

    @app_commands.command(name="avatar", description="???")
    async def avatar(self, interaction:discord.Interaction, member:discord.Member = None):
        if member is None:
            member = interaction.user
        
        avatr_em = discord.Embed(title="tmp1", description="a temp embed")
        avatr_em.set_image(url=member.avatar)
        avatr_em.set_footer(text=f"hi {member.name}",icon_url=member.avatar)
        await interaction.response.send_message(embed=avatr_em)


async def setup(bot):
    await bot.add_cog(Tmp(bot))