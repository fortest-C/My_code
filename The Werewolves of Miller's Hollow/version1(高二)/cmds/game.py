### to play ###
# discord mods
import discord
from discord.ext import commands

# other mods
import json

# my mods
from core.classes import myCog

class Game(myCog):
    @commands.command()
    async def join(self, ctx):
        with open('data.json', 'r', encoding='utf-8') as dt:
            data = json.load(dt)
            
        if ctx.author.id in data['player_id']:
            await ctx.send(f"<@{ctx.author.id}> 您已在玩家儲列中")
            ptinfo = ""
            for i in range(1, len(data['player_name'])+1):
                ptinfo += f"{i}: {data['player_name'][i-1]}\n"
            await ctx.send(ptinfo)
            return

        data['player_name'].append(ctx.author.name)
        data['player_id'  ].append(ctx.author.id)

        await ctx.send("!add successfully!")
        ptinfo = ""
        for i in range(1, len(data['player_name'])+1):
            ptinfo += f"{i}: {data['player_name'][i-1]}\n"
        await ctx.send(ptinfo)

        with open('data.json', 'w', encoding = "utf8") as dt:
            json.dump(data, dt, indent = 4)

    @commands.command()
    async def quit(self, ctx):
        with open('data.json', 'r', encoding='utf-8') as jdata:
            data = json.load(jdata)

        if ctx.author.id not in data['player_id']:
            await ctx.send(f"<@{ctx.author.id}> 您未在玩家儲列中")
            ptinfo = ""
            for i in range(1, len(data['player_name'])+1):
                ptinfo += f"{i}: {data['player_name'][i-1]}\n"
            await ctx.send(ptinfo)
            return

        data['player_name'].remove(ctx.author.name)
        data['player_id'].remove(ctx.author.id)

        await ctx.send("!delete successfully!")
        ptinfo = ""
        for i in range(1, len(data['player_name'])+1):
            ptinfo += f"{i}: {data['player_name'][i-1]}\n"
        await ctx.send(ptinfo)

        with open('data.json', 'w') as jdata:
            json.dump(data, jdata, indent = 4)

    @commands.command()
    async def player(self, ctx):
        with open('data.json', 'r', encoding = "utf8") as jdata:
            data = json.load(jdata)
        await ctx.send(f"目前玩家:{data['player_name']}\nvillager_number: {data['villager_number']}\nseer_number: {data['seer_number']}\nwitch_number: {data['witch_number']}\nwerewolf_number: {data['werewolf_number']}")

    @commands.command()
    async def cleanplayer(self, ctx):
        with open('data.json', 'r', encoding = "utf8") as jdata:
            data = json.load(jdata)
        data["player_name"] = []
        data["player_id"] = []
        data["werewolf_list"] = []
        data["villager_list"] = []
        data["witch_list"] = []
        data["seer_list"] = []
        await ctx.send("add player data have been received")



    @commands.command()
    async def st_q(self, ctx):
        await self.bot.unload_extension(f"cmds.main_game")
        print("unload main_game")
        await self.bot.load_extension(f"cmds.main_game")
        print("load main_game")
        await ctx.send("game stop successfully")




async def setup(bot):
    await bot.add_cog(Game(bot))