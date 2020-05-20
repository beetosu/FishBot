import sqlite3
import data

def create_player(player, guild):
    conn_p = sqlite3.connect('databases/players.db')
    cur_p = conn_p.cursor()
    cur_p.execute('INSERT INTO users VALUES ("' + str(player.id) + "_" + str(guild.id) + '", "Flimsy Rod", 1, 1, "none", 0, 0, "' + str(guild.id) + '")')
    conn_p.commit()
    print("[DATABASE] " + player.name + " of guild " + guild.name + " added to players.db")
    conn_p.close()

    conn_i = sqlite3.connect('databases/inv.db')
    cur_i = conn_i.cursor()
    cur_i.execute('CREATE TABLE IF NOT EXISTS user' + str(player.id) + '_' + str(guild.id) + '(name, type, quantity)')
    cur_i.execute('INSERT INTO user' + str(player.id) + '_' + str(guild.id) + ' VALUES ("Flimsy Rod", "Rod", 1)')
    conn_i.commit()
    print("[DATABASE] " + player.name + " of guild " + guild.name + " added to inv.db")
    conn_i.close()

def get_player(ctx):
    conn_p = sqlite3.connect('databases/players.db')
    cur_p = conn_p.cursor()
    test = cur_p.execute('SELECT COUNT(*) FROM users WHERE id="' + str(ctx.author.id) + '_' + str(ctx.guild.id) + '"')
    for i in test:
        if i[0] == 0:
            create_player(ctx.author, ctx.guild)
        return cur_p.execute('SELECT * FROM users WHERE id="' + str(ctx.author.id) + '_' + str(ctx.guild.id) + '"')
