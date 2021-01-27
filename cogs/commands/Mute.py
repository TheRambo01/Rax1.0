import discord
from discord.ext import commands
import discord.permissions

class Mute(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        await ctx.channel.set_permissions(member, read_message_history = True, read_messages=True, send_messages=False, reason=reason)
        embed = discord.Embed(colour=discord.Colour.dark_green())
        embed.set_author(name=f'{member.name}#{member.discriminator} was muted :)')
        embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        await ctx.send(embed=embed)
       
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description='Get \'Kick Members\' permission to use this command.',colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! You do not have enough permissions.')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description='Command usage: <prefix>mute <member> [reason]',colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! Wrong command usage.')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(description='Make sure the member is present in the server.',colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! Invalid member specified')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! Rax does not have enough permissions.')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandError):
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='Sorry, an error occured. Please make sure permissions are enabled.')
            await ctx.send(embed=embed)

    @commands.command(aliases=['help mute', 'mutehelp'])
    async def helpmute(self, ctx):
        embed = discord.Embed(title='**Mute**', description='Disable the \'Send Messages\' and a few other permissions for the given user. [Requires \'Kick Members\' permission.]', colour=discord.Colour.dark_blue())
        embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        embed.add_field(name='Usage', value='<prefix>mute <user> [reason]')
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Mute(client))
