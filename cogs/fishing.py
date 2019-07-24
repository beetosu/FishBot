import discord
from discord.ext import commands
from datetime import datetime
import time
import data

class Fishing(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('fishing is online')

    @commands.command()
    async def fish(self, ctx):
        await ctx.send('reel casted!')
        time.sleep(2)
        data.ready_fish[ctx.author] = datetime.now()
        await ctx.send('something\'s on the line!')

    @commands.command()
    async def reel(self, ctx):
        if ctx.author in data.ready_fish.keys():
            await ctx.send(f':fishing_pole_and_fish: fish caught! \n wow that took {datetime.now() - data.ready_fish[ctx.author]}')
            data.ready_fish.pop(ctx.author, None)
        else:
            await ctx.send('there\'s nothing to reel in yet.' )

def setup(client):
    client.add_cog(Fishing(client))
