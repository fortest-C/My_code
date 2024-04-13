### to play ###
# discord mods
import discord
from discord.ext import commands

# other mods
import json

# my mods
from core.classes import myCog

class Menu(discord.ui.Select):
    def __init__(self):
        placeholder = "What can I help you?"
        min_values = 1
        max_values = 1
        options = [
            discord.SelectOption(label="Join", value="join", description="choose me to join the game"),
            discord.SelectOption(label="Quit", value="quit", description="choose me to quit the game"),
            discord.SelectOption(label="List", value="player_list", description="chose me to check player list"),
            discord.SelectOption(label="Delete", value="del_player_list", description="<BE CAREFUL>choose me to delete all the players from player list"),
            discord.SelectOption(label="Clean", value="clean_data", description="<BE CAREFUL>choose me to clean all data"),
            discord.SelectOption(label="Stop", value="stop_game", description="<BE CAREFUL>choose me to exit the game if you are playing")
        ]
        super().__init__(
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            options=options
        )
    async def callback(self, interaction: discord.Interaction):
        values = self.values
        action = Action(interaction)
        if "join" in values: await action.join()
        elif "quit" in values: await action.quit()
        elif "player_list" in values: await action.player_list()
        elif "del_player_list" in values: await action.del_player_list()
        elif "clean_data" in values: await action.clean_data()
        elif "stop_game" in values: await action.stop_game()
class Menu_View(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Menu())

def printString(data):
    printString = ""
    for i in range(len(data['player_name'])):
        printString += f"{i+1}: {data['player_name'][i]}\n"
    return printString

class Action:
    def __init__(self, interaction: discord.Interaction):
        self.interaction = interaction

    async def join(self):
        print('in join')
        interaction = self.interaction
        ID = interaction.user.id
        with open('data.json', 'r', encoding='utf-8') as dt:
            data = json.load(dt)
        if ID in data['player_id']:
            print('in if')
            await interaction.response.send_message(f"<@{ID}> 您已在玩家儲列中", ephemeral=True)

        else:
            print('in else')
            data['player_name'].append(interaction.user.name)
            data['player_id' ].append(ID)

            with open('data.json', 'w', encoding = "utf8") as dt:
                json.dump(data, dt, indent = 1)
            await interaction.response.send_message("<<<add successfully>>>\n"+ printString(data), ephemeral=False)

    async def quit(self):
        print("in quit")
        interaction = self.interaction
        ID = interaction.user.id

        with open('data.json', 'r', encoding='utf-8') as dt:
            data = json.load(dt)

        if ID not in data['player_id']:
            print("in if")
            await interaction.response.send_message(f"<@{ID}> 您未在玩家儲列中", ephemeral=True)

        else:
            print("in else")
            data['player_name'].remove(interaction.user.name)
            data['player_id'].remove(ID)

            with open('data.json', 'w', encoding = "utf8") as dt:
                json.dump(data, dt, indent = 1)
            await interaction.response.send_message("<<<delete successfully>>>\n" + printString(data), ephemeral=False)

    async def player_list(self):
        interaction = self.interaction
        with open('data.json', 'r', encoding = "utf8") as dt:
            data = json.load(dt)
        string = f"目前玩家:\n{printString(data)}\nvillager_number: {data['villager_number']}\nseer_number: {data['seer_number']}\nwitch_number: {data['witch_number']}\nwerewolf_number: {data['werewolf_number']}"
        await interaction.response.send_message(string, ephemeral=True)

    async def del_player_list(self):
        interaction = self.interaction
        with open('data.json', 'r', encoding = "utf8") as dt:
            data = json.load(dt)
        data['player_id'] = []
        data['player_name'] = []
        data['seer_list'] = {}
        data['witch_list'] = {}
        data['villager_list'] = []
        data['werewolf_list'] = []      
        with open('data.json', 'w') as dt:
            json.dump(data, dt, indent=1)
        await interaction.response.send_message("added player data have been received", ephemeral=False)

    async def clean_data(self):
        interaction = self.interaction
        with open('data.json', 'r', encoding = "utf8") as dt:
            data = json.load(dt)
        data['player_name'] = []
        data['player_id'] = []

        data['werewolf_number'] = 0
        data['villager_number'] = 0
        data['seer_number'] = 0
        data['witch_number'] = 0

        data['tell_everyone_the_true'] = ""

        data['villager_list'] = []
        data['seer_list'] = {}
        data['witch_list'] = {}
        data['werewolf_list'] = []

        data['seer_check'] = []
        data['witches_use_poisons_on'] = {}
        data['witches_use_antidotes_on'] = {}
        data['werewolves_voting'] = {}
        data['people_voting'] = {}

        data['alive'] = []
        data['killed'] = {}
        data['current_progress'] = ""
        data['speaking'] = 0

        with open('data.json', 'w') as dt:
            json.dump(data, dt, indent=1)
        await interaction.response.send_message("all data have been received", ephemeral=False)

class PlayerData(myCog):
    @commands.command()
    async def player_data(self, ctx):
        await Functions().SendPlayerDataView(x=ctx)
    
    @commands.command()
    async def stop_game(self):
        interaction = self.interaction
        await self.bot.unload_extension(f"cmds.main_game")
        print("unload main_game")
        await self.bot.load_extension(f"cmds.main_game")
        print("load main_game")
        await interaction.response.send_message("game stop successfully")

class Functions:
    async def SendPlayerDataView(self, x: commands.Context | discord.Interaction):
        if type(x) == commands.Context:
            await x.send("Thanks for calling ``Player Data``", view=Menu_View())
        elif type(x) == discord.Interaction:
            await x.response.send_message("Thanks for calling ``Player Data``", view=Menu_View(), ephemeral=True)
        else: print('error')
async def setup(bot):
    await bot.add_cog(PlayerData(bot))