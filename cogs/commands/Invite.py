import discord
from discord.ext import commands


class Invite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title='Invite Rax', description='[Invite with recommended permissions](https://discord.com/api/oauth2/authorize?client_id=765492360041726003&permissions=1544023286&scope=bot) \n[Invite with 0 permissions](https://discord.com/api/oauth2/authorize?client_id=765492360041726003&permissions=0&scope=bot) \n[Invite with Administrator permissions](https://discord.com/api/oauth2/authorize?client_id=765492360041726003&permissions=8&scope=bot)', colour=discord.Colour.dark_blue())
        embed.set_footer(
            text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        await ctx.send(embed=embed)

    @commands.command(aliases=['help invite', 'invitehelp'])
    async def helpinvite(self, ctx):
        embed = discord.Embed(
            title='Invite Rax', description='Get an invite link for adding Rax to your server.', colour=discord.Colour.dark_blue())
        embed.set_footer(
            text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        embed.add_field(name='Usage', value='<prefix>invite ')
        await ctx.channel.send(embed=embed)


def setup(client):
   client.add_cog(Invite(client))
