import discord
from discord.ext import commands

class Enlarge(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def enlarge(self, ctx, emoji: discord.Emoji):
        await ctx.send(emoji.url)

    @enlarge.error
    async def enlarge_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description='Command Syntax : <prefix>enlarge <custom_emoji>',colour=discord.Colour.dark_orange())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! Wrong command usage.')
            await ctx.send(embed=embed)

    @commands.command(aliases=['help enlarge', 'enlargehelp'])
    async def helpenlarge(self, ctx):
        embed = discord.Embed(title='**Enlarge**', description='Get an enlarged image of a custom emoji in a server.', colour=discord.Colour.dark_blue())
        embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        embed.add_field(name='Usage', value='Command Syntax : <prefix>enlarge <custom_emoji>')
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Enlarge(client))
