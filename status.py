class Status:
    def __init__(self, Hunger=50, Happiness=50, Energy=80):
        self.Hunger = Hunger
        self.Happiness = Happiness
        self.Energy = Energy

    def __str__(self):
        return (
            f"Głód: {self.Hunger}/100\n"
            f"Szczęście: {self.Happiness}/100\n"
            f"Energia: {self.Energy}/100\n"
        )