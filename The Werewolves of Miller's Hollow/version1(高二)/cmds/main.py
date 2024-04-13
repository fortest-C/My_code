# discord mods

import discord
from discord.ext import commands

# other mods

# my mods
from core.classes import myCog

class ctrl(myCog):
    # load unload reload file
    @commands.command() # reload
    async def rlf(self, ctx, ext: str=None):
        if ext=="main":
            await ctx.send("cannot unload main file")
            return
        try:
            print("===================", ext)
            await self.bot.unload_extension(f"cmds.{ext}")
            await self.bot.load_extension(f"cmds.{ext}")
            await ctx.send("reload file successfully")
        except Exception as er:
            print(er)
    @commands.command() # reload
    async def rl_q(self, ctx):
        try:
            print("===================")
            await self.bot.unload_extension(f"menu.HelpCommands")
            await self.bot.load_extension(f"menu.HelpCommands")
            await ctx.send("reload file successfully")
        except Exception as er:
            print(er)
    @commands.command() # unload
    async def ulf(self, ctx, ext: str=None):
        if ext=="main":
            await ctx.send("cannot unload main file")
            return
        try:
            print("===================", ext)
            await self.bot.unload_extension(f"cmds.{ext}")
            await ctx.send("unload file successfully")
        except Exception as er:
            print(er)
    @commands.command() # load
    async def  lf(self, ctx, ext: str=None):
        if ext=="main":
            await ctx.send("cannot unload main file")
            return
        try:
            print("===================", ext)
            await self.bot.load_extension(f"cmds.{ext}")
            await ctx.send("load file successfully")
        except Exception as er:
            print(er)


async def setup(bot):
    await bot.add_cog(ctrl(bot))