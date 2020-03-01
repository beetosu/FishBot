ready_fish = {}

fish_types = [
    [{"name": "Boot", "emoji": ":boot:", "points": 5, "money":0},
    {"name": "Tuna", "emoji": ":fish:", "points": 5, "money": 10},
    {"name": "Yellow Tang", "emoji": ":tropical_fish:", "points": 15, "money": 15},
    {"name": "Pufferfish", "emoji": ":blowfish:", "points": 35, "money": 20}],

    [{"name": "Super Boot", "emoji": ":high_heel:", "points": 10, "money": 0}]]

rods = {
    "Wooden Pole": {
        "desc": "Just the basics, nothing too fancy going on here.",
        "attraction": 1,
        "catch": 1,
        "shop": False,
        "cost": 0
        },
    "Sturdy Pole": {
        "desc": "Like the wooden pole, but a little hartier.\nMore forgiving catch rate",
        "attraction": 1,
        "catch": 2,
        "shop": True,
        "cost": 20
        }
}

reel = {
    1: {
        "desc": "The standard amount, only reaches the surface of the sea",
        "cost": 0,
        "shop": False
    },
    2: {
        "desc": "Twice as long as the standard reel, able to reach the twilight zone",
        "cost": 100,
        "shop": False
    }
}

bait = []

fish_odds = [[.385, .385, .192, .038], [1]]
