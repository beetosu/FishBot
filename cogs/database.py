import discord
from discord.ext import commands
import sqlite3, asyncio, json
import playerdb

#this is just handling accessing the database outside of fishing and catching

class Database(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('[SYSTEM] database is online')

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
        guild: the guild a user is currently in
    WARNING: doesn't currently override whatever db currently exists
    TO DO: maybe fix that??
    '''
    @commands.command()
    async def createdb(self, ctx):
        conn_p = sqlite3.connect('databases/players.db')
        cur_p = conn_p.cursor()
        await ctx.send('databases loaded!')
        cur_p.execute('CREATE TABLE IF NOT EXISTS users (id, rod, reel_max, reel, bait, money, points, guild)')
        conn_p.commit()
        conn_p.close()
        print("[DATABASE] players.db established")
        await ctx.send('creation complete!')

    #get current player stats
    @commands.command()
    async def stats(self, ctx):
        player = playerdb.get_player(ctx)
        for i in player:
            await ctx.send(f'your current rod is: {i[1]}\nyour reel length is: {i[3]}\nyour bait is: {i[4]}\nyou have {i[5]} coins\nyour total points is: {i[6]}')

    @commands.command()
    async def leaderboard(self, ctx):
        conn_p = sqlite3.connect('databases/players.db')
        cur_p = conn_p.cursor()
        players = cur_p.execute('SELECT id, points FROM users WHERE guild="' + str(ctx.guild.id) + '" ORDER BY points ASC')
        for i in players:
            await ctx.send(f'{ctx.guild.get_member(int(i[0].split("_")[0])).nick}: {i[1]} points')

    #revert player who envokes this command back to default values
    @commands.command()
    async def clear(self, ctx):
        await ctx.send(f'Are you sure you want to clear save data? Cleared data cannot be recovered!\nType "yes" now to confirm.')
        def make_sure(msg):
            return msg.content == "yes"
        try:
            #hold until user confirms
            resp = await self.client.wait_for('message', check=make_sure, timeout=30.0)
        except asyncio.TimeoutError:
            #if half a minute passes, nothing is cleared
            await ctx.send("clearing process cancelled")
        else:
            conn_p = sqlite3.connect('databases/players.db')
            cur_p = conn_p.cursor()
            inv = {}
            cur_p.execute('UPDATE users SET rod = "Flimsy Rod", reel_max = 1, reel = 1, bait = "none", money = 0, points = 0, name = "' + ctx.author.name + '" WHERE id = "' + str(ctx.author.id) + "_" + str(ctx.guild.id) + '"')
            conn_p.commit()
            conn_p.close()
            conn_i = sqlite3.connect('databases/inv.db')
            cur_i = conn_i.cursor()
            cur_i.execute('DELETE FROM user' + str(ctx.author.id) + '_' + str(ctx.guild.id))
            cur_i.execute('INSERT INTO user' + str(ctx.author.id) + '_' + str(ctx.guild.id) + ' VALUES ("Flimsy Rod", "Rod", 1)')
            conn_i.commit()
            conn_i.close()
            await ctx.send(f'{ctx.author.name} data cleared')


def setup(client):
    client.add_cog(Database(client))
