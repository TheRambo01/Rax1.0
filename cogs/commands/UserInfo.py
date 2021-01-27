import discord
from discord.ext import commands

class UserInfo(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def userinfo(self, ctx, member:discord.Member):
        pass


def setup(client):
    client.add_cog(UserInfo(client))