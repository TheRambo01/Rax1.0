import discord
from discord.ext import commands

class Misc(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases=['bhosdike', 'bosdike'])
    async def bsdk(self, ctx, member:discord.Member):
        if member == self.client.user:
            await ctx.send(f'Not me. Better luck next time. {ctx.author.mention} :)')
        else: 
            embed1 = discord.Embed(colour=discord.Color.blurple())
            embed1.set_image(url='https://i.postimg.cc/xd4fdMfY/mirzapur1.jpg')
            await ctx.send(member.mention, embed=embed1)

def setup(client):
    client.add_cog(Misc(client))
