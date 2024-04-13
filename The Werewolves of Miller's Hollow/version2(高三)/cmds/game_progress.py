### main game progress python file ###
# discord mods
import discord
from discord.ext import commands

# other mods
import json
import random
import asyncio

# my mods
from core.classes import myCog
from cmds.role_cmd import Role_Cmd as role_cmds


class Progress(myCog):
    def open(self):
        with open('data.json', 'r') as dt:
            return json.load(dt)
    def dump(self, data):
        with open('data.json', 'w') as dt:
            json.dump(data, dt, indent=1)

    async def start_game(self, ctx: commands.Context):
# initialize
        Role_Cmd = role_cmds(self.bot)
        data = self.open()

        data['villager_list'] = []
        data['werewolf_list'] = []
        data['seer_list'] = {}
        data['witch_list'] = {}
        data['tell_everyone_the_true'] = ""

        self.dump(data)
# check the number of characters 
        if data['seer_number'] + data['witch_number'] == 0:
            await ctx.send("提示: 沒有神職人員")
        if data['villager_number'] == 0:
            await ctx.send("提示: 沒有平民")
        if data['werewolf_number'] == 0:
            await ctx.send("錯誤: 沒有狼人")
            return
        if data['seer_number'] + data['witch_number'] + data['villager_number'] == 0:
            await ctx.send("錯誤: 好人陣營人數為零")
            return
#role assigning
        t_villager_number = data['villager_number']
        t_seer_number = data['seer_number']
        t_witch_number = data['witch_number']
        t_werewolf_number = data['werewolf_number']
        print('t_villager_number = ', t_villager_number)
        print('t_seer_number = ', t_seer_number)
        print('t_witch_number = ', t_witch_number)
        print('t_werewolf_number = ', t_werewolf_number)
        i = 0
        while i < (len(data['player_id'])):
        # choose the list that is empty first
            empty_list = []
            if len(data['villager_list']) == 0 and t_villager_number != 0:
                empty_list.append("villager")
            if len(data['seer_list'])     == 0 and t_seer_number     != 0:
                empty_list.append("seer")
            if len(data['witch_list'])    == 0 and t_witch_number    != 0:
                empty_list.append("witch")
            if len(data['werewolf_list']) == 0 and t_werewolf_number != 0:
                empty_list.append("werewolf")
            print("empty_list:", empty_list)
            if len(empty_list) != 0:
                mth = random.choice(empty_list)
                tof = True
                if mth == "villager":
                    tof = False
                    t_villager_number -= 1
                    print('choose villager by empty')
                    data['villager_list'].append(data['player_id'][i])
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> 是 `平民`\n"
                elif mth == "werewolf":
                    tof = False
                    t_werewolf_number -= 1
                    print('choose werewolf by empty')
                    data['werewolf_list'].append(data['player_id'][i])
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> 是 `狼人`\n"
                elif mth == "seer":
                    tof = False
                    t_seer_number -= 1
                    print('choose seer by empty')
                    data['seer_list'][data['player_id'][i]] = False
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> 是 `預言家`\n"
                elif mth == "witch":
                    tof = False
                    t_witch_number -= 1
                    print('choose witch by empty')
                    data['witch_list'][data['player_id'][i]] = {"has_antidote": True, "has_poison": True}
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> 是 `巫師`\n"
                if tof:
                    print("===! ERROR !===")
                i += 1
                continue
        # continue if there are no more empty list
            mth = random.randrange(0, 3)
            crr = -1
            # 3 type of random system
            if mth == 0:
                crr = random.randrange(1, 5)
            elif mth == 1:
                crr = random.choice([3,4,2,1])
            elif mth == 2:
                tmp = random.randrange(137)
                crr = (tmp*3-9)%4+1

            # according the result, assign players to corresponding roles
            if crr == 1:
                if t_villager_number == 0:
                    print('-1')
                else:
                    t_villager_number -= 1
                    print('choose villager')
                    data['villager_list'].append(data['player_id'][i])
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> 是 `平民`\n"
                    i += 1
            elif crr == 2:
                if t_seer_number == 0:
                    print('-1')
                else:
                    t_seer_number -= 1
                    print('choose seer')
                    data['seer_list'][data['player_id']] = False
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> 是 `預言家`\n"
                    i += 1
            elif crr == 3:
                if t_witch_number == 0:
                    print('-1')
                else:
                    t_witch_number -= 1
                    print('choose witch')
                    data['witch_list'][data['player_id']] = {"has_antidote": True, "has_poison": True}
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> 是 `巫師`\n"
                    i += 1
            elif crr == 4:
                if t_werewolf_number == 0:
                    print('-1')
                else:
                    t_werewolf_number -= 1
                    print('choose werewolf')
                    data['werewolf_list'].append(data['player_id'][i])
                    data['tell_everyone_the_true']+=f"<@{data['player_id'][i]}> 是 `狼人`\n"
                    i += 1
        self.dump(data)
        print("stop")

# inform players of their roles
        for i in data['villager_list']:
            print('send villager')
            a = self.bot.get_user(i)
            await a.send("您在本局中的角色是平民")
        for i in data['seer_list']:
            print('send seer')
            a = self.bot.get_user(i)
            await a.send("您在本局中的角色是預言家")
        for i in data['witch_list']:
            print('send witch')
            a = self.bot.get_user(i)
            await a.send("您在本局中的角色是女巫")
        for i in data['werewolf_list']:
            print('send werewolf')
            a = self.bot.get_user(i)
            await a.send("您在本局中的角色是狼人")
### prepare to start
        data['alive'] = data['player_id']

        self.dump(data)
        await ctx.send("遊戲開始")
# enter the game
        while True:
            with open('data.json','r') as dt:
                data = json.load(dt)
# night falls
            data['current_progress'] = "night"
            await ctx.send(f"夜晚降臨")
# initialize data
            data['werewolves_voting'] = {}
            data['killed'] = {}
            self.dump(data)
# dealing with werewolves voting
            await ctx.send("狼人開始投票")
            data['current_progress'] = "werewolves voting"
            await Role_Cmd.werewolf()
            self.dump(data)

            while(True):
                await asyncio.sleep(4)
                data = self.open()
                if len(data['werewolves_voting']) == len(data['werewolf_list']):
                    data['current_progress'] = "counting werewolves' votes"
                    self.dump(data)
                    break

            data = self.open()
            for i in data['werewolf_list']:
                werewolf = self.bot.get_user(i)
                await werewolf.send("投票結束")

            werewolf_voting_result = {}
            get_most_voting = []
            most_voting = 0
            for id in data['werewolves_voting']:
                obj = data['werewolves_voting'].get(id)
                if werewolf_voting_result.get(obj) is None:
                    werewolf_voting_result[obj] = 0
                else:
                    werewolf_voting_result[obj] += 1
                if (werewolf_voting_result[obj] > most_voting):
                    most_voting = werewolf_voting_result[obj]
                    get_most_voting = [obj]
                elif (werewolf_voting_result[obj] == most_voting):
                    get_most_voting.append(obj)
            get_most_voting = random.choice(get_most_voting)
            data['killed'][get_most_voting] = 'werewolves'
            self.dump(data)
# dealing with witches and seers casting
    # initialize data
            data = self.open()
            for i in data['seer_list']:
                data['seer_list'][i] = False
            data['seer_check'] = []
            data['witches_use_poisons_on'] = {}
            data['witches_use_antidotes_on'] = {}

            data['current_progress'] = "witches/seers casting the spells"
            self.dump(data)

            await Role_Cmd.witch_antidote(RoleCmd=Role_Cmd)
            await Role_Cmd.check()

            while True:
                await asyncio.sleep(4)
                data = self.open()
                if len(data['witches_use_poisons_on']) == len(data['witch_list']) and len(data['witches_use_antidotes_on']) == len(data['witch_list']) and len(data['seer_check']) == len(data['seer_list']):
                    break
    # change the data
            for id in data['witches_use_antidotes_on']:
                obj = data['witches_use_antidotes_on'][id]
                if obj:
                    data['witch_list'][id]['has_antidote'] = False
                    data['killed'] = {}
            for id in data['witches_use_poisons_on']:
                if data['witches_use_poisons_on'][id] != -1:
                    data['witch_list'][id]['has_poison'] = False
                    data['killed'][data['witches_use_poisons_on'][id]] = 'witch'
            data['current_progress'] = "dealing with witches/seers casting"
            self.dump(data)
# day time
            await ctx.send('白晝降臨')
            data = self.open()
            if len(data['killed']) != 0:
                for killed_id in data['killed']:
                    killed_id = int(killed_id)
                    try: del data['alive'][ data['alive'].index(killed_id) ]
                    except: pass
                    try: del data['villager_list'][ data['villager_list'].index(killed_id) ]
                    except: pass
                    try: del data['seer_list'][killed_id]
                    except: pass
                    try: del data['witch_list'][killed_id]
                    except: pass
                    try: del data['werewolf_list'][ data['werewolf_list'].index(killed_id) ]
                    except: pass

                    await ctx.send(f"昨晚 <@{killed_id }> 被 `{data['killed'][ str(killed_id) ]}` 殺了")
            else: await ctx.send(f'昨晚安然度過')
            data['current_progress'] = "people voting"
            self.dump(data)
# check win or lose
            data = self.open()
            still_have_good_gay = False
            still_have_werewolf = False
            if len(data['villager_list']) or len(data['seer_list']) or len(data['witch_list']):
                still_have_good_gay = True
            if len(data['werewolf_list']):
                still_have_werewolf = True
            
            rst = self.who_win()
            if rst == 'g':
                await ctx.send("GAME OVER: 好人方獲勝!!")
                data['current_progress'] = "end_game"
                self.dump(data)
                return
            elif rst == 'b':
                await ctx.send("GAME OVER: 狼人方獲勝!!")
                data['current_progress'] = "end_game"
                self.dump(data)
                return
            elif rst == 'e' or rst == None:
                await ctx.send("game over with an ERROR: I don't Know why")
                data['current_progress'] = "end_game"
                self.dump(data)
                return
            data['current_progress'] = "people voting"
# people discussing and voting
            await ctx.send(f'眾人開始討論')
            await Role_Cmd.speaking(ctx)
            while True:
                await asyncio.sleep(5)
                data = self.open()
                if data['speaking'] == -1: break
            
            await ctx.send(f'眾人開始投票')
            await Role_Cmd.voting()

            while True:
                await asyncio.sleep(5)
                data = self.open()
                if len(data['people_voting']) == len(data['alive']):
                        break

            people_voting_result = {}
            get_most_voting = []
            most_voting = 0
            for id in data['people_voting']:
                obj = data['people_voting'].get(id)
                if people_voting_result.get(obj) is None:
                    people_voting_result[obj] = 0
                else:
                    people_voting_result[obj] += 1
                    if (people_voting_result[obj] > most_voting):
                        most_voting = people_voting_result[obj]
                        get_most_voting = [obj]
                    elif (people_voting_result[obj] == most_voting):
                        get_most_voting.append(obj)
            exiled = random.choice(get_most_voting)
            await ctx.send(f"投票結束\n"+f"<@{exiled}> 被放逐了")
            data = self.open()
            exiled = int(exiled)
            try: del data['alive'][ data['alive'].index(exiled) ]
            except: pass
            try: del data['villager_list'][ data['villager_list'].index(exiled) ]
            except: pass
            try: del data['seer_list'][exiled]
            except: pass
            try: del data['witch_list'][exiled]
            except: pass
            try: del data['werewolf_list'][ data['werewolf_list'].index(exiled) ]
            except: pass
            self.dump(data)

            rst = self.who_win()
            if rst == 'g':
                await ctx.send("GAME OVER: 好人方獲勝!!")
                data['current_progress'] = "end_game"
                self.dump(data)
                return
            elif rst == 'b':
                await ctx.send("GAME OVER: 狼人方獲勝!!")
                data['current_progress'] = "end_game"
                self.dump(data)
                return
            elif rst == 'e' or rst == None:
                await ctx.send("game over with an ERROR: I don't Know why")
                data['current_progress'] = "end_game"
                self.dump(data)
                return

    def who_win(self):
            data = self.open()
            still_have_good_gay = False
            still_have_werewolf = False
            if len(data['villager_list']) + len(data['seer_list']) + len(data['witch_list']):
                still_have_good_gay = True
            if len(data['werewolf_list']):
                still_have_werewolf = True
            
            if still_have_good_gay==True and still_have_werewolf==False:
                return 'g' # good gays
            elif still_have_werewolf==True and still_have_good_gay==False:
                return 'b' # bad gays
            elif still_have_werewolf==False and still_have_good_gay==False:
                return 'e' # error
            else:
                return 'c' # continue

    @commands.command()
    async def start(self, ctx: commands.Context):
        if ctx.guild == None:
            await ctx.send("Error you need to use this function in a guild!")
            return
        await self.start_game(ctx)
        data = self.open()
        await ctx.send(data['tell_everyone_the_true'])

async def setup(bot):
    await bot.add_cog(Progress(bot))