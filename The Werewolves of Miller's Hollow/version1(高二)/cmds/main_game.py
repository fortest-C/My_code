### main game python file ###
# discord mods
import discord
from discord.ext import commands

# other mods
import json
import random
import asyncio

# my mods
from core.classes import myCog

class Main(myCog):
    @commands.command()
    async def start(self, ctx):
        #===== ===== 初始化 始 ===== =====#
        with open('data.json', 'r') as dt:
            data = json.load(dt)
        
        data['werewolf_list'] = []
        data['villager_list'] = []
        data['seer_list'] = []
        data['witch_list'] = []
        data['tell_everyone_the_true'] = ""

        with open('data.json', 'w') as dt:
            json.dump(data, dt, indent=1)
        #===== ===== 初始化 終 ===== =====#

        #===== ===== 檢查角色分配 始 ===== =====#
        with open('data.json', 'r') as dt:
            data = json.load(dt)
        if data['seer_number'] + data['witch_number'] == 0:
            await ctx.send("提示: 沒有神職人員")
        if data['villager_number'] == 0:
            await ctx.send("提示: 沒有平民")
        if data['werewolf_number'] == 0:
            await ctx.send("錯誤: 沒有狼人")
            return
        #===== ===== 檢查角色分配 終 ===== =====#

        #===== ===== 分配 始 ===== =====#
        
        t_villager_number = data['villager_number']
        t_seer_number =     data['seer_number']
        t_witch_number =    data['witch_number']
        t_werewolf_number = data['werewolf_number']
        print('t_villager_number = ', t_villager_number)
        print('t_seer_number = '    , t_seer_number)
        print('t_witch_number = '   , t_witch_number)
        print('t_werewolf_number = ', t_werewolf_number)
        i = 0
        while i < (len(data['player_id'])):
            # == == choose the list that is empty first :start: == ==　#
            empty_l = []
            if len(data['villager_list']) == 0 and t_villager_number != 0:
                empty_l.append("villager")
            if len(data['seer_list'])     == 0 and t_seer_number     != 0:
                empty_l.append("seer")
            if len(data['witch_list'])    == 0 and t_witch_number    != 0:
                empty_l.append("witch")
            if len(data['werewolf_list']) == 0 and t_werewolf_number != 0:
                empty_l.append("werewolf")
            print("empty_l:", empty_l)
            if len(empty_l) != 0:
                mth = random.choice(empty_l)
                tof = True
                if mth == "werewolf":
                    tof = False
                    t_werewolf_number -= 1
                    print('choose werewolf by empty')
                    data['werewolf_list'].append(data['player_id'][i])
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> is `werewolf`"
                if mth == "seer":
                    tof = False
                    t_seer_number -= 1
                    print('choose seer by empty')
                    data['seer_list'].append([data['player_id'][i], False])
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> is `seer`"
                if mth == "witch":
                    tof = False
                    t_witch_number -= 1
                    print('choose witch by empty')
                    data['witch_list'].append([data['player_id'][i],1,1,False])
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> is `witch`"
                if mth == "villager":
                    tof = False
                    t_villager_number -= 1
                    print('choose villager by empty')
                    data['villager_list'].append(data['player_id'][i])
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> is `villager`"
                if tof:
                    print("===! ERROR !===")
                i += 1
                continue
            # == == choose the list that is empty first :stop: == ==　#

            await asyncio.sleep(0.1)
            mth = random.randrange(0, 3)
            crr = -1
            if mth == 0:
                crr = random.randrange(1, 5)
            elif mth == 1:
                crr = random.choice([3,4,2,1])
            elif mth == 2:
                tmp = random.randrange(137)
                crr = (tmp*3-9)%4+1

            if crr == 1:
                if t_villager_number == 0:
                    print('-1')
                else:
                    t_villager_number -= 1
                    print('choose villager')
                    data['villager_list'].append(data['player_id'][i])
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> is `villager`"
                    i += 1
            elif crr == 2:
                if t_seer_number == 0:
                    print('-1')
                else:
                    t_seer_number -= 1
                    print('choose seer')
                    data['seer_list'].append([data['player_id'][i], False])
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> is `seer`"
                    i += 1
            elif crr == 3:
                if t_witch_number == 0:
                    print('-1')
                else:
                    t_witch_number -= 1
                    print('choose witch')
                    data['witch_list'].append([data['player_id'][i],True,True])
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> is `witch`"
                    i += 1
            elif crr == 4:
                if t_werewolf_number == 0:
                    print('-1')
                else:
                    t_werewolf_number -= 1
                    print('choose werewolf')
                    data['werewolf_list'].append(data['player_id'][i])
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> is `werewolf`"
                    i += 1
        with open('data.json', 'w') as dt:
            json.dump(data, dt, indent=1)
        #===== ===== 分配 終 ===== =====#
        print("stop")
        #===== ===== 通知角色 始 ===== =====#
        with open('data.json', 'r') as dt:
            data = json.load(dt)
        for i in data['villager_list']:
            print('send villager')
            a = self.bot.get_user(i)
            await a.send("您是平民")
        for i in data['seer_list']:
            print('send seer')
            a = self.bot.get_user(i[0])
            await a.send("您是預言家")
        for i in data['witch_list']:
            print('send witch')
            a = self.bot.get_user(i[0])
            await a.send("您是女巫")
        for i in data['werewolf_list']:
            print('send werewolf')
            a = self.bot.get_user(i)
            await a.send("您是狼人")
        #===== ===== 通知角色 終 ===== =====#

        #===== ===== 調適 ===== =====#
        data['alive'] = data['player_id']
        with open('data.json', 'w') as dt:
            json.dump(data, dt, indent=1)
        await ctx.send("遊戲開始")
        #===== ===== 進入遊戲 ===== =====#
        while True:
            with open('data.json','r') as dt:
                data = json.load(dt)
            #===== ===== 夜晚降臨 ===== =====#
            data['time'] = "night"

            await ctx.send(f"夜晚降臨")
            #===== ===== 數據初始化 始 ====== =====#
            data['wolf_vote'] =    []
            data['killed_id'] =    []
            data['killed_by'] =    []
            data['witch_poison'] = []
            data['witch_save'] =   []

            data['killed_id'] = []
            data['killed_by'] = []
            with open('data.json', 'w') as dt:
                json.dump(data, dt, indent=1)
            #===== ===== 數據初始化 終 ====== =====#

            # ptinfo is a string used to send all the people that still alive
            ptinfo = ""
            for i in range(0, len(data['alive'])):
                ptinfo += f"{i}: <@{data['alive'][i]}>\n"

            #===== ===== 狼人投票 始 ====== =====#
            await ctx.send("狼人開始投票")
            wolf_list = list(map(lambda x: self.bot.get_user(x), data['werewolf_list']))
            ptwolf = ""
            for i in wolf_list:
                ptwolf += f"\n--{i.name}"
            for i in wolf_list:
                await i.send(f"狼人互認身分:{ptwolf}\n")
                await i.send(f"請選擇對象 (`+/kill <number>`)\n"+
                            f"{ptinfo}")
            while(True):
                await asyncio.sleep(4)
                with open('data.json', 'r') as dt:
                    data = json.load(dt)
                if len(data['wolf_vote']) == len(data['werewolf_list']):
                    break
            for i in wolf_list:
                await i.send("投票結束")
                
            be_voted_by_wolf = []
            for i in data['alive']:
                be_voted_by_wolf.append(0)
            for i in data['wolf_vote']:
                be_voted_by_wolf[i[0]] += 1
            max = 0
            for i in be_voted_by_wolf:
                if i > max:
                    max = i
            kill = []
            l = len(be_voted_by_wolf)
            for i in range(l):
                if be_voted_by_wolf[i] == max:
                    kill.append(i)
            kill = random.choice(kill)
            kill = data['alive'][kill]
            data['killed_id'].append(kill)
            data['killed_by'].append("狼人")
            with open('data.json', 'w') as dt:
                json.dump(data, dt, indent=1)
            del be_voted_by_wolf
            del wolf_list
            del ptwolf
            del kill
            #===== ===== 狼人投票 終 ====== =====#

            #===== ===== 告知女巫、預言家 始 ===== =====#
            data['witch_antidote_n'] = 0
            data['witch_antidote'] = []
            data['witch_poison'] =   []
            data['seer_check'] =     []

            for witch in data['witch_list']:
                x = self.bot.get_user(witch[0])
                if witch[1] == True:
                    await x.send(f"就在方才<@{data['killed_id'][0]}>被狼人殺了，你要幫助他嗎?`+/witch <Y/N>`)\n")
                else:
                    await x.send("您已使用過解藥")
                    data['witch_antidote'].append(False)
                if witch[2] == True:
                    await x.send(f"是否使用毒藥 `+/witch <number>` PS.若附加值為-1則不下毒\n"+
                                 f"{ptinfo}")
                else:
                    await x.send("您已使用過毒藥")
                    data['witch_poison'].append(-1)

            for seer in data['seer_list']:
                await asyncio.sleep(4)
                x = self.bot.get_user(seer[0])
                seer[1] = True
                await x.send(f"請選擇查驗對象(+/check)\n"+
                             f"{ptinfo}")
            with open('data.json', 'w') as dt:
                json.dump(data, dt, indent =1)
            #===== ===== 告知女巫、預言家 終 ===== =====#

            #===== ===== 女巫、預言家施法 始 ====== =====#
            await ctx.send(f"女巫及預言家正在施法")
            wn = len(data['witch_list'])
            sn = len(data['seer_list'])
            while True:
                await asyncio.sleep(4)
                with open('data.json', 'r') as dt:
                    data = json.load(dt)
                if len(data['witch_antidote']) == wn and len(data['witch_poison']) == wn and len(data['seer_check']) == sn:
                    break
            with open('data.json', 'r') as dt:
                data = json.load(dt)
            if data['witch_antidote_n'] % 2 != 0:
                del data['killed_id'][0]
                del data['killed_by'][0]
            with open('data.json', 'w') as dt:
                json.dump(data, dt, indent=1)
            del wn
            del sn
            #===== ===== 女巫、預言家施法 終 ====== =====#
            
            #===== ===== 旭日高升 ===== =====#    
            await ctx.send('白晝降臨')

            with open('data.json', 'r') as jdata:
                data = json.load(jdata)

            if len(data['killed_id']) > 0:
                for i in range(len(data['killed_id'])):
                    finded = False
                    for j in range(len(data['alive'])):
                        if data['alive'][j] == data['killed_id'][i]:
                            del data['alive'][j]
                            break
                    for j in range(len(data['witch_list'])):
                        if data['witch_list'][j][0] == data['killed_id'][i]:
                            del data['witch_list'][j]
                            finded = True
                            await ctx.send(f"昨晚 <@{data['killed_id'][i]}> 被 `{data['killed_by'][i]}` 殺了")
                            break
                    if finded:
                        continue
                    for j in range(len(data['seer_list'])):
                        if data['seer_list'][j][0] == data['killed_id'][i]:
                            del data['seer_list'][j]
                            finded = True
                            await ctx.send(f"昨晚 <@{data['killed_id'][i]}> 被 `{data['killed_by'][i]}` 殺了")
                            break
                    if finded:
                        continue
                    for j in range(len(data['villager_list'])):
                        if data['villager_list'][j] == data['killed_id'][i]:
                            print('q')
                            del data['villager_list'][j]
                            print('w')
                            finded = True
                            print('e')
                            await ctx.send(f"昨晚 <@{data['killed_id'][i]}> 被 `{data['killed_by'][i]}` 殺了")
                            break
                    if finded:
                        continue
                    for j in range(len(data['werewolf_list'])):
                        if data['werewolf_list'][j] == data['killed_id'][i]:
                            del data['werewolf_list'][j]
                            finded = True
                            await ctx.send(f"昨晚 <@{data['killed_id'][i]}> 被 `{data['killed_by'][i]}` 殺了")
                            break
                    if finded:
                        continue
            else:
                await ctx.send(f'昨晚安然度過')
            data['people_vote'] = []
            data['time'] = 'day'
            with open('data.json', 'w') as dt:
                json.dump(data, dt, indent=1)

            #===== ===== 檢查玩家角色狀態 始 ===== =====#            
            with open('data.json', 'w') as dt:
                json.dump(data, dt, indent=1)

            gq=False
            bq=False
            if len(data['villager_list']) or len(data['seer_list']) or len(data['witch_list']):
                gq = True
            if len(data['werewolf_list']):
                bq = True
            
            if gq==True and bq==False:
                await ctx.send("GAME OVER: Good Guys Win!!")
                return
            if bq==True and gq==False:
                await ctx.send("GAME OVER: Bad Guys Win!!")
                return
            #===== ===== 檢查玩家角色狀態 終 ===== =====#

            # ptinfo is a string used to send all the people that still alive
            be_voted_by_people = []
            ptinfo = ""
            for i in range(0, len(data['alive'])):
                ptinfo += f"{i}: <@{data['alive'][i]}>\n"
                be_voted_by_people.append(0)
            
            await ctx.send(f'眾人開始討論並投票`+/vote <number>`\n'+
                        f'{ptinfo}')
            l = len(data['alive'])
            while(True):
                await asyncio.sleep(5)
                with open('data.json', 'r') as jdata:
                    data = json.load(jdata)
                if len(data['people_vote']) == l:
                        break

            for i in data['people_vote']:
                be_voted_by_people[i[1]] += 1
            max = 0
            for i in be_voted_by_people:
                if i > max:
                    max = i
            exile = []
            print("be_voted_by_people", be_voted_by_people)
            print("exile", exile)
            l = len(be_voted_by_people)
            for i in range(l):
                if be_voted_by_people[i] == max:
                    exile.append(i)
            exile = random.choice(exile)
            print("exile", exile)
            exile = data['alive'][exile]
            await ctx.send(f"投票結束\n"+
                           f"<@{exile}> 被放逐了")
            while True:
                finded = False
                        
                for j in range(len(data['alive'])):
                    if data['alive'][j] == exile:
                        del data['alive'][j]
                        break
                    
                for j in range(len(data['witch_list'])):
                    if data['witch_list'][j][0] == exile:
                        del data['witch_list'][j]
                        finded = True
                        break
                if finded:
                    break
                for j in range(len(data['seer_list'])):
                    if data['seer_list'][j][0] == exile:
                        del data['seer_list'][j]
                        finded = True
                        break
                if finded:
                    break
                for j in range(len(data['villager_list'])):
                    if data['villager_list'][j] == exile:
                        del data['villager_list'][j]
                        finded = True
                        break
                if finded:
                    break
                for j in range(len(data['werewolf_list'])):
                    if data['werewolf_list'][j] == exile:
                        del data['werewolf_list'][j]
                        finded = True
                        break
                if finded:
                    break
            with open('data.json', 'w') as dt:
                json.dump(data, dt, indent=1)

            gq=False
            bq=False
            if len(data['villager_list']) or len(data['seer_list']) or len(data['witch_list']):
                gq = True
            if len(data['werewolf_list']):
                bq = True
            
            if gq==True and bq==False:
                await ctx.send("GAME OVER: Good Guys Win!!")
                return
            if bq==True and gq==False:
                await ctx.send("GAME OVER: Bad Guys Win!!")
                return
        

async def setup(bot):
    await bot.add_cog(Main(bot))
