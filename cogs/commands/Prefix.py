import discord
import json
from discord.ext import commands

class Prefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def prefix(self, ctx, pref=None):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        if pref!=None:
            prefixes[str(ctx.guild.id)] = pref
            with open('prefixes.json', 'w') as f:
                json.dump(prefixes, f, indent=3)

            embed = discord.Embed(colour=discord.Colour.dark_green())
            embed.set_author(name=f'Rax prefix set to: "{pref}"')
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            await ctx.send(embed=embed)
        elif pref==None:
            embed = discord.Embed(colour=discord.Colour.dark_green())
            embed.set_author(name=f'Current Rax prefix is: "{prefixes[str(ctx.guild.id)]}"')
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(Prefix(client))
