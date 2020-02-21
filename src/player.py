class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return self.name
