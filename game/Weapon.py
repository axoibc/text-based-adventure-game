from GameObject import GameObject


class Weapon(GameObject):
    def __init__(self, name, description, damage, location=None):
        super().__init__(name, description, location)
        self.damage = damage

    def __str__(self):
        return f"{self.name}: {self.description} (Damage: {self.damage})"