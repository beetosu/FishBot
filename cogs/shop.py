import discord
from discord.ext import commands
import sqlite3
import data, playerdb

class Shop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('[SYSTEM] shop is online')

    @commands.command()
    async def shop(self, ctx):
        await ctx.send("RODS:\n(type `f!buy [ROD NAME]` to purchase.)")
        for rod, info in data.rods.items():
            if info["shop"]:
                await ctx.send(str(rod) +  "- $" + str(info["cost"]))
        player = playerdb.get_player(ctx)
        for i in player:
            currentReel = data.reel[int(i[2])]
            await ctx.send("REEL LENGTH " + str(int(i[2]) + 1) + ": $" + str(currentReel["cost"]))
            break


    #processes a rod/bait/reel purchase
    @commands.command()
    async def buy(self, ctx, item, type="", amt=1):
        product = item + " " + type
        if type == "":
            product = item
        #if the product exists
        if product in data.rods.keys():
            conn = sqlite3.connect('databases/players.db')
            cur = conn.cursor()
            #I could do the "if user doesn't exist, add them", but they start broke anyway, and that sacrifices getting jus the values I want.
            player = cur.execute('SELECT id, money, reel_max FROM users WHERE id="' + str(ctx.author.id) + "_" + str(ctx.guild.id) + '"')
            conn_i = sqlite3.connect('databases/inv.db')
            cur_i  = conn_i.cursor()
            count = 0
            for i in player:
                count += 1
                #if they don't have the money
                if int(i[1]) < data.rods[product]["cost"] * amt:
                    await ctx.send("you do not have enough money for " + product)
                    break
                #if they're buying a rod, check that they don't already own it.
                if type == "Rod":
                    dupFound = False
                    dup = cur_i.execute('SELECT * FROM user' + str(ctx.author.id)  + '_' + str(ctx.guild.id) + ' WHERE name="' + product + '"')
                    for i in dup:
                        dupFound = True
                        break
                    if dupFound:
                        await ctx.send("you already own " + product)
                        break
                #make the monetary transaction
                newCoins = str(int(i[1]) - data.rods[product]["cost"])
                cur.execute('UPDATE users SET money = ' +  newCoins + ', rod = "' + product + '" WHERE id ="' + str(ctx.author.id) + "_" + str(ctx.guild.id) + '"')
                #if duplicates exist, in a item type that allows for duplicates, change the quantity
                quantity = 0
                for i in dup:
                    quantity = int(i[2])
                cur_i.execute('INSERT INTO user' + str(ctx.author.id) + '_' + str(ctx.guild.id) + ' VALUES ("' + product +  '", "' + type + '", ' + str(quantity+amt) + ')')
                await ctx.send(product + " purchased!")
            conn_i.commit()
            conn.commit()
            conn_i.close()
            conn.close()
            if count == 0:
                await ctx.send("you do not have enough money for " + product)
        else:
            await ctx.send('"' + product + '" not found.')

def setup(client):
    client.add_cog(Shop(client))
