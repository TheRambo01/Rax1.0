import discord
from discord.ext import commands

class Vote(commands.Cog):    
    
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['upvote'])    
    async def vote(self, ctx):
        embed = discord.Embed(title='Vote Rax', description='Help Rax reach more servers and people by upvoting it: \n[Top.gg](https://top.gg/bot/765492360041726003/vote) \n[Discord Bot List](https://discordbotlist.com/bots/rax/upvote) \n[Discord-Bot List (EU)](https://discord-botlist.eu/bots/765492360041726003/vote)', colour=discord.Colour.green())
        embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        await ctx.send(embed=embed)

    @commands.command(aliases=['votehelp'])
    async def helpvote(self, ctx):
        embed = discord.Embed(title='**Vote Rax**', description='Get links for upvoting Rax.', colour=discord.Colour.dark_blue())
        embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        embed.add_field(name='Usage', value='<prefix>vote ')
        await ctx.channel.send(embed=embed)
          
def setup(client):
   client.add_cog(Vote(client))