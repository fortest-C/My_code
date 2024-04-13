# discord mods
import discord
from discord.ext import commands
from typing import List

# other mods

# my mods
from core.classes import myCog

class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="This is a label", style=discord.ButtonStyle.red)
    async def button1(self, interaction: discord.Interaction, button: discord.Button):
        await interaction.response.send_message("Hi There")


class Select1(discord.ui.Select):
    def __init__(self):
        placeholder = "Select an option"
        min_values=1
        max_values=1
        options = [
                discord.SelectOption(label="Select_1", value="select_1", description="Description_1"),
                discord.SelectOption(label="Select_2", value="select_2", description="Description_2"),
                discord.SelectOption(label="Select_3", value="select_3", description="Description_3")
        ]
        super().__init__(
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            options=options
        )
    async def callback(self, interaction: discord.Interaction):
        values = self.values
        if "select_1" in values:
            await interaction.response.send_message("You chose the first option")
        elif "select_2" in values:
            await interaction.response.send_message("You chose the second option (ephemeral)", ephemeral=True)
        elif "select_3" in values:
            await interaction.response.edit_message(content="You chose the third option (edit message)")

class Select2(discord.ui.Select):
    def __init__(self):
        placeholder = "Select an option"
        min_values=1
        max_values=1
        options = [
                discord.SelectOption(label="Select_1", value="select_1", description="Description_1")
        ]
        super().__init__(
            placeholder=placeholder,
            min_values=min_values,
            max_values=max_values,
            options=options
        )
    async def callback(self, interaction: discord.Interaction):
        values = self.values
        if "select_1" in values:
            await interaction.response.send_message("You chose the first option")
class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180, value = None):
        super().__init__(timeout=timeout)
        self.add_item(Select1())
        self.add_item(Select2())



class UiExample(myCog):

    @commands.command()
    async def button_1(self, ctx):
        await ctx.send("You Called a button", view=Buttons())

    @commands.command()
    async def select_1(self, ctx):
        await ctx.send("You Called a select",view=SelectView(value=None))

    @commands.command()
    async def embed(self, ctx):
        em = discord.Embed(
            title="This is a title",
            description="This is a description",
        )
        em.add_field(name="This is a name1", value="This is a value",inline=False)
        em.add_field(name="This is a name1", value="This is a value",inline=False)
        em1 = discord.Embed(
            title="This is a title",
            description="This is a description",
        )
        em1.add_field(name="This is a name", value="This is a value",inline=True)
        em1.add_field(name="This is a name", value="This is a value",inline=True)
        await ctx.send("This is a Embed", embed=em)
        await ctx.send("This is a Embed1", embed=em1)


async def setup(bot):
    await bot.add_cog(UiExample(bot))