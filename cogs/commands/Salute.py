import discord
from discord.ext import commands

class Salute(commands.Cog):
    
    def __init__(self, client):
        self.client = client    
    
    @commands.command()
    async def salute(self, ctx, member:discord.Member, *, reason=None):
        if reason != None:
            embed1 = discord.Embed(colour=discord.Color.blurple())
            embed1.set_image(url='https://i.postimg.cc/G2Bgv9sF/salute.png')
            embed1.set_footer(text=f'by {ctx.author.name}')
            message = await ctx.send(f'{member.mention} You have been saluted for : {reason} ', embed=embed1)
            emoji1 = '🇸'
            await message.add_reaction(emoji1)
            emoji2 = '🇦'
            await message.add_reaction(emoji2)
            emoji3 = '🇱'
            await message.add_reaction(emoji3)
            emoji4 = '🇺'
            await message.add_reaction(emoji4)
            emoji5 = '🇹'
            await message.add_reaction(emoji5)
            emoji6 = '🇪'
            await message.add_reaction(emoji6)
        elif reason == None:
            embed1 = discord.Embed(title='We salute you.', colour=discord.Color.blurple())
            embed1.set_image(url='https://i.postimg.cc/G2Bgv9sF/salute.png')
            embed1.set_footer(text=f'by {ctx.author.name}')
            message = await ctx.send(member.mention, embed=embed1)
            emoji1 = '🇸'
            await message.add_reaction(emoji1)
            emoji2 = '🇦'
            await message.add_reaction(emoji2)
            emoji3 = '🇱'
            await message.add_reaction(emoji3)
            emoji4 = '🇺'
            await message.add_reaction(emoji4)
            emoji5 = '🇹'
            await message.add_reaction(emoji5)
            emoji6 = '🇪'
            await message.add_reaction(emoji6)

    @salute.error
    async def salute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description='Command Syntax : <prefix>salute <member>',colour=discord.Colour.dark_orange())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! Wrong command usage.')
            await ctx.send(embed=embed)
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(description='Specify a member present in the server.',colour=discord.Colour.dark_orange())
            embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
            embed.set_author(name='ERROR! Invalid member specified.')
            await ctx.send(embed=embed)
       
    @commands.command(aliases=['help salute', 'salutehelp'])
    async def helpsalute(self, ctx):
        embed = discord.Embed(title='**Salute**', description='Get a salutation image for the tagged user.', colour=discord.Colour.dark_blue())
        embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        embed.add_field(name='Usage', value='<prefix>salute <user> [reason]')
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Salute(client))
