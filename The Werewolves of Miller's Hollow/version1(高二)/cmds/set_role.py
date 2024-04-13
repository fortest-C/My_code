### set number of role ###
# discord mods
import discord
from discord.ext import commands

# other mods
import json

# my mods
from core.classes import myCog

class Role_set(myCog):
    # print role info
    async def print_role(self, ctx):
        with open('data.json', 'r') as dt:
            data = json.load(dt)
        await ctx.send(f"villager number: {data['villager_number']}\nseer number: {data['seer_number']}\nwitch number: {data['witch_number']}\nwerewolf number: {data['werewolf_number']}")
    
    #set werewolf
    async def set_werewolf(self, ctx, ext):
        with open("data.json", 'r') as dt:
            data = json.load(dt)
        if ext == "+":
            data['werewolf_number'] += 1
        elif ext == "-":
            if data['werewolf_number'] == 0:
                await ctx.send("該數量不應為負數")
                return
            data['werewolf_number'] -= 1
        else:
            try:
                ext = int(ext)
            except:
                await ctx.send("附加值錯誤, 應為0 ~ 9或 '+', '-'")
            if ext < 0:
                await ctx.send(f"附加值{ext}不應為負")
                return
            else:
                data['werewolf_number'] = ext

        with open("data.json", 'w') as dt:
            json.dump(data, dt, indent = 4)
        
        await ctx.send("!change successfully!")
        await self.print_role(ctx)
    @commands.command()
    async def werewolf(self, ctx, ext):
        await self.set_werewolf(ctx, ext)
    @commands.command()
    async def wf(self, ctx, ext):
        await self.set_werewolf(ctx, ext)

    #set villager
    async def set_villager(self, ctx, ext):
        with open("data.json", 'r') as dt:
            data = json.load(dt)
        if ext == "+":
            data['villager_number'] += 1
        elif ext == "-":
            if data['villager_number'] == 0:
                await ctx.send("該數量不應為負數")
                return
            data['villager_number'] -= 1
        else:
            try:
                ext = int(ext)
            except:
                await ctx.send("附加值錯誤, 應為0 ~ 9或 '+', '-'")
            if ext < 0:
                await ctx.send(f"附加值{ext}不應為負")
                return
            else:
                data['villager_number'] = ext

        with open("data.json", 'w') as dt:
            json.dump(data, dt, indent = 4)
        
        await ctx.send("!change successfully!")
        await self.print_role(ctx)
    @commands.command()
    async def villager(self, ctx, ext):
        await self.set_villager(ctx, ext)
    @commands.command()
    async def vlg(self, ctx, ext):
        await self.set_villager(ctx, ext)

    #set seer
    async def set_seer(self, ctx, ext):
        with open("data.json", 'r') as dt:
            data = json.load(dt)
        if ext == "+":
            data['seer_number'] += 1
        elif ext == "-":
            if data['seer_number'] == 0:
                await ctx.send("該數量不應為負數")
                return
            data['seer_number'] -= 1
        else:
            try:
                ext = int(ext)
            except:
                await ctx.send("附加值錯誤, 應為0 ~ 9或 '+', '-'")
            if ext < 0:
                await ctx.send(f"附加值{ext}不應為負")
                return
            else:
                data['seer_number'] = ext

        with open("data.json", 'w') as dt:
            json.dump(data, dt, indent = 4)
        
        await ctx.send("!change successfully!")
        await self.print_role(ctx)
    @commands.command()
    async def seer(self, ctx, ext):
        await self.set_seer(ctx, ext)
    @commands.command()
    async def sr(self, ctx, ext):
        await self.set_seer(ctx, ext)
        
    #set witch
    async def set_witch(self, ctx, ext):
        with open("data.json", 'r') as dt:
            data = json.load(dt)
        if ext == "+":
            data['witch_number'] += 1
        elif ext == "-":
            if data['witch_number'] == 0:
                await ctx.send("該數量不應為負數")
                return
            data['witch_number'] -= 1
        else:
            try:
                ext = int(ext)
            except:
                await ctx.send("附加值錯誤, 應為0 ~ 9或 '+', '-'")
            if ext < 0:
                await ctx.send(f"附加值{ext}不應為負")
                return
            else:
                data['witch_number'] = ext

        with open("data.json", 'w') as dt:
            json.dump(data, dt, indent = 4)
        
        await ctx.send("!change successfully!")
        await self.print_role(ctx)
    @commands.command()
    async def witch(self, ctx, ext):
        await self.set_witch(ctx, ext)
    @commands.command()
    async def wh(self, ctx, ext):
        await self.set_witch(ctx, ext)

async def setup(bot):
    await bot.add_cog(Role_set(bot))
