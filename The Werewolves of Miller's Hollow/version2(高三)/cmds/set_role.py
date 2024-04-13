# discord mods
import discord
from discord.ext import commands

# other mods
import json
import asyncio

# my mods
from core.classes import myCog

def add_selectOption(options: list) -> list:
    with open('data.json', 'r') as dt:
        data = json.load(dt)
    for i in range( len(data['player_id']) + 1 ):
        options.append( discord.SelectOption(label=f"{i}", value=f"{i}", description="") )
    return options

async def my_callback(interaction: discord.Interaction, value: int, role: str):
    with open('data.json', 'r') as dt:
        data = json.load(dt)
    data[f'{role}_number'] = value
    with open('data.json', 'w') as dt:
        json.dump(data, dt, indent=1)
    await interaction.response.send_message(f"Successfully set the number of ``{role}`` to ``{value}``", ephemeral=True)


class set_villager(discord.ui.Select):
    def __init__(self):
        placeholder = "Select an option"
        min_values=1
        max_values=1
        options = add_selectOption([])
        super().__init__(placeholder=placeholder,min_values=min_values,max_values=max_values,options=options)
    async def callback(self, interaction: discord.Interaction):
        await my_callback(interaction, int(self.values[0]), "villager")
class set_villager_view(discord.ui.View):
    def __init__(self, *, timeout = 180, value = None):
        super().__init__(timeout=timeout)
        self.add_item(set_villager())
class set_seer(discord.ui.Select):
    def __init__(self):
        placeholder = "Select an option"
        min_values=1
        max_values=1
        options = add_selectOption([])
        super().__init__(placeholder=placeholder,min_values=min_values,max_values=max_values,options=options)
    async def callback(self, interaction: discord.Interaction):
        await my_callback(interaction, int(self.values[0]), "seer")
class set_seer_view(discord.ui.View):
    def __init__(self, *, timeout = 180, value = None):
        super().__init__(timeout=timeout)
        self.add_item(set_seer())
class set_witch(discord.ui.Select):
    def __init__(self):
        placeholder = "Select an option"
        min_values=1
        max_values=1
        options = add_selectOption([])
        super().__init__(placeholder=placeholder,min_values=min_values,max_values=max_values,options=options)
    async def callback(self, interaction: discord.Interaction):
        await my_callback(interaction, int(self.values[0]), "witch")
class set_witch_view(discord.ui.View):
    def __init__(self, *, timeout = 180, value = None):
        super().__init__(timeout=timeout)
        self.add_item(set_witch())
class set_werewolf(discord.ui.Select):
    def __init__(self):
        placeholder = "Select an option"
        min_values=1
        max_values=1
        options = add_selectOption([])
        super().__init__(placeholder=placeholder,min_values=min_values,max_values=max_values,options=options)
    async def callback(self, interaction: discord.Interaction):
        await my_callback(interaction, int(self.values[0]), "werewolf")
class set_werewolf_view(discord.ui.View):
    def __init__(self, *, timeout = 180, value = None):
        super().__init__(timeout=timeout)
        self.add_item(set_werewolf())

class set_role(discord.ui.Select):
    def __init__(self):
        placeholder = "請選擇要變更數量的角色"
        min_values=1
        max_values=1
        options = [
                discord.SelectOption(label="Villager", value="villager", description="set the number of villager"),
                discord.SelectOption(label="Seer", value="seer", description="set the number of seer"),
                discord.SelectOption(label="Witch", value="witch", description="set the number of witch"),
                discord.SelectOption(label="Werewolf", value="werewolf", description="set the number of werewolf")
        ]
        super().__init__(placeholder=placeholder,min_values=min_values,max_values=max_values,options=options)
    async def callback(self, interaction: discord.Interaction):
        value = self.values[0]
        if value == "villager":
            await interaction.response.send_message("請選擇 平民 的數量", view=set_villager_view(), ephemeral=True)
        elif value == "seer":
            await interaction.response.send_message("請選擇 預言家 的數量", view=set_seer_view(), ephemeral=True)
        elif value == "witch":
            await interaction.response.send_message("請選擇 巫師 的數量", view=set_witch_view(), ephemeral=True)
        elif value == "werewolf":
            await interaction.response.send_message("請選擇 狼人 的數量", view=set_werewolf_view(), ephemeral=True)
class set_role_view(discord.ui.View):
    def __init__(self, *, timeout = 180, value = None):
        super().__init__(timeout=timeout)
        self.add_item(set_role())

class SetRole(myCog):
    @commands.command()
    async def set_role(self, ctx):
        await ctx.send("Thanks for calling ``Set Role``", view=set_role_view())

async def setup(bot):
    await bot.add_cog(SetRole(bot))