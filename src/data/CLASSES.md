# Project Class Documentation

This document provides an overview of the key classes in the project, detailing their methods, attributes, and interactions.

---

## Creature

### Overview
The `Creature` class represents an entity (e.g., a player character or monster) with a name, proficiency bonus, type, stats, and skills. It aggregates two major components:
- A `StatList` instance that holds the creature's statistics.
- A `SkillList` instance that manages the creature's skills.

### Attributes
- **name** (`str`): The creature's name.
- **prof_bonus** (`int`): The proficiency bonus used in various calculations.
- **type** (`str`): The classification or type of the creature.
- **stats** (`StatList`): Contains the creature's statistics.
- **skills** (`SkillList`): Contains the creature's skills.

### Methods
- `__init__(self, creature: dict)`:  
  Initializes a `Creature` instance from a dictionary with the following keys:
  - `"name"`: Creature's name.
  - `"prof_bonus"`: Proficiency bonus.
  - `"type"`: Creature type.
  - `"stats"`: A list of stat scores used to create the creature's stats.
  
  This constructor creates a `StatList` from the provided stat scores and a `SkillList` using the creature instance (to access its stats) and the proficiency bonus.
  
- `__str__(self)`:  
  Returns a string representation of the creature's attributes (using the object's `__dict__`).

---

## Stat

### Overview
The `Stat` class models an individual statistic (such as Strength or Dexterity) with a numeric score, a derived modifier, and a saving throw value.

### Attributes
- **name** (`str`): The name of the stat (e.g., "Strength").
- **abbr** (`str`): A three-letter uppercase abbreviation (first three letters of the name).
- **score** (`int`): The raw score for the stat.
- **trained** (`bool` or `int`): Indicates if the stat is trained (default is `False`, but later used as an integer in calculations).
- **mod** (`int`): The modifier calculated as `(score // 2) - 5`.
- **save** (`int`): The saving throw value, computed as `mod + (prof_bonus * trained)`.

### Methods
- `__init__(self, name: str = "Unknown", score: int = 10, prof_bonus: int = 2)`:  
  Sets up a stat with the provided name, score, and proficiency bonus, and initializes its derived values.
  
- `update_score(self, score: int, prof_bonus: int)`:  
  Increases the stat's score by the given amount and updates both the modifier and saving throw.
  
- `update_mod(self)`:  
  Calculates and returns the modifier using `(score // 2) - 5`.
  
- `update_trained(self, prof_bonus: int, trained: int)`:  
  Updates the `trained` attribute and recalculates the saving throw.
  
- `update_save(self, prof_bonus: int)`:  
  Calculates and returns the saving throw value as `mod + (prof_bonus * trained)`.
  
- `get_score(self)`:  
  Returns the current score.
  
- `get_mod(self)`:  
  Returns the current modifier.
  
- `get_score_mod(self)`:  
  Returns a tuple `(score, mod)`.
  
- `get_save(self)`:  
  Returns the current saving throw.
  
- `__str__(self)`:  
  Provides a string representation of the stat's attributes.

---

## StatList

### Overview
The `StatList` class manages a collection of `Stat` objects. It dynamically creates attributes for each stat based on a predefined list (e.g., `DEFAULT_STATS`).

### Attributes
- **Dynamic Attributes**:  
  For each default stat (such as strength, dexterity, etc.), an attribute is created (named in lowercase) that holds a `Stat` instance.

### Methods
- `__init__(self, stats, prof_bonus: int = 2)`:  
  Initializes the list by inserting stat scores along with a proficiency bonus.
  
- `insert_stats(self, stats: list, prof_bonus: int)`:  
  Iterates over the provided list of stat scores and creates a `Stat` for each, assigning it to an attribute whose name is derived from the default stat names.
  
- `get_summary(self)`:  
  Returns a tuple summarizing each stat’s score and modifier in a specific order (e.g., strength, dexterity, constitution, intelligence, wisdom, charisma).
  
- `__str__(self)`:  
  Returns a string representation of all the stat objects contained in the list.

---

## Skill

### Overview
The `Skill` class represents a particular skill for a creature. Its bonus is computed based on a related stat’s modifier and the creature's proficiency bonus, adjusted by the training level.

### Attributes
- **name** (`str`): The skill's name.
- **trained** (`int`): The training level in the skill (default is 0).
- **bonus** (`int`): The bonus value computed as `mod + (prof_bonus * trained)`.

### Methods
- `__init__(self, name: str, mod: int, prof_bonus: int, trained: int = 0)`:  
  Initializes a skill with its name, an initial modifier (typically from a related stat), a proficiency bonus, and an optional training level. It calculates the bonus using `update_bonus`.
  
- `update_bonus(self, mod: int, prof_bonus: int)`:  
  Computes and returns the bonus using the formula:  
  `bonus = mod + (prof_bonus * trained)`.
  
- `update_trained(self, mod: int, prof_bonus: int, trained: int = 0)`:  
  Updates the training level and recalculates the bonus accordingly.
  
- `__str__(self)`:  
  Returns a string representation of the skill’s attributes.

---

## SkillList

### Overview
The `SkillList` class aggregates a set of `Skill` objects for a creature. It leverages a constant mapping (`SKILL_CHART`) to associate each skill with its corresponding stat, dynamically creating skill attributes.

### Attributes
- **Dynamic Attributes**:  
  Each key in the `SKILL_CHART` becomes an attribute on the `SkillList` (using a lowercase version of the skill name) and is assigned a `Skill` instance.

### Methods
- `__init__(self, mods, skills)`:  
  Constructs the skill list by calling `create_skills`. In practice:
  - The first parameter (`mods`) is the creature instance (which provides access to its stats).
  - The second parameter (`skills`) is the proficiency bonus.
  
- `create_skills(self, creature, prof_bonus)`:  
  Iterates over the `SKILL_CHART` items. For each skill:
  - Retrieves the corresponding stat from the creature's `StatList` (using the stat name from the chart).
  - Creates a `Skill` instance using the skill name, the stat’s modifier, the proficiency bonus, and an initial training level (0).
  - Assigns the skill to an attribute on the `SkillList` object with a lowercase name.
  
- `__str__(self)`:  
  Returns a string representation of the `SkillList` attributes.

---

## Interactions Between Classes

- **Creature and StatList**:  
  When a `Creature` is instantiated, it passes its stat scores to a new `StatList`. This list dynamically creates individual `Stat` objects (using names defined in `DEFAULT_STATS`) which hold the creature's basic statistics.

- **Creature and SkillList**:  
  The `Creature` also initializes a `SkillList`, providing itself (to access its stats) and its proficiency bonus. The `SkillList` uses the creature's stats to compute each skill's bonus based on the mapping in `SKILL_CHART`.

- **Stat and Skill**:  
  A key interaction is that each `Skill` relies on a modifier from a corresponding `Stat` (retrieved via the creature's `StatList`) and the proficiency bonus to compute its bonus value.