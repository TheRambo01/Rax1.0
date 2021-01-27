import discord
from discord.ext import commands

class Purge(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=0):
        if(amount != 0) and (amount > 0) and (amount < 100):
            await ctx.channel.purge(limit=amount + 1)
            await (await ctx.channel.send(f'{ctx.author.mention} purged {amount} messages. :)')).delete(delay=3)
        if(amount == 0):
            emb = discord.Embed(description='Please specify an amount of messages to delete.', color=discord.Color.dark_orange())
            emb.set_author(name='ERROR! No amount specified.')
            emb.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            await ctx.send(embed=emb)
        if(amount >= 100):
            emb = discord.Embed(description='Please specify an amount lower than 100.', color=discord.Color.dark_orange())
            emb.set_author(name='ERROR! Too many messages to delete!')
            emb.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            await ctx.send(embed=emb)
    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description='Get \'Manage Messages\' permission to use this command.',colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! You do not have enough permissions.')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description='Command Syntax : <prefix>purge <amount>',colour=discord.Colour.dark_orange())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! Wrong command usage.')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! Rax does not have enough permissions.')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandError):
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='Sorry, an error occured.')
            await ctx.send(embed=embed)

    @commands.command(aliases=['help purge', 'purgehelp'])
    async def helppurge(self, ctx):
        embed = discord.Embed(title='**Purge**', description='Purge/Delete a specified amount of messages in the present channel. [Maximum limit = 100] [Requires \'Manage Messages\' permission.]', colour=discord.Colour.dark_blue())
        embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        embed.add_field(name='Usage', value='<prefix>purge <amount>')
        await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(Purge(client))
