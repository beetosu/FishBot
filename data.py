ready_fish = {}

structure = [{"useless": 1, "good": 1}]

fish_types = [
    [{"name": "Boot", "emoji": ":boot:", "points": 5, "money":0},
    {"name": "Tuna", "emoji": ":fish:", "points": 5, "money": 10},
    {"name": "Yellow Tang", "emoji": ":tropical_fish:", "points": 15, "money": 15},
    {"name": "Pufferfish", "emoji": ":blowfish:", "points": 35, "money": 20}],

    [{"name": "Super Boot", "emoji": ":high_heel:", "points": 10, "money": 0}]]

rods = {
    "Flimsy Rod": {
        "desc": "Just the basics, nothing too fancy going on here.",
        "attraction": 1,
        "catch": 1,
        "shop": False,
        "cost": 0
        },
    "Sturdy Rod": {
        "desc": "Like the wooden pole, but a little hartier.\nMore forgiving catch rate",
        "attraction": 1,
        "catch": 1.5,
        "shop": True,
        "cost": 20
        }
}

bait = {
    "Worm": {
        "desc": "A little worm fella.\ngood at attracting all kinds of fish.",
        "cost": 1,
        "useless_attraction": 1,
        "attraction": 1.2,
        "rare_attraction": 1.2,
        "speed": 1.1,
        "catch": 1
    },
    "Toy Fish": {
        "desc": "A little dangly plastic fish\nLittle spikes make it hard for a fish to detach from it.",
        "cost": 2,
        "useless_attraction": 1.1,
        "attraction": 1.1,
        "rare_attraction": 1.1,
        "speed": 1,
        "catch": 1.3
    }
}

reel = [{
        "desc": "The standard amount, only reaches the surface of the sea",
        "cost": 0,
        "shop": False
    },
    {
        "desc": "Twice as long as the standard reel, able to reach the twilight zone",
        "cost": 100,
        "shop": False
    }
]

bait = []

fish_odds = [[.385, .385, .192, .038], [1]]
