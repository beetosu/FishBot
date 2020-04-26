import sqlite3

def create_player(player, guild):
    conn_p = sqlite3.connect('databases/players.db')
    cur_p = conn_p.cursor()
    cur_p.execute('INSERT INTO users VALUES ("' + str(player.id) + "_" + str(guild.id) + '", "Wooden Pole", 1, 1, "none", 0, 0)')
    conn_p.commit()
    print("[DATABASE] " + player.nick + " of guild " + guild.name + " added to database")
    conn_p.close()
