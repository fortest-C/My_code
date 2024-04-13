# discord mods

import discord
from discord.ext import commands

# other mods
import json

# my mods
from core.classes import myCog

class werewolf_commands(myCog):
    @commands.command()
    async def kill(self, ctx, ext):
        with open('data.json','r') as dt:
            data = json.load(dt)
        if ctx.author.id not in data['werewolf_list']:
            print('raise a error by {werewolf cmds} because not a werewolf')
            await ctx.send("您無拜訪此命令之權限")
            return
        if data['time'] == "day":
            print('raise a error by {werewolf cmds} because time is not "night"')
            await ctx.send("目前時間為早上")
            return
        try:
            ext = int(ext)
        except:
            print('raise a error by {werewolf cmds} because type of "ext" is not "int"')
            await ctx.send("資料錯誤")
            return
        if ext >= len(data['alive']) or ext < 0:
            print('raise a error by {werewolf cmds} because "ext" is not correct')
            await ctx.send("查無此人")
            return
        for i in data['wolf_vote']:
            if i[1] == ctx.author.id:
                i[0] = ext
                await ctx.author.send("目標已變更")
                with open('data.json', 'w') as dt:
                    json.dump(data, dt, indent =1)
                return
        data['wolf_vote'].append([ext, ctx.author.id])
        await ctx.author.send("目標已選定")
        with open('data.json', 'w') as dt:
            json.dump(data, dt, indent =1)
    
    # werewolf discuss
    async def discuss_def(self, ctx):
        with open('data.json', 'r') as dt:
            data = json.load(dt)
        if ctx.author.id not in data['werewolf_list']:
            await ctx.send("您不是狼人，沒有與狼人溝通的能力")
            print('raise a error by {discuss cmds} because not a werewolf')
            return
        else:
            if len(data['werewolf_list']) == 1:
                await ctx.send("沒有說話對象")
                print('raise a error by {discuss cmds} because there is no person to talk')
                return
            else:
                message = ctx.message.content
        for i in data['werewolf_list']:
            x = self.bot.get_user(i)
            await x.send(f"_公告: <@{ctx.author.id}> 說:_\n"+
                         f"`{message[9:]}`")
    @commands.command()
    async def discuss(self, ctx, ext):
        await self.discuss_def(ctx)
    @commands.command()
    async def dc(self, ctx, ext):
        await self.discuss_def(ctx)

    @commands.command()
    async def witch(self, ctx, ext):
        print('in witch cmd, ext =', ext)
        id = ctx.author.id

        with open('data.json', 'r') as dt:
            data = json.load(dt)
        if data['time'] == 'day':
            print('raise a error by {witch cmds} because now is day')
            await ctx.send('白天無法施法')
            return
        location_in_list = -1
        for i in range(len(data['witch_list'])):
            if id == data['witch_list'][i][0]:
                location_in_list = i
                break
        if location_in_list == -1:
            print('raise a error by {witch cmds} because not a witch')
            await ctx.send('您無拜訪此命令之權限')
            return

        if ext == 'Y' or ext == 'y':
            if data['witch_list'][location_in_list][1] == 0:
                print('raise a error by {werewolf cmds} because there is not have any antidote')
                await ctx.send('您已使用過解藥')
                return
            data['witch_list'][location_in_list][1] = 0
            data['witch_antidote'].append(True)
            data['witch_antidote_n'] += 1
            with open('data.json', 'w') as dt:
                json.dump(data, dt, indent=1)
            await ctx.send('您已對他使用解藥')

        elif ext == 'N' or ext == 'n':
            data['witch_antidote'].append(False)
            with open('data.json', 'w') as dt:
                json.dump(data, dt, indent=1)
            await ctx.send('您不對她使用解藥')
        
        else: # 毒藥
            print('毒藥')
            if not data['witch_list'][location_in_list][2]:
                print('raise a error by {witch cmds} because poison has been used')
                await ctx.send('您已使用過毒藥')
                return
            try:
                ext = int(ext)
            except:
                print('raise a error by {witch cmds} because the type of extension is not correct')
                await ctx.send("附加值錯誤")
                return
            if ext >= len(data['alive']) or ext < -1:
                print('raise a error by {witch cmds} because the extension is not correct')
                await ctx.send("查無此人")
                return

            if ext == -1:
                await ctx.send('您今晚將不下毒')
                data['witch_poison'].append(-1)
                with open('data.json', 'w') as dt:
                    json.dump(data, dt, indent=1)
                return

            with open('data.json', 'r') as dt:
                data = json.load(dt)
            kill_id = data['alive'][ext]

            temp1 = True
            for i in range(len(data['killed_id'])):
                if data['killed_id'][i] == kill_id:
                    if data['killed_by'][i] == "狼人":
                        print("raise a error by {witch cmds} because the target has already been killed")
                        await ctx.send("無效的操作，因該對象已遭殺害")
                        return
                    else:
                        temp1 = False

            data['witch_poison'].append(ext)
            if temp1:
                data['killed_id'].append(kill_id)
                data['killed_by'].append('女巫')
            data['witch_list'][location_in_list][2] = False

            #DEBUG:
            for d in data:
                print(d, '-->', data[d])

            with open('data.json', 'w') as dt:
                json.dump(data, dt, indent=1)
            await ctx.send('您已對他使用毒藥')
            
    @commands.command()
    async def check(self, ctx, ext):
        id = ctx.author.id

        with open('data.json', 'r') as dt:
            data = json.load(dt)
        if data['time'] == 'day':
            print('raise a error by {seer cmds} because now is day')
            await ctx.send('白天無法施法')
            return
        location_in_list = -1
        for i in range(len(data['seer_list'])):
            if id == data['seer_list'][i][0]:
                location_in_list = i
                break
        if location_in_list == -1:
            print('raise a error by {seer cmds} because not a seer')
            await ctx.send('您無拜訪此命令之權限')
            return
        if id in data['seer_check']:
            print('raise a error by {seer cmds} because has used check command already')
            await ctx.send("您今晚的體力已耗盡")
            return
        try:
            ext = int(ext)
        except:
            print('raise a error by {seer cmds} because the type of extension is not correct')
            await ctx.send("附加值錯誤")
            return
        if ext >= len(data['alive']) or ext < -1:
            print('raise a error by {seer cmds} because the extension is not correct')
            await ctx.send("查無此人")
            return

        if data['alive'][ext] in data['werewolf_list']:
            await ctx.send(f"<@{data['alive'][ext]}>是狼人")
        else:
            await ctx.send(f"<@{data['alive'][ext]}>不是狼人")
        
        data['seer_check'].append(id)
        data['seer_list'][location_in_list][1] = False
        with open('data.json', 'w') as dt:
            json.dump(data, dt, indent=1)

    @commands.command()
    async def vote(self, ctx, ext):
        with open('data.json', 'r') as dt:
            data = json.load(dt)
        if ctx.author.id not in data['alive']:
            print('raise a error by {vote cmds} because he has died')
            await ctx.send('您已被被放逐或已死亡')
            return
        if data['time'] == 'night':
            print('raise a error by {vote cmds} because now is day')
            await ctx.send('您只能在白天時投票')
            return
        try:
            ext = int(ext)
        except:
            print('raise a error by {vote cmds} because the type of extension is not correct')
            await ctx.send("附加值錯誤")
            return
        if ext >= len(data['alive']) or ext < 0:
            print('raise a error by {vote cmds} because the extension is not correct')
            await ctx.send("查無此人")
            return

        havebeen = False
        for i in data['people_vote']:
            if i[0] == ctx.author.id:
                print('raise a error by {vote cmds} because antidote has been used')
                await ctx.send('您已投過票')
                havebeen = True
                break
        if havebeen:
            return
        with open('data.json', 'r') as dt:
            data = json.load(dt)
        data['people_vote'].append([ctx.author.id, ext])
        await ctx.send('投票已送出')
        with open('data.json', 'w') as dt:
            json.dump(data, dt, indent=1)
        


async def setup(bot):
    await bot.add_cog(werewolf_commands(bot))