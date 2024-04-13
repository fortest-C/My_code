### Main Menu ###
# discord mods
import discord
from discord.ext import commands

# other mods
import json
with open('setting.json', 'r') as st:
    setting = json.load(st)

# my mods
from core.classes import myCog
from cmds.introduction import Functions
Introduction_Functions = Functions()
from cmds.player_data import Functions
PlayerData_Functions = Functions()



class Embeds:
    head_icon = discord.File("head_icon.png", filename="head_icon.png")

    WhoIAm = discord.Embed(
        color=0x9400d3,
        title="我是誰?",
        description=f"我是一台狼人殺機器人，目前版本:{setting['version']}!")
    WhoIAm.set_author(name="The_Werewolves_of_Miller_coolooc", icon_url="attachment://head_icon.png")

    WhatIsTheWerewolvesOfMiller = discord.Embed(
        color=0xb22222,
        title="點我了解更詳細規則",
        url="",
        description="我還在開發中，僅支持基本角色，利用``+/introduction``指令了解更多吧!"
    )

    HowToStart = discord.Embed(
        color=0x191970,
        title="如何開始遊戲",
        description="",
    )
    HowToStart.add_field(inline=False, name="基本設定", value="使用``+/player_data``來加入/退出遊戲，並設定遊戲基本數值")
    HowToStart.add_field(inline=False, name="開始遊戲", value="使用``+/start``來開始遊戲，我將會為你們進行遊戲流程")
    HowToStart.add_field(inline=False, name="遊戲流程", value="遊戲開始後會透過訊息來通知每個玩家各自扮演的角色, 記得檢查我的私訊OwO\n"+
                                                                      "如果你有職業的話，請透過私訊中的提示使用你的技能吧\n"+
                                                                      "白天時，所有倖存玩家會輪流發言，發言完畢後，記得到``text channel``中按下``我說完了``按鈕，遊戲才會繼續進行(每個玩家請在5分鐘內按下按鈕)\n"+
                                                                      "接著，所有倖存玩家請到我的私訊，選擇要票死的玩家\n"+
                                                                      "不斷重複以上步驟，直至有一方獲得勝利!")

class Selects:
    class MainSelect(discord.ui.Select):
        def __init__(self, ctx):
            placeholder = "What can I help you?"
            min_values=1
            max_values=1
            options = [
                    discord.SelectOption(label="你是誰", description="快來看看我是做什麼的吧!", value="WhoAreYou"),
                    discord.SelectOption(label="狼人殺是甚麼東西，能吃嗎", description="不行。但想快速入門，點我就對了!", value="WhatIsTheWerewolvesOfMiller'sHollow"),
                    discord.SelectOption(label="廢話真多，快告訴我怎麼開始", description="別急別急，聽我娓娓道來!", value="HowToStart"),
            ]
            super().__init__(placeholder=placeholder,min_values=min_values,max_values=max_values,options=options)
        async def callback(self, interaction: discord.Interaction):
            values = self.values
            if "WhoAreYou" in values:
                await interaction.response.send_message(embed=Embeds().WhoIAm, ephemeral=True)
            elif "WhatIsTheWerewolvesOfMiller'sHollow" in values:
                await interaction.response.send_message(embed=Embeds().WhatIsTheWerewolvesOfMiller, view=Views.IntroductionButton(), ephemeral=True)
            elif "HowToStart" in values:
                await interaction.response.send_message(embed=Embeds().HowToStart, view=Views.PlayerDataButton(), ephemeral=True)
    

class Views:
    class MainSelectView(discord.ui.View):
        def __init__(self, *, timeout = 180, ctx: commands.Context):
            super().__init__(timeout=timeout)
            self.add_item(Selects.MainSelect(ctx=ctx))

    class IntroductionButton(discord.ui.View):
        def __init__(self, *, timeout=50):
            super().__init__(timeout=timeout)
        @discord.ui.button(label="run +/introduction", style=discord.ButtonStyle.red)
        async def button1(self, interaction: discord.Interaction, button: discord.Button):
            await Introduction_Functions.SendIntroductionView(interaction)

    class PlayerDataButton(discord.ui.View):
        def __init__(self, *, timeout=50):
            super().__init__(timeout=timeout)
        @discord.ui.button(label="run +/player_data", style=discord.ButtonStyle.red)
        async def button1(self, interaction: discord.Interaction, button: discord.Button):
            await PlayerData_Functions.SendPlayerDataView(interaction)


# =================================================================
class MainMenu(myCog):
    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send("Thanks for calling ``HelpMenu``", view=Views.MainSelectView(ctx=ctx))

async def setup(bot):
    await bot.add_cog(MainMenu(bot))