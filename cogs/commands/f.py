import discord
from discord.ext import commands 

class f(commands.Cog):
    
    def __init__(self, client):
        self.client = client    
    
    @commands.command()
    async def f(self, ctx, member:discord.Member, *, fs=None):
        if member == self.client.user:
            await ctx.send(f'Not me. Better luck next time. {ctx.author.mention} :)')
        else:
            embed1 = discord.Embed(title='Press F to pay respect.', colour=discord.Color.blurple())
            embed1.set_image(url='https://i.postimg.cc/4dTpCWG5/tenor.gif')
            message = await ctx.send(member.mention, embed=embed1)
            emoji = '🇫'
            await message.add_reaction(emoji)
    @f.error
    async def f_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description='Command Syntax : <prefix>f <member>',colour=discord.Colour.dark_orange())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! Wrong command usage.')
            await ctx.send(embed=embed)
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(description='Specify a member present in the server.',colour=discord.Colour.dark_orange())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! Invalid member specified.')
            await ctx.send(embed=embed)
       
    @commands.command(aliases=['help f', 'fhelp'])
    async def helpf(self, ctx):
        embed = discord.Embed(title='**f**', description='Press F to pay Respects.', colour=discord.Colour.dark_blue())
        embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        embed.add_field(name='Usage', value='<prefix>f <user>')
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(f(client))
