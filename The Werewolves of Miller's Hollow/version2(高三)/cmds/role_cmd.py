# discord mods
import discord
from discord.ext import commands

# other mods
import json
import asyncio

# my mods
from core.classes import myCog
def Open() -> dict:
    with open('data.json', 'r') as dt:
        return json.load(dt)
def Dump(data: dict):
    with open('data.json', 'w') as dt:
        json.dump(data, dt, indent=1)

class Kill(discord.ui.Select):
    def __init__(self, bot):
        self.bot = bot
        placeholder="Select an option"
        min_values=1
        max_values=1
        options = []
        data = Open()
        for id in data['alive']:
            id = int(id)
            name = bot.get_user(id)
            name = name.name
            options.append(discord.SelectOption(label=name, value=id, description=""))
        super().__init__(placeholder=placeholder,min_values=min_values,max_values=max_values,options=options)
    async def callback(self, interaction: discord.Interaction):
        chosen = int(self.values[0])
        user = interaction.user
        print('chosen =', chosen, 'user =', user)

        data = Open()
        if user.id not in data['werewolf_list']:
            await user.send("錯誤,可能因為逾時,error code: CmdRolecmdKillCallback001'", ephemeral=True)
            return
        if data['current_progress'] != "werewolves voting":
            await user.send("錯誤,可能因為逾時,error code: CmdRolecmdKillCallback002'", ephemeral=True)
            return
        data['werewolves_voting'][user.id] = chosen
        Dump(data)
        await user.send("目標已選定")
class KillView(discord.ui.View):
    def __init__(self, *, timeout = 300, bot):
        super().__init__(timeout=timeout)
        self.add_item(Kill(bot=bot))

class Poison(discord.ui.Select):
    def __init__(self, bot):
        self.bot = bot
        placeholder="Select an option"
        min_values=1
        max_values=1
        options=[
            discord.SelectOption(label="I don't want to use the poison now", value="Null", description="You can use the poison in the next turn maybe.")
        ]
        data = Open()
        killed_by_werewolves = int( list( data['killed'].keys() )[0] )
        for id in data['alive']:
            if id == killed_by_werewolves: continue
            name = bot.get_user(id)
            name = name.name
            options.append(discord.SelectOption(label=name, value=str(id), description=""))
        super().__init__(placeholder=placeholder,min_values=min_values,max_values=max_values,options=options)
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        id = user.id
        value = self.values[0]
        data = Open()
        if value == "Null":
            data['witches_use_poisons_on'][id] = -1
            await user.send("你將不使用毒藥")
            Dump(data)
            return
        else:
            data['witches_use_poisons_on'][f"{id}"] = value
            await user.send(f"你將對<@{value}>使用毒藥")
            Dump(data)
class PoisonView(discord.ui.View):
    def __init__(self, *, timeout = 300, bot):
        super().__init__(timeout=timeout)
        self.add_item(Poison(bot=bot))

class Antidote(discord.ui.View):
    def __init__(self, *, timeout=300, bot, RoleCmd):
        self.bot = bot
        self.RoleCmd = RoleCmd
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Yes", style=discord.ButtonStyle.green)
    async def yes(self, interaction: discord.Interaction, button: discord.Button):
        user = interaction.user
        id = user.id
        data = Open()
        if data['current_progress'] != "witches/seers casting the spells":
            await user.send("錯誤,可能因為逾時,error code: CmdsRolecmdAntidoteYes001")
            return
        data['witches_use_antidotes_on'][id] = True    
        await user.send("你將對他使用解藥")
        Dump(data)
        await self.RoleCmd.witch_poison()

    @discord.ui.button(label="No", style=discord.ButtonStyle.red)
    async def no(self, interaction: discord.Interaction, button: discord.Button):
        user = interaction.user
        id = user.id
        data = Open()
        if data['current_progress'] != "witches/seers casting the spells":
            await user.send("錯誤,可能因為逾時,error code: CmdsRolecmdAntidoteNo001")
            return
        data['witches_use_antidotes_on'][id] = False
        await user.send("你將不會對他使用解藥")
        Dump(data)
        await self.RoleCmd.witch_poison()

class Seer(discord.ui.Select):
    def __init__(self, bot):
        self.bot = bot
        placeholder = "Select an option"
        min_values=1
        max_values=1
        options = []
        data = Open()
        for id in data['alive']:
            id = int(id)
            user = bot.get_user(id)
            name = user.name
            options.append(discord.SelectOption(label=name, value=id, description=""))
        super().__init__(
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            options=options
        )
    async def callback(self, interaction: discord.Interaction):
        id = int(self.values[0])
        user = interaction.user
        data = Open()
        if data['seer_list'].get(f"{user.id}") == True:
            await interaction.response.send_message("今晚你已經使用過技能", ephemeral=True)
            return
        else:
            identify = ""
            if id in data['villager_list']: identify = "平民"
            elif id in data['werewolf_list']: identify = "狼人"
            elif f"{id}" in data['seer_list']: identify = "預言家"
            elif f"{id}" in data['witch_list']: identify = "巫師"
            else: identify = "error code: CmdsRolecmdSeerCallback001"
            await user.send(f"<@{id}>的身分是'{identify}'")
            data['seer_list'][f"{user.id}"] = True
            data['seer_check'].append(user.id)
            Dump(data)
class SeerView(discord.ui.View):
    def __init__(self, *, timeout = 180, bot):
        super().__init__(timeout=timeout)
        self.add_item(Seer(bot=bot))

class SpeakingOverView(discord.ui.View):
    def __init__(self, *, timeout=300):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="我說完了", style=discord.ButtonStyle.green)
    async def button(self, interaction: discord.Interaction, button: discord.Button):
        user = interaction.user
        id = user.id
        data = Open()
        it = data['alive'].index( data['speaking'] )
        try:
            if not data['alive'].index(id) == it:
                await interaction.response.send_message(content="錯誤，可能因為逾時或尚未輪到您,error code: CmdsRolecmdSpeakingOverViewButton001", ephemeral=True)
                return
        except:
            await interaction.response.send_message(content="錯誤，你不在遊戲內，可能因為逾時或你被淘汰了", ephemeral=True)
        if it+1 >= len( data['alive'] ):
            data['speaking'] = -1
            Dump(data)
            return
        data['speaking'] = data['alive'][it+1]
        Dump(data)

class Voting(discord.ui.Select):
    def __init__(self, bot):
        placeholder="Select an option"
        min_values=1
        max_values=1
        options = []
        data = Open()
        for id in data['alive']:
            id = int(id)
            name = bot.get_user(id)
            name = name.name
            options.append(discord.SelectOption(label=name, value=id, description=""))
        super().__init__(placeholder=placeholder,min_values=min_values,max_values=max_values,options=options)
    async def callback(self, interaction: discord.Interaction):
        chosen = int(self.values[0])
        user = interaction.user
        print('chosen =', chosen, 'user =', user)

        data = Open()
        if user.id not in data['alive']:
            await user.send("錯誤,可能因為逾時,error code: CmdRolecmdVotingCallback001'", ephemeral=True)
            return
        if data['current_progress'] != "people voting":
            await user.send("錯誤,可能因為逾時,error code: CmdRolecmdVotingCallback002'", ephemeral=True)
            return
        data['people_voting'][user.id] = chosen
        Dump(data)
        await user.send("目標已選定")
class VotingView(discord.ui.View):
    def __init__(self, *, timeout = 300, bot):
        super().__init__(timeout=timeout)
        self.add_item(Voting(bot=bot))

# =================================================================

class Role_Cmd:
    def __init__(self, bot):
        self.bot = bot

    async def werewolf(self):
        data = Open()
        
        for id in data['werewolf_list']:
            id = int(id)
            werewolf = self.bot.get_user(id)
            await werewolf.send("Now, is time to discuss with your pack who to kill", view=KillView(bot=self.bot))

    async def witch_antidote(self, RoleCmd):
        data = Open()
        killed = list(data['killed'].keys())[0]
        if data['killed'][killed] != "werewolves": 
            print("error code: CmdsRolecmdCmdsWitch001")
            return
        killed = int(killed)
        for id in data['witch_list']:
            id = int(id)
            witch = self.bot.get_user(id)
            if killed == id: 
                await witch.send("您已被狼人殺害, 因此無法施法")
                data['witches_use_poisons_on'][id] = -1
                data['witches_use_antidotes_on'][id] = False
                Dump(data)
                continue
            await witch.send(f"<@{killed}>被狼人殺了，你要對他使用解藥嗎?", view=Antidote(bot=self.bot, RoleCmd = RoleCmd))

    async def witch_poison(self):
        data = Open()
        for id in data['witch_list']:
            id = int(id)
            witch = self.bot.get_user(id)
            if data['witches_use_antidotes_on'].get(str(id)) == True:
                await witch.send("您今晚已使用過解藥, 因此無法再使用毒藥")
                data['witches_use_poisons_on'][f"{id}"] = -1
                Dump(data)
                continue
            else:
                await witch.send("請選擇下毒對象", view=PoisonView(bot=self.bot))

    async def check(self):
        data = Open()
        for id in data['seer_list']:
            id = int(id)
            seer = self.bot.get_user(id)
            await seer.send("請選擇查驗對象", view=SeerView(bot=self.bot))
    
    async def speaking(self, ctx: commands.Context):
        data = Open()
        data['speaking'] = data['alive'][0]
        Dump(data)
        for id in data['alive']:
            await ctx.send(f"請<@{id}>發言，完畢後請按下按鈕", view = SpeakingOverView())
            while True:
                await asyncio.sleep(4)
                data = Open()
                if id != data['speaking']:
                    break

    async def voting(self):
        data = Open()
        data['people_voting'] = {}
        for id in data['alive']:
            survivor = self.bot.get_user(id)
            await survivor.send("請選擇要票死的對象", view = VotingView(bot=self.bot))
        Dump(data)

class Cmds(myCog):
    @commands.Cog.listener()
    async def on_ready(self):
        pass
    
    @commands.Cog.listener("on_message")
    async def discussion(self, message: discord.Message):
        if (not message.content.startswith('~~')) or (message.author == self.bot.user):
            return
        author = message.author
        author_id = author.id
        data = Open()
        if (message.content[2:].isspace()):
            if message.channel == None:
                await author.send("錯誤，訊息不可為空, error code: CmdsRolecmdCmdsDiscussion001", reference=message)
                return
            else:
                await message.channel.send("錯誤，訊息不可為空, error code: CmdsRolecmdCmdsDiscussion002", reference=message)
                return
        if author_id not in data['werewolf_list']: 
            if message.guild == None: 
                if data['current_progress'] not in ["night", "werewolves voting"]: 
                    await message.channel.send("錯誤，可能因為逾時, error code: CmdsRolecmdCmdsDiscussion003", reference=message)
                    return
            else: 
                await message.channel.send("權限錯誤，可能因為逾時, error code: CmdsRolecmdCmdsDiscussion004", reference=message)
                return
        content = message.content[2:]
        for id in data['werewolf_list']:
            if author_id == id: 
                await message.author.send("傳送成功", reference=message)
                continue
            werewolf = self.bot.get_user(id)
            em = discord.Embed(
                color=0xcd853f,
                title=f"@{author.name} Say:", 
                description=content
            )
            await werewolf.send(embed = em)




async def setup(bot):
    await bot.add_cog(Cmds(bot))