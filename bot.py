import discord
import os
from discord.ext import commands

#this is picked jus bc it seems uncommon + quicker than like a double command (helpful for gameplay)
client = commands.Bot(command_prefix = ";")

'''
this is what runs all the main commands, and deploys all the non essential commands (cogs)
unlike the cogs, any addition to this code will have to be deployed by restarting the bot.
'''

#makes bot status changes (might change later lul)
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('with ur heart'))
    print("bot is ready!")

#quick n dirty latency check
@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

#these three commands jus work with the cogs in whatever way they're needed
#TO DO: make these only acessable to me? or get rid for alpha all together?
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

#maybe worth elaborating?
#@client.event
#async def on_command_error(ctx, error):
    #if isinstance(error, commands.CommandNotFound):
        #pass

#on bot bootup, load every cog
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename} loaded')

client.run(os.environ.get('FISH_KEY'))
