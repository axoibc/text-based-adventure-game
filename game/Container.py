from GameObject import GameObject


class Container(GameObject):
    def __init__(self, name, description, capacity, location=None):
        super().__init__(name, description, location)
        self.capacity = capacity
        self.contents = []

    def add_item(self, item):
        if len(self.contents) < self.capacity:
            self.contents.append(item)
            return True
        return False

    def __str__(self):
        return f"{self.name}: {self.description} (Capacity: {self.capacity}, Items: {len(self.contents)})"