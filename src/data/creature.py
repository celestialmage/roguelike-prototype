from src.data.stat import StatList
from src.data.skill import SkillList


class Creature:

    def __init__(self, creature: dict):
        self.name = creature["name"]
        self.prof_bonus = creature["prof_bonus"]
        self.type = creature["type"]
        self.stats = StatList(creature["stats"])
        self.skills = SkillList(self, self.prof_bonus)

    def __str__(self):
        return str(self.__dict__)
