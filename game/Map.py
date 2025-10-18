from GameObject import GameObject


class Map(GameObject):
    def __init__(self, name, description, location=None):
        super().__init__(name, description, location)

    def __str__(self):
        return f"{self.name}: {self.description} (A map to help you navigate!)"