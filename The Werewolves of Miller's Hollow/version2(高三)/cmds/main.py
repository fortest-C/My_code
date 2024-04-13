# discord mods

import discord
from discord.ext import commands

# other mods
import json
with open('setting.json', 'r') as s:
    setting = json.load(s)

# my mods
from core.classes import myCog


async def TestAuthorPermission(ctx: commands.Context) -> bool:
    if ctx.author.id not in setting['Developers'] :
        await ctx.send("權限錯誤, error code: MainPermission001'", ephemeral=True)
        return False
    else: return True

class ctrl(myCog):
    # load unload reload file
    @commands.command() # reload
    async def rlf(self, ctx, ext: str=None):
        if not await TestAuthorPermission(ctx): return
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
        if not TestAuthorPermission(ctx): return
        try:
            print("===================")
            await self.bot.unload_extension(f"menu.HelpCommands")
            await self.bot.load_extension(f"menu.HelpCommands")
            await ctx.send("reload file successfully")
        except Exception as er:
            print(er)
    @commands.command() # unload
    async def ulf(self, ctx, ext: str=None):
        if not TestAuthorPermission(ctx): return
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
        if not TestAuthorPermission(ctx): return
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