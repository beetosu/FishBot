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
    async def buy(self, ctx, item, type, amt=1):
        product = item + " " + type
        if product in data.rods.keys():
            conn = sqlite3.connect('databases/players.db')
            cur = conn.cursor()
            player = cur.execute('SELECT id, money FROM users WHERE id="' + str(ctx.author.id) + "_" + str(ctx.guild.id) + '"')
            conn_i = sqlite3.connect('databases/inv.db')
            cur_i  = conn_i.cursor()
            for i in player:
                if int(i[1]) < data.rods[product]["cost"]:
                    await ctx.send("you do not have enough money for " + product)
                    break
                dup = cur_i.execute('SELECT * FROM user' + str(ctx.author.id)  + '_' + str(ctx.guild.id) + ' WHERE name="' + product + '"')
                if type == "Rod":
                    for i in dup:
                        await ctx.send("you already own " + product)
                        break
                newCoins = str(int(i[1]) - data.rods[product]["cost"])
                cur.execute('UPDATE users SET money = ' +  newCoins + ', rod = "' + product + '" WHERE id ="' + str(ctx.author.id) + "_" + str(ctx.guild.id) + '"')
                quantity = 0
                for i in dup:
                    quantity = int(i[2])
                cur_i.execute('INSERT INTO user' + str(ctx.author.id) + '_' + str(ctx.guild.id) + ' VALUES ("' + product +  '", "' + type + '", ' + str(quantity+amt) + ')')
                await ctx.send(product + " purchased!")
            conn_i.commit()
            conn.commit()
            conn_i.close()
            conn.close()
        else:
            await ctx.send(product + " not found.")

def setup(client):
    client.add_cog(Shop(client))
