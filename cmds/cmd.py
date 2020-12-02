import discord
from discord.ext import commands
from  core.classes import Cog_Extension
import random
import json
import os
import os.path
from datetime import datetime as dt


with open('setting.json','r' , encoding="utf-8") as jFile:
    jdata = json.load(jFile)

sagumelist = os.listdir("./image/Sagume")
day = {
    "Mon": "星期一",
    "Tue": "星期二", 
    "Wed": "星期三", 
    "Thu": "星期四", 
    "Fri": "星期五",
    "Sat": "星期六",
    "Sun": "星期日",
}



class cmd(Cog_Extension):
    
    @commands.command(name='bot')
    async def _bot(self,ctx):
        
        image = random.choice(sagumelist)
        await ctx.send('殺菇咩好耶 殺菇咩又中',file=discord.File("image/Sagume/" + image))
    

    @commands.command(name='殺菇')
    async def mushroom(self,ctx ):
        
        image = random.choice(sagumelist)
        await ctx.send('我要殺菇!' , file=discord.File("image/Sagume/" + image))
        
        return
    

    @commands.command()
    async def time(self,ctx):
        time = dt.now()
        
        week = day[time.strftime('%a')]
        localTime = time.strftime(f'%Y年%m月%d日 {week} %X (GMT+8) ')
        await ctx.send(f"月都依家既時間係 : {localTime}")

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title=self.bot.user.name, description=self.bot.description, color=0xC6CFD6)
        times = len(jdata["Command"])
        for i in range(times):
            embed.add_field(name=jdata["Command"][i], value=jdata["Use"][i], inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    async def add(self , ctx , left : int, right : int):
        """Adds two numbers together."""
        await ctx.send(left + right)


    @commands.command()
    async def roll(self , ctx, dice : str):
        print('------')
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.group(pass_context=True)
    async def cool(self , ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

def setup(bot):
    bot.add_cog(cmd(bot))