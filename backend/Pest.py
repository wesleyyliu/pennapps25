class Pest:
    def __init__(self, name: str, timeStamps, description: str):
        self.name = name
        self.timeStamps = timeStamps
        self.description = description
        self.added = False