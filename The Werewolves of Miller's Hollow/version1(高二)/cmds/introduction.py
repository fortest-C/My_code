### introduc how to play ###
# discord mods
import discord
from discord.ext import commands

# other mods

# my mods
from core.classes import myCog

class Introduct(myCog):
    @commands.command()
    async def Role(self, ctx):
        try:
            em = discord.Embed(
                color=0x9932cc,
                title="<:i_help:1066289043828133898> 角色說明",
                description="所有玩家將被分為兩個陣營\n"+
                            "率先殲滅敵對者獲勝"
            )
            good = open('./cmds/introduction/good.txt', 'r', encoding='utf-8')
            em.add_field(
                name="好人",
                value=good.read(),
                inline=False
            )
            bad = open('./cmds/introduction/bad.txt', 'r', encoding='utf-8')
            em.add_field(
                name="壞人",
                value=bad.read(),
                inline=False
            )
            await ctx.send(embed=em)
        except Exception as e:
            print(e)

    @commands.command()
    async def Rule(self, ctx):
        rule = open('./cmds/introduction/rule.txt', 'r', encoding='utf-8')
        em = discord.Embed(
            color=0xff8c00,
            title="<:i_help:1066289043828133898> 流程說明",
            description="獲勝方式: 率先殲滅敵對者獲勝"
        )
        em.add_field(
            name="流程",
            value=rule.read(),
            inline=False
        )
        await ctx.send(embed=em)
        rule.close()

    @commands.command()
    async def stop_game(self, ctx:discord.ext.commands.context.Context):
        await self.sgfun(ctx)
    @commands.command()
    async def sg(self, ctx:discord.ext.commands.context.Context):
        await self.sgfun(ctx)
    async def sgfun(self, ctx):
        em = discord.Embed(
            color=0x32cd32,
            title="<:i_help:1066289043828133898> 強制結束遊戲",
            description="使用命令以強制停止遊戲(command: `st_q`)\n" +
                        "*注意: 本局資料將不復存在!"
        )
        await ctx.send(embed=em)


async def setup(bot):
    await bot.add_cog(Introduct(bot))