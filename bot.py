import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = ";")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('with ur heart'))
    print("bot is ready!")

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded!')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded!')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} reloaded!')

#@client.event
#async def on_command_error(ctx, error):
    #if isinstance(error, commands.CommandNotFound):
        #pass

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename} loaded')

client.run("NTA1MTM1NzcyMDI3MDYwMjI0.XTYQqQ.ZrmsTnSkNVKh4BVW3cUYUCS4rtE")
