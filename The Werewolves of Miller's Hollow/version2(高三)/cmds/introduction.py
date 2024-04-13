### introduce how to play ###
# discord mods
import discord
from discord.ext import commands

# other mods
import asyncio

# my mods
from core.classes import myCog


class Introduction(discord.ui.Select):
    def __init__(self):
        super().__init__(
            placeholder="What can I help you?",
            min_values=1,
            max_values=1,
                options=[
                    discord.SelectOption(label="Role", value="role", description="choose me to see what characters are available"),
                    discord.SelectOption(label="Rule", value="rule", description="choose me to see how to play"),
                    discord.SelectOption(label="Stop", value="stop", description="choose me to see how to force stop the game when you are playing"),
                ]
        )
    async def callback(self, interaction: discord.Interaction):
        values = self.values
        action = Action(interaction)
        if "role" in values:
            await action.role()
        elif "rule" in values:
            await action.rule()
        elif "stop" in values:
            await action.stop()
class Introduction_View(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Introduction())

class Action:
    def __init__(self, interaction: discord.Interaction):
        self.interaction = interaction

    async def role(self):
        interaction = self.interaction
        em = discord.Embed(
            color=0x9932cc,
            title="<:i_help:1066289043828133898> 角色說明",
            description="所有玩家將被分為兩個陣營\n"+
                        "率先殲滅敵對者獲勝"
        )
        goodTxt = open('./cmds/introduction/good.txt', 'r', encoding='utf-8')
        em.add_field(
            name="好人",
            value=goodTxt.read(),
            inline=False
        )
        badTxt = open('./cmds/introduction/bad.txt', 'r', encoding='utf-8')
        em.add_field(
            name="壞人",
            value=badTxt.read(),
            inline=False
        )
        await interaction.response.send_message(embed=em, ephemeral=True)
        goodTxt.close()
        badTxt.close()

    async def rule(self):
        interaction = self.interaction
        ruleTxt = open('./cmds/introduction/rule.txt', 'r', encoding='utf-8')
        em = discord.Embed(
            color=0xff8c00,
            title="<:i_help:1066289043828133898> 流程說明",
            description="獲勝方式: 率先殲滅敵對者獲勝"
        )
        em.add_field(
            name="流程",
            value=ruleTxt.read(),
            inline=False
        )
        await interaction.response.send_message(embed=em, ephemeral=True)
        ruleTxt.close()
        print('Successfully')

    async def stop(self):
        interaction = self.interaction
        em = discord.Embed(
            color=0x32cd32,
            title="<:i_help:1066289043828133898> 強制結束遊戲",
            description="使用命令以強制停止遊戲(command: `+/Stop_Game`)\n" +
                        "*注意: 本局資料將不復存在!"
        )
        await interaction.response.send_message(embed=em, ephemeral=True)

class Introduce(myCog):
    @commands.command()
    async def introduction(self, ctx):
        await Functions().SendIntroductionView(x=ctx)

class Functions:
    async def SendIntroductionView(self, x: commands.Context | discord.Interaction):
        if type(x) == commands.Context:
            await x.send("Thanks for calling ``Introduction``", view=Introduction_View())
        elif type(x) == discord.Interaction:
            await x.response.send_message("Thanks for calling ``Introduction``", view=Introduction_View(), ephemeral=True)
        else: print('error')

async def setup(bot):
    await bot.add_cog(Introduce(bot))