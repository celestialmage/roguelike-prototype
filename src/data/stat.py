from .constants import DEFAULT_STATS


class Stat:
    def __init__(self, name, score, prof_bonus=2):
        self.name = name
        self.abbr = name[:3].upper()
        self.score = score
        self.mod = self.update_mod()
        self.save = self.update_save(prof_bonus)

    def update_score(self, score):
        self.score = score
        self.mod = self.update_mod()
        self.save = self.update_save()

    def update_mod(self):
        return (self.score // 2) - 5

    def update_save(self, prof_bonus):
        return self.mod + prof_bonus

    def __str__(self):
        return str(self.__dict__)


class StatList:
    def __init__(self, stats, prof_bonus=2):
        self.insert_stats(stats, prof_bonus)

    def insert_stats(self, stats, prof_bonus):
        for i in range(len(stats)):
            setattr(self, DEFAULT_STATS[i].lower(), Stat(
                DEFAULT_STATS[i], stats[i], prof_bonus))

    def __str__(self):
        return str(self.__dict__)
