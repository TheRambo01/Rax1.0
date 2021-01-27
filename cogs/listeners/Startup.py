import discord
from discord.ext import commands

class Startup(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Rax is ready.")
        guild_count = 0
        member_count = 0
        for guild in self.client.guilds:
            guild_count += 1
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game(f',help'))


def setup(client):
    client.add_cog(Startup(client))
