from src.data.creature import Creature

lil_guy = {
    "name": "Goblin",
    "prof_bonus": 2,
    "type": "humanoid",
    "stats": [8, 14, 10, 10, 8, 8]
}

goblin = Creature(lil_guy)

print(goblin.stats.get_summary())