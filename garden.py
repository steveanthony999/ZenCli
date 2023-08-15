import csv
import os


class Plant:
    GROWTH_STAGES = ["seed", "seedling", "adult plant", "flower", "fruit/seed"]

    def __init__(self, name, description, color):
        self.name = name
        self.description = description
        self.color = color
        self.current_stage = 0  # Starts at "seed"
        self.health = 100  # Starts fully healthy

    def grow(self):
        if self.current_stage < len(self.GROWTH_STAGES) - 1:
            self.current_stage += 1

    def wilt(self, amount=10):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount=5):
        self.health += amount
        if self.health > 100:
            self.health = 100

    @property
    def stage(self):
        return self.GROWTH_STAGES[self.current_stage]

    def is_fully_grown(self):
        return self.current_stage == len(self.GROWTH_STAGES) - 1

    def is_dead(self):
        return self.health == 0


class Garden:
    def __init__(self, owner_username):
        self.owner_username = owner_username
        self.plants = []
        self.final_garden = []
        self.trash = []  # Dead plants go here

    def add_plant(self, plant):
        self.plants.append(plant)

    def transfer_to_final_garden(self, plant):
        if plant.is_fully_grown():
            self.final_garden.append(plant)
            self.plants.remove(plant)

    def transfer_to_trash(self, plant):
        if plant.is_dead():
            self.trash.append(plant)
            self.plants.remove(plant)

    def calculate_score(self):
        zen_health = {
            "In Progress": len(self.plants),
            "Final Garden": len(self.final_garden),
            "Trash": len(self.trash),
        }
        return zen_health

    def save_to_csv(self):
        with open(
            "{owner_username}_garden.csv".format(owner_username=self.owner_username),
            "w",
            newline="",
        ) as file:
            writer = csv.writer(file)
            writer.writerow(["Plant Name", "Current Stage", "Description", "Color"])
            for plant in self.plants:
                writer.writerow(
                    [plant.name, plant.stage, plant.description, plant.color]
                )

    @classmethod
    def load_from_csv(cls, username):
        garden = cls(username)
        if os.path.exists("{username}_garden.csv".format(username=username)):
            with open(
                "{username}_garden.csv".format(username=username), "r", newline=""
            ) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    plant = Plant(row["Plant Name"], row["Description"], row["Color"])
                    plant.current_stage = Plant.GROWTH_STAGES.index(
                        row["Current Stage"]
                    )
                    garden.add_plant(plant)
        return garden
