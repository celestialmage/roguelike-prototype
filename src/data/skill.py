from ..constants.constants import SKILL_CHART


class Skill:
    def __init__(self, name: str, mod: int, prof_bonus: int, trained: int = 0):
        self.name = name
        self.trained = trained
        self.bonus = self.update_bonus(mod, prof_bonus)

    def update_bonus(self, mod: int, prof_bonus: int):
        return mod + (prof_bonus * self.trained)

    def update_trained(self, mod: int, prof_bonus: int, trained: int = 0):
        self.trained = trained
        self.bonus = self.update_bonus(mod, prof_bonus)

    def __str__(self):
        return str(self.__dict__)


class SkillList:
    def __init__(self, mods, skills):
        self.create_skills(mods, skills)

    def create_skills(self, creature, prof_bonus):
        for skill, stat in SKILL_CHART.items():
            setattr(self, skill.lower(), Skill(skill, getattr(
                creature.stats, stat).mod, prof_bonus, 0))

    def __str__(self):
        return str(self.__dict__)
