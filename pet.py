from status import Status

class Pet:
    def __init__(self, Name=""):
        self.Name = Name
        self.Status = Status()

    def Feed(self, chosenFood):
        self.Status.Hunger -= chosenFood.ReducesHungerBy
        self.Status.Energy += chosenFood.AddsEnergy
        self.LimitStatus()

    def Play(self, chosenToy):
        self.Status.Happiness += chosenToy.AddsHappiness
        self.Status.Energy -= chosenToy.CostsEnergy
        self.LimitStatus()

    def SpendTime(self, choice):
        if choice == 1:  # krótka przerwa
            self.Status.Hunger += 5
            self.Status.Happiness -= 5
            self.Status.Energy += 5
        elif choice == 2:  # drzemka
            self.Status.Hunger += 10
            self.Status.Happiness -= 5
            self.Status.Energy += 15
        elif choice == 3:  # spanie
            self.Status.Hunger += 15
            self.Status.Happiness -= 10
            self.Status.Energy += 25
        elif choice == 4:  # spacer
            self.Status.Hunger += 10
            self.Status.Happiness += 15
            self.Status.Energy -= 10
        else:
            return

        self.LimitStatus()

    def LimitStatus(self):
        if self.Status.Hunger < 0:
            self.Status.Hunger = 0
        if self.Status.Hunger > 100:
            self.Status.Hunger = 100

        if self.Status.Happiness < 0:
            self.Status.Happiness = 0
        if self.Status.Happiness > 100:
            self.Status.Happiness = 100

        if self.Status.Energy < 0:
            self.Status.Energy = 0
        if self.Status.Energy > 100:
            self.Status.Energy = 100

    def IsGameOver(self):
        # TODO
        return False