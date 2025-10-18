from GameObject import GameObject


class NPC(GameObject):
    def __init__(self, name, description, dialogue, location=None):
        super().__init__(name, description, location)
        self.dialogue = dialogue

    def talk(self):
        return self.dialogue