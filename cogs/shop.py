import discord
from discord.ext import commands
import sqlite3
import data

class Shop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('[SYSTEM] shop is online')

    @commands.command()
    async def shop(self, ctx):
        for rod, info in data.rods.items():
            if info["shop"]:
                await ctx.send(str(rod) +  "- $" + str(info["cost"]))

    @commands.command()
    async def buy(self, ctx, item, type):
        product = item + " " + type
        if product in data.rods.keys():
            conn = sqlite3.connect('databases/players.db')
            cur = conn.cursor()
            player = cur.execute('SELECT * FROM users WHERE id="' + str(ctx.author.id) + "_" + str(ctx.guild.id) + '"')
            for i in player:
                if int(i[5]) < data.rods[product]["cost"]:
                    await ctx.send("you do not have enough money for " + product)
                    break
                if i[1] == product:
                    await ctx.send(product + " already bought!")
                    break
                newCoins = str(int(i[5]) - data.rods[product]["cost"])
                cur.execute('UPDATE users SET money = ' +  newCoins + ', rod = "' + product + '" WHERE id ="' + str(ctx.author.id) + "_" + str(ctx.guild.id) + '"')
                await ctx.send(product + " purchased!")
            conn.commit()
            conn.close()
        else:
            await ctx.send(product + " not found.")

def setup(client):
    client.add_cog(Shop(client))
