from GameObject import GameObject


class Key(GameObject):
    def __init__(self, name, description, unlocks, location=None):
        super().__init__(name, description, location)
        self.unlocks = unlocks

    def __str__(self):
        return f"{self.name}: {self.description} (Unlocks: {self.unlocks})"