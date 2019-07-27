import discord
from discord.ext import commands
from datetime import datetime, timedelta
import time
import data
import math
import random
from numpy.random import choice

class Fishing(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('fishing is online')

    @commands.command()
    async def fish(self, ctx):
        await ctx.send('reel casted!')
        time.sleep(random.randint(1, 2))
        data.ready_fish[ctx.author] = datetime.now()
        await ctx.send(f'{ctx.author.mention}! something\'s on the line!')

    @commands.command()
    async def theguild(self, ctx):
        await ctx.send(f'your guild is {ctx.guild.members}.')

    @commands.command()
    async def catch(self, ctx):
        catch = choice(data.fish_types[0], 1, data.fish_odds[0])[0]
        if ctx.author in data.ready_fish.keys():
            odds = math.exp(-(datetime.now() - data.ready_fish[ctx.author]).total_seconds()/25)
            if random.random() < odds:
                await ctx.send(f'you caught a {catch["name"]}! {catch["emoji"]}\n{catch["points"]} points earned\n{catch["money"]} money earned')
            else:
                await ctx.send(f'dang! it got away!')
            data.ready_fish.pop(ctx.author, None)
        else:
            await ctx.send('there\'s nothing to reel in yet.' )

def setup(client):
    client.add_cog(Fishing(client))
