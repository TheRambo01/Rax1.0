import discord
import os
import json
from discord.ext import commands

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(case_insensitive=True, command_prefix = get_prefix)
client.remove_command('help')

def is_me(ctx):
    return ctx.author.id == 614067686535594006

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = ','

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=3)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=3)

@client.command()
@commands.check(is_me)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}')

@client.command()
@commands.check(is_me)
async def unload(ctx, extension):
   client.unload_extension(f'cogs.{extension}')
   await ctx.send(f'Unloaded {extension}')

@client.command()
@commands.check(is_me)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')

@client.command()
@commands.check(is_me)
async def listguilds(self, ctx):
    async for guild in self.client.fetch_guilds(limit=150):
        print(guild.id)

for filename in os.listdir('./cogs/commands'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.commands.{filename[:-3]}')

for filename in os.listdir('./cogs/listeners'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.listeners.{filename[:-3]}')

client.run(token)
