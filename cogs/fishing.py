import discord
from discord.ext import commands
from datetime import datetime, timedelta
import time
import data
import math
import random
import sqlite3
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
        await ctx.send(f'{ctx.author.mention}! something\'s on the line!\ntype ";catch" to reel it in!')

    @commands.command()
    async def theguild(self, ctx):
        await ctx.send(f'your guild is {ctx.guild.members}.')

    @commands.command()
    async def catch(self, ctx):
        catch = choice(data.fish_types[0], 1, data.fish_odds[0])[0]
        if ctx.author in data.ready_fish.keys():
            odds = math.exp(-(datetime.now() - data.ready_fish[ctx.author]).total_seconds()/25)
            if random.random() < odds:
                conn_p = sqlite3.connect('databases/players.db')
                conn_g = sqlite3.connect('databases/guild_players.db')
                cur_p = conn_p.cursor()
                cur_g = conn_g.cursor()
                id = cur_g.execute('SELECT * FROM server_' + str(ctx.guild.id) + ' WHERE username=' + str(ctx.author.id))
                for q in id:
                    actual_id = str(q[1])
                    player = cur_p.execute('SELECT * FROM users WHERE id=' + str(q[1]))
                for i in player:
                    new_coins = str(int(i[5]) + catch["money"])
                    new_points = str(int(i[6]) + catch["points"])
                    cur_p.execute('UPDATE users SET money = ' + new_coins + ', points = ' + new_points + ' WHERE id =' + actual_id)
                conn_p.commit()
                conn_p.close()
                conn_g.close()
                await ctx.send(f'you caught a {catch["name"]}! {catch["emoji"]}\n{catch["points"]} points earned\n{catch["money"]} money earned')
            else:
                await ctx.send(f'dang! it got away!')
            data.ready_fish.pop(ctx.author, None)
        else:
            await ctx.send('there\'s nothing to reel in yet.' )

def setup(client):
    client.add_cog(Fishing(client))
