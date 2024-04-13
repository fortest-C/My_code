# discord mods
import discord
from discord.ext import commands
from discord.ui import Select,View

# other mods
import json
import asyncio
import random
from datetime import datetime

# my mods
from core.classes import myCog


with open('database\help.json',mode='r',encoding='utf8') as jfile:#r==read,utf8解碼
    helptext = json.load(jfile)

main_help_embed=discord.Embed(title=helptext["main_title"],description=helptext["main_description"],color=0xFF6984)
main_help_embed.set_footer(text="彈力鯊鍋余頭")
main_help_embed.set_thumbnail(url=helptext["bot_avatar_url"])


em_rule                    =discord.Embed(title="規則簡介",color=discord.Colour.random())
em_role_introduction       =discord.Embed(title="角色說明",color=discord.Colour.random())
em_operation_introduction  =discord.Embed(title="操作設定",color=discord.Colour.random())


#====================================== Main help
class Myselect(View):
    @discord.ui.select(
        placeholder="click here",
        max_values=1,
        options=[
            discord.SelectOption(label="規則簡介",value='opt_rule',description="遊戲規則的說明"),
            discord.SelectOption(label="角色說明",value='opt_role',description="角色功能的說明"),
            discord.SelectOption(label="指令操作",value='opt_oper',description="動作指令的說明"),
            ]
    )
    async def select_callback(self,select,interaction):
        select.disabled=True
        if select.values[0]=="opt_role":
            cla=Rule()
            await interaction.response.edit_message(embed=em_rule,view=cla)     
        if select.values[0]=="opt_role":
            cla=Role()
            await interaction.response.edit_message(embed=em_role_introduction,view=cla)
        if select.values[0]=="opt_oper":
            cla=Operation()
            await interaction.response.edit_message(embed=em_operation_introduction,view=cla)


r1 = discord.Embed(title="遊戲參與" ,description="透過指令加入或退出玩家儲列" ,color=discord.Colour)
r1.add_field(name="加入遊戲"    ,value="透過<join>指令加入遊戲"   ,inline=False)
r1.add_field(name="退出遊戲"    ,value="透過<quit>指令退出遊戲"   ,inline=False)
r1.add_field(name="查詢玩家儲列" ,value="透過<player>查詢玩家儲列" ,inline=False)

r2 = discord.Embed(title="遊戲基礎設定" ,description="角色數量設定",color=discord.Colour)
r2.add_field(name="目前共有4種身分",
             value="分別為\n"+
                   "狼人  巫師  預言家  村民\n"+
                   "角色說明請透過<help>指令選取<角色說明>",
             inline=False)
r2.add_field(name="透過<",
             value="\n"+
                   "\n"+
                   "",
             inline=False)
r3 = discord.Embed(title="遊戲開始"     ,description="遊戲初始化完成, 進入遊戲" ,color=discord.Colour)
r3.add_field(name="" ,value="" ,inline=False)
r4 = discord.Embed(title="第一個夜晚"   ,description="月圓之時, 狼人化身"       ,color=discord.Colour)
r4.add_field(name="" ,value="" ,inline=False)

rule={}
for i in rule:
    rule[i].set_footer(text=rule[i].title)

ww = discord.Embed(title="狼人"   ,description="關於狼人的說明"   ,color= discord.Colour.light_grey)
wc = discord.Embed(title="巫師"   ,description="關於巫師的說明"   ,color= discord.Colour.purple)
sr = discord.Embed(title="預言家" ,description="關於預言家的說明" ,color= discord.Colour.blue)
vl = discord.Embed(title="村民"   ,description="關於村民的說明"   ,color= discord.Colour.dark_gold)

ww.add_field(name="刺殺",
             value="_小北百科顯示:\n"+
                   "狼人總是於夜晚成群出沒, 並且其鋒利的爪子具有使人一擊斃命的極高攻擊力_\n"+
                   "夜晚降臨時, 狼人們互認身分並討論殺害對象",
            inline=False)
ww.add_field(name="投票權",
             value="可於白天時投給懷疑的對象或欲陷害的對象\n"+
                   "投票結束後, 票數最多的將被放逐, 並失去所有權力及技能",
            inline=False)
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
sr.add_field(name="窺探",
             value="_每晚夜裡, 預言家透過閱讀小北百科領悟了人生之理, 看透了一個人的內心_"+
                   "夜晚降臨時, 預言家可以獲得任一玩家的真實身分(如:狼人)",
                   inline=False)
sr.add_field(name="投票權",
             value="可於白天時投給懷疑的對象或欲陷害的對象\n"+
                   "投票結束後, 票數最多的將被放逐, 並失去所有權力及技能",
            inline=False)
vl.add_field(name="沉睡",
             value="_小北百科顯示:\n"+
                   "這個村莊中的人大多患有失眠症, 僅一些村民具有沉睡的能力_\n"+
                   "夜晚降臨時, 此技能被強制啟用, 使用後將無法漁夜中執行其他動作, 一覺到天亮")
vl.add_field(name="投票權",
             value="可於白天時投給懷疑的對象或欲陷害的對象\n"+
                   "投票結束後, 票數最多的將被放逐, 並失去所有權力及技能",
            inline=False)

'''
ww.set_footer(text=ww.title)
wc.set_footer(text=wc.title)
sr.set_footer(text=sr.title)
vl.set_footer(text=vl.title)
'''
role={
    "werewolf" : ww,
    "witch"    : wc,
    "seer"     : sr,
    "villager" : vl
}
for i in rule:
    rule[i].set_footer(text=rule[i].title)

del ww
del wc
del sr
del vl

operation={}
for i in operation:
    operation[i].set_footer(text=operation[i].title)


#====================================== Role
class Role(View):
    @discord.ui.select(
        placeholder="clike here",
        max_values=1,
        options=[
            discord.SelectOption(label="狼人"  ,value="werewolf"),
            discord.SelectOption(label="巫師"  ,value="witch"),
            discord.SelectOption(label="預言家",value="seer"),
            discord.SelectOption(label="村民"  ,value="villager"),
            discord.SelectOption(label="回前頁",value="back")
            ]
    )
    async def select_callback(self,select,interaction):
        if select.values[0]=="back":
            view=Myselect()
            await interaction.response.edit_message(view=view,embed=main_help_embed)
        else:
            await interaction.response.edit_message(embed=role[select.values[0]])


#====================================== rule
class Rule(View):
    @discord.ui.select(
        placeholder="clike here",
        max_values=1,
        options=[
            discord.SelectOption(label="狼人"  ,value="werewolf"),
            discord.SelectOption(label="巫師"  ,value="witch"),
            discord.SelectOption(label="預言家",value="seer"),
            discord.SelectOption(label="村民"  ,value="villager"),
            discord.SelectOption(label="回前頁",value="back")
            ]
    )
    async def select_callback(self,select,interaction):
        if select.values[0]=="back":
            view=Myselect()
            await interaction.response.edit_message(view=view,embed=main_help_embed)
        else:
            await interaction.response.edit_message(embed=rule[select.values[0]])



#====================================== operation
class Operation(View):
    @discord.ui.select(
        placeholder="clike here",
        max_values=1,
        options=[
            discord.SelectOption(label="狼人"  ,value="werewolf"),
            discord.SelectOption(label="巫師"  ,value="witch"),
            discord.SelectOption(label="預言家",value="seer"),
            discord.SelectOption(label="村民"  ,value="villager"),
            discord.SelectOption(label="回前頁",value="back")
            ]
    )
    async def select_callback(self,select,interaction):
        if select.values[0]=="back":
            view=Myselect()
            await interaction.response.edit_message(view=view,embed=main_help_embed)
        else:
            await interaction.response.edit_message(embed=operation[select.values[0]])