import discord
from discord.ext import commands

class Avatar(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases=['avatar'])
    async def av(self, ctx, member:discord.Member):
        embed = discord.Embed(title='User Avatar', description=f'{member.display_name}\'s avatar:', color=discord.Color.greyple())
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)
    @av.error
    async def av_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description='Command usage: <prefix>av|avatar <member>',colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url=self.ClientUser.avatar_url)
            embed.set_author(name='ERROR! Wrong command usage.')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandError):
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='Sorry an error occured.')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(description='Make sure the member is present in the server.',colour=discord.Colour.red())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! Invalid member specified')
            await ctx.send(embed=embed)


    @commands.command(aliases=['help avatar', 'avatarhelp', 'avhelp', 'helpav'])
    async def helpavatar(self, ctx):
        embed = discord.Embed(title='**Avatar**', description='Returns the avatar (profile image) of the given user.', colour=discord.Colour.dark_blue())
        embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        embed.add_field(name='Usage', value='<prefix>avatar|av <user> ')
        await ctx.channel.send(embed=embed)

        
def setup(client):
    client.add_cog(Avatar(client))
