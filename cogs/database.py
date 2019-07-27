import discord
from discord.ext import commands
import sqlite3

class Database(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('database is online')

    @commands.command()
    async def createdb(self, ctx):
        conn_p = sqlite3.connect('databases/players.db')
        conn_g = sqlite3.connect('databases/guild_players.db')
        cur_p = conn_p.cursor()
        cur_g = conn_g.cursor()
        await ctx.send('databases loaded!')
        cur_p.execute('CREATE TABLE IF NOT EXISTS users (id, rod, reel_max, reel, bait, money, points)')
        cur_g.execute('CREATE TABLE IF NOT EXISTS server_' + str(ctx.guild.id) + ' (username, id)')
        current_id = 0#len(cur_p.execute('SELECT * from users'))
        for i in ctx.guild.members:
            if i.id != 505135772027060224:
                cur_p.execute('INSERT INTO users VALUES (' + str(current_id) + ', "default", 1, 1, "none", 0, 0)')
                cur_g.execute('INSERT INTO server_' + str(ctx.guild.id) + ' VALUES (' + str(i.id) + ', ' + str(current_id) + ')')
                await ctx.send(f'{i.name} added!')
                current_id += 1
        conn_p.commit()
        conn_p.close()
        conn_g.commit()
        conn_g.close()
        await ctx.send('creation complete!')




def setup(client):
    client.add_cog(Database(client))
