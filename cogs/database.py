import discord
from discord.ext import commands
import sqlite3

#this is just handling accessing the database outside of fishing and catching

class Database(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('database is online')

    '''
    makes the current db by whatever the current needs are

    current format:
        id [userid_guildid]: the id of a user on a particular server
        rod: current rod being used
        reel_max: the max reel length a player has
        reel: the current length a player is using
        bait: the bait currently being used by player, if any
        money: $ currently possessed
        points: points currently possessed
    WARNING: doesn't currently override whatever db currently exists
    TO DO: maybe fix that??
    '''
    @commands.command()
    async def createdb(self, ctx):
        conn_p = sqlite3.connect('databases/players.db')
        cur_p = conn_p.cursor()
        await ctx.send('databases loaded!')
        print("hi")
        cur_p.execute('CREATE TABLE IF NOT EXISTS users (id, rod, reel_max, reel, bait, money, points)')
        print("fugg")
        for i in ctx.guild.members:
            print(i.id)
            if i.id != 505135772027060224:
                cur_p.execute('INSERT INTO users VALUES ("' + str(i.id) + "_" + str(ctx.guild.id) + '", "Wooden Pole", 1, 1, "none", 0, 0)')
                await ctx.send(f'{i.name} added!')
        conn_p.commit()
        conn_p.close()
        await ctx.send('creation complete!')

    #get current player stats
    @commands.command()
    async def stats(self, ctx):
        conn_p = sqlite3.connect('databases/players.db')
        cur_p = conn_p.cursor()
        player = cur_p.execute('SELECT * FROM users WHERE id="' + str(ctx.author.id) + "_" + str(ctx.guild.id) + '"')
        for i in player:
            await ctx.send(f'your current rod is: {i[1]}\nyour reel length is: {i[3]}\nyour bait is: {i[4]}\nyou have {i[5]} coins\nyour total points is: {i[6]}')
        conn_p.close()

    #revert player who envokes this command back to default values
    @commands.command()
    async def clear(self, ctx):
        conn_p = sqlite3.connect('databases/players.db')
        cur_p = conn_p.cursor()
        cur_p.execute('UPDATE users SET rod = "Wooden Pole", reel_max = 1, reel = 1, bait = "none", money = 0, points = 0 WHERE id = "' + str(ctx.author.id) + "_" + str(ctx.guild.id) + '"')
        conn_p.commit()
        conn_p.close()
        await ctx.send(f'{ctx.author.nick} data cleared')


def setup(client):
    client.add_cog(Database(client))
