import discord
from discord.ext import commands

class Warn(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason):
        if ctx.author == member:
            await ctx.send(f'{ctx.author.mention} Meh you can\'t warn yourself!')
        else: 
            embed = discord.Embed(description=f'by {ctx.author.mention} in {ctx.guild}',colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name=f'You were WARNED for: {reason}')
            await member.send(embed=embed)
    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description='Command Syntax : <prefix>warn <user> <warning>',colour=discord.Colour.dark_orange())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! Wrong command usage.')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description='Get more permissions to use this command.',colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! You do not have enough permissions.')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandError):
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='Sorry, an error occured.')
            await ctx.send(embed=embed)
            
    @commands.command(aliases=['help warn', 'warnhelp'])
    async def helpwarn(self, ctx):
        embed = discord.Embed(title='**Warn**', description='Give a warning to a member.', colour=discord.Colour.dark_blue())
        embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        embed.add_field(name='Usage', value='<prefix>warn <user> <warning>')
        await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(Warn(client))
