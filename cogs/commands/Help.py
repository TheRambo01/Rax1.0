import discord 
from discord.ext import commands 

class Help(commands.Cog):

    def  __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='**Help**', colour=discord.Colour.dark_blue())
        embed.set_footer(text='Rax', icon_url='https://i.postimg.cc/jSHYPtDP/rax0.png')
        embed.add_field(name='Moderation', value='**`ban <user>`** - Ban a specified member. \n**`kick <user>`** - Kick a specified member. \n**`mute <user>`** - Mute a specified member from sending messages in the present channel. \n**`purge <amount>`** - Purge(delete) the specified amount of messages. \n**`unban <user>`** - Unban a banned user. \n**`unmute <user>`** - Unmute a muted user. \n**`warn <user> <reason/warning>`** - Warn a specified member for a given reason.', inline=False)
        embed.add_field(name='Fun', value='**`f <member>`** - Press F to pay respect XD. \n**`salute <member>`** - Salute a member. ', inline=False)
        embed.add_field(name='Miscellaneous', value='**`av|avatar`** - Get the avatar (profile picture) of a member. \n**`enlarge`** - Get an enlarged image of a custom emoji. \n**`help`** - Get info about all the commands. \n**`help<command>`** - Get more info about individual commands. \n**`prefix`** - Set the bot prefix.', inline=False)
        embed.add_field(name='Rax', value='**`invite`** - Get an invite link to add Rax to your server. \n**`stats`** - Get some info about Rax. \n**`vote`** - Get a invite link for voting Rax.', inline=False)
        
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))
