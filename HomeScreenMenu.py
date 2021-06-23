class HomeScreenMenu:
    def __init__(self, choice):
        self.choice = choice
        self.menu_choices = {
            "1": "A",
            "2": "B",
            "3": "C",
            "4": "D",
        }

    # 1 - The type of Knapsack(Fractional - I / 0)
    # 2 - The cost function based on(Maximum Profit - Minimum Weight - Maximum Profit / Weight - All)
    # 3 - Update the objects and the maximum weight of the knapsack(constrain)
    # 4 - Close the program

    def menu(self):
        if self.choice in self.menu_choices:
            return self.menu_choices[self.choice]
        else:
            return "Entered a wrong choice please try again."