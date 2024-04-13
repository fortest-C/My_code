### just for test ###
# discord mods
import discord
from discord.ext import commands

# other mods

# my mods
from core.classes import myCog


class Test(myCog):
    @commands.command()
    async def test1(self, ctx: commands.Context):
        file = discord.File("head_icon.png", filename="test.png")
        embed = discord.Embed(
            color=0x9400d3,
            title="我是誰?",
            description="下面就讓我來說說我的來歷吧!",
            url="https://www.google.com"
        )
        embed.set_author(name="The_Werewolves_of_Miller_coolooc", icon_url="attachment://test.png")
        await ctx.send(file=file, embed=embed)


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.content == "hi":
            await message.channel.send("hello", reference=message)
#     @commands.Cog.listener("on_message")
#     async def greet(self,message):
#         Cheers= ["Hi", "hi", "Hello", "hello"]
#         if message.content in Cheers:
#             await message.channel.send('Hello again')
#             await self.client.process_commands(message)


async def setup(bot):
    await bot.add_cog(Test(bot))