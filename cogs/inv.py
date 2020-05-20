import discord
from discord.ext import commands
import sqlite3, asyncio

#this is just handling accessing the database outside of fishing and catching

class Inv(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('[SYSTEM] database is online')

    @commands.command()
    async def inv(self, ctx):
        conn = sqlite3.connect('databases/inv.db')
        cur  = conn.cursor()
        stuff = cur.execute('SELECT * FROM user' + str(ctx.author.id)  + '_' + str(ctx.guild.id))
        for i in stuff:
            await ctx.send(i[0] + " (x" + str(i[2]) + ")")
        cur.close()

    @commands.command()
    async def equip(self, ctx, item, type):
        conn_i = sqlite3.connect('databases/inv.db')
        cur_i = conn_i.cursor()
        conn_p = sqlite3.connect('databases/players.db')
        cur_p = conn_p.cursor()
        thing = cur_i.execute('SELECT name FROM user' + str(ctx.author.id)  + '_' + str(ctx.guild.id) + ' WHERE name="' + item + ' ' + type + '"')
        found = False
        for i in thing:
            found = True
            break
        if found:
            cur_p.execute('UPDATE users SET rod = "' + item + " " + type + '" WHERE id = "' + str(ctx.author.id) + "_" + str(ctx.guild.id) + '"')
            conn_p.commit()
            await ctx.send("Equipped " + item + " " + type + "!")
        else:
            await ctx.send('"' + item + ' ' + type + '" not found!')
        cur_i.close()
        cur_p.close()

def setup(client):
    client.add_cog(Inv(client))
