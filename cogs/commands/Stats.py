from datetime import datetime
import discord
from discord.ext import commands

class Stats(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        start_time = datetime.now()
        print(start_time)
        return start_time

    @commands.command(aliases=['botinfo', 'ping', 'raxstats'])
    async def stats(self, ctx):
        s_time = on_ready()
        new_time = datetime.now()
        diff = new_time - s_time
        print(diff)
        guild_count = 0
        for guild in self.client.guilds:
            guild_count += 1
        png = round(self.client.latency*1000)
        embed = discord.Embed(title='Rax Stats', colour=discord.Colour.green())
        embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        embed.add_field(name='Bot Latency', value=f'{png} ms', inline=True)
        embed.add_field(name='Server Count', value=f'{guild_count} ' ,inline=True)
        embed.add_field(name='Members in this server', value=ctx.guild.member_count, inline=True)
        await ctx.send(embed=embed)
            
    @commands.command(aliases=['help botinfo', 'botinfohelp', 'statshelp'])
    async def helpstats(self, ctx):
        embed = discord.Embed(title='**Bot Info**', description='Gives some basic info about Rax.', colour=discord.Colour.dark_blue())
        embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        embed.add_field(name='Usage', value='<prefix>stats ')
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Stats(client))
