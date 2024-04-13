import discord
from discord.ext import commands
from discord.ui import Select,View,Button

# other mods
import json
import asyncio
import random
from datetime import datetime
import logging

# my mods
from core.classes import myCog
with open('help_data.json' ,'r' ,encoding='utf8') as jdt:
    data = json.load(jdt)


class Rule_help(View):

    def __init__(self):
        with open('help_data.json' ,'r' ,encoding='utf8') as jdt:
            data = json.load(jdt)
        data['rule_page'] = 1
        with open('help_data.json' ,'w' ,encoding='utf8') as jdt:
            json.dump(data, jdt)

    rule_page1 = discord.Embed(title="Page 1" ,description="遊戲參與--透過指令加入或退出玩家儲列")
    rule_page1.add_field(name="加入遊戲"    ,value="透過<join>指令加入遊戲"   ,inline=False)
    rule_page1.add_field(name="退出遊戲"    ,value="透過<quit>指令退出遊戲"   ,inline=False)
    rule_page1.add_field(name="查詢玩家儲列" ,value="透過<player>查詢玩家儲列" ,inline=False)
    
    rule_page2 = discord.Embed(title="Page 2" ,description="遊戲基礎設定--角色數量設定")
    rule_page2.add_field(name="目前共有4種角色身分",
                value="分別為\n"+
                    "[狼人  巫師  預言家  村民]\n"+
                    "角色說明請透過<help>指令選取<角色說明>\n"+
                    "透過<help>指令選取<指令操作>取得設定數量指令",
                inline=False)
#=====================================================================================  UNFINISHED
    rule_page3 = discord.Embed(title="Page 3" ,description="遊戲開始--遊戲初始化完成, 進入遊戲" )
    rule_page3.add_field(name="" ,value="" ,inline=False)

    rule_page4 = discord.Embed(title="Page 4" ,description="第一個夜晚--月圓之時, 狼人化身"     )
    rule_page4.add_field(name="" ,value="" ,inline=False)

    @discord.ui.button(label="上一頁" ,style=discord.ButtonStyle.primary)
    async def back(self ,interaction: discord.Integration ,button: discord.Button):
        with open('help_data.json' ,'r' ,encoding='utf8') as jdt:
            data = json.load(jdt)
        data['rule_page'] -= 1
        if data['rule_page'] == 0:
            await interaction.delete()
        elif data['rule_page'] == 1:
            await interaction.response.edit_message(embed=self.rule_page1)
        elif data['rule_page'] == 2:
            await interaction.response.edit_message(embed=self.rule_page2)
        elif data['rule_page'] == 3:
            await interaction.response.edit_message(embed=self.rule_page3)
        else:
            logging.error('i dant know what happen in Rule_help.back()')
        with open('help_data.json' ,'w' ,encoding='utf8') as jdt:
            json.dump(data, jdt)
    
    @discord.ui.button(label="下一頁" ,style=discord.ButtonStyle.primary)
    async def next(self ,interaction: discord.Integration ,button: discord.Button):
        with open('help_data.json' ,'r' ,encoding='utf8') as jdt:
            data = json.load(jdt)
        data['rule_page'] += 1
        if data['rule_page'] == 1:
            await interaction.response.edit_message(embed=self.rule_page1)
        elif data['rule_page'] == 2:
            await interaction.response.edit_message(embed=self.rule_page2)
        elif data['rule_page'] == 3:
            await interaction.response.edit_message(embed=self.rule_page3)
        elif data['rule_page'] > 3:
            data['rule_page'] -= 1
        else:
            logging.error('i dant know what happen in Rule_help.next()')
        with open('help_data.json' ,'w' ,encoding='utf8') as jdt:
            json.dump(data, jdt)


class Role_help(View):

    ww = discord.Embed(title="狼人"   ,description="關於狼人的說明"   ,color= discord.Colour.light_grey())
    ww.add_field(name="刺殺",
                value="_小北百科顯示:\n"+
                      "狼人總是於夜晚成群出沒, 並且其鋒利的爪子具有使人一擊斃命的極高攻擊力_\n"+
                      "夜晚降臨時, 狼人們互認身分並討論殺害對象",
                inline=False)
    ww.add_field(name="投票權",
                value="可於白天時投給懷疑的對象或欲陷害的對象\n"+
                      "投票結束後, 票數最多的將被放逐, 並失去所有權力及技能",
                inline=False)
    
    wc = discord.Embed(title="巫師"   ,description="關於巫師的說明"   ,color= discord.Colour.purple())
    wc.add_field(name="救術",
                value="_每位巫師根據小北百科中的遠古文獻進行七七49天的釀造, 製造出極為珍稀且強效的藥水_\n"+
                      "__每位巫師僅能施用一次救術__\n"+
                      "夜晚降臨時, 女巫悄悄來到遭狼人殺害者身旁, 對其使用救術,\n"+
                      "然此藥效果極為強烈, 若短時間內被施加兩劑則吐血而亡",
                inline=False)
    wc.add_field(name="黑術",
                value="_每位巫師根據小北百科中的遠古文獻進行七七77天的釀造, 製造出極具毒性的珍稀藥水\n"+
                      "__每位巫師僅能施用一次黑術__\n"+
                      "夜晚降臨時, 女巫悄悄來到懷疑的對象身旁, 對其使用黑術,\n"+
                      "此藥效果極為強烈, 凡碰觸此藥者短時間內七竅出血而亡",
                inline=False)
    wc.add_field(name="投票權",
                value="可於白天時投給懷疑的對象或欲陷害的對象\n"+
                      "投票結束後, 票數最多的將被放逐, 並失去所有權力及技能",
                inline=False)
    
    sr = discord.Embed(title="預言家" ,description="關於預言家的說明" ,color= discord.Colour.blue())
    sr.add_field(name="窺探",
                value="_每晚夜裡, 預言家透過閱讀小北百科領悟了人生之理, 看透了一個人的內心_"+
                      "夜晚降臨時, 預言家可以獲得任一玩家的真實身分(如:狼人)",
                inline=False)
    sr.add_field(name="投票權",
                value="可於白天時投給懷疑的對象或欲陷害的對象\n"+
                      "投票結束後, 票數最多的將被放逐, 並失去所有權力及技能",
                inline=False)
    
    vl = discord.Embed(title="村民"   ,description="關於村民的說明"   ,color= discord.Colour.dark_gold())
    vl.add_field(name="沉睡",
                value="_小北百科顯示:\n"+
                      "這個村莊中的人大多患有失眠症, 僅一些村民具有沉睡的能力_\n"+
                      "夜晚降臨時, 此技能被強制啟用, 使用後將無法漁夜中執行其他動作, 一覺到天亮",
                inline=False)
    vl.add_field(name="投票權",
                value="可於白天時投給懷疑的對象或欲陷害的對象\n"+
                      "投票結束後, 票數最多的將被放逐, 並失去所有權力及技能",
                inline=False)

    channel: int = None
    '''# error
    def __init__(self):
        with open('help_data.json' ,'r' ,encoding='utf8') as jdt:
            data = json.load(jdt)
        data['role_page'] = 1
        with open('help_data.json' ,'w' ,encoding='utf8') as jdt:
            json.dump(data, jdt)
    ''' 
    @discord.ui.button(label="上一頁" ,style=discord.ButtonStyle.primary)
    async def back(self ,interaction: discord.Integration ,button: discord.Button):
        with open('help_data.json' ,'r' ,encoding='utf8') as jdt:
            data = json.load(jdt)
        data['role_page'] -= 1
        if data['role_page'] == 0:
            await interaction.delete()
        elif data['role_page'] == 1:
            await interaction.response.edit_message(embed=self.ww)
        elif data['role_page'] == 2:
            await interaction.response.edit_message(embed=self.wc)
        elif data['role_page'] == 3:
            await interaction.response.edit_message(embed=self.sr)
        elif data['role_page'] == 4:
            await interaction.response.edit_message(embed=self.vl)
        else:
            logging.error('i dant know what happen in Role_help.back()')
        with open('help_data.json' ,'w' ,encoding='utf8') as jdt:
            json.dump(data, jdt)
    
    @discord.ui.button(label="下一頁" ,style=discord.ButtonStyle.primary)
    async def next(self ,interaction: discord.Integration ,button: discord.Button):
        with open('help_data.json' ,'r' ,encoding='utf8') as jdt:
            data = json.load(jdt)
        data['role_page'] += 1
        if data['role_page'] == 1:
            await interaction.response.edit_message(embed=self.ww)
        elif data['role_page'] == 2:
            await interaction.response.edit_message(embed=self.wc)
        elif data['role_page'] == 3:
            await interaction.response.edit_message(embed=self.sr)
        elif data['role_page'] == 4:
            await interaction.response.edit_message(embed=self.vl)
        elif data['role_page'] > 4:
            data['role_page'] -= 1
        else:
            logging.error('i dant know what happen in Role_help.next()')
        with open('help_data.json' ,'w' ,encoding='utf8') as jdt:
            json.dump(data, jdt)





class Main_help(View):

    channel: int = None


    @discord.ui.select(
        placeholder="click here",
        max_values=1,
        options=[
            discord.SelectOption(label="規則流程",value='opt_rule',description="遊戲流程的說明"),
            discord.SelectOption(label="角色說明",value='opt_role',description="角色功能的說明"),
            discord.SelectOption(label="指令操作",value='opt_oper',description="動作指令的說明"),
            ]
    )
    async def main_help(self ,interaction: discord.Integration ,select: Select):
        '''
        if select.values[0]=="opt_rule":
            rpl = Rule_help()
            await interaction.message.reply(embed=em_rule     ,view=Rule())
        '''
        if select.values[0]=="opt_role":
            rpl = Role_help()
            rpl.channel = self.channel
            print('role',self.channel)
            await self.channel.send(view=rpl)
            print('goto role')
    '''
        if select.values[0]=="opt_oper":
            await interaction.message.reply(embed=em_operation,view=Operation())
                    

    @discord.ui.select()
    async def slc(self, internation: discord.Integration, button: Button):
        pass
    '''


class myHelp(myCog):
    @commands.command()
    async def apapap(self, ctx):
        view=Main_help()
        view.channel=ctx.channel
        print('help',ctx.channel)
        await ctx.send(view=view)
        print('hi')






async def setup(bot):
    await bot.add_cog(myHelp(bot))