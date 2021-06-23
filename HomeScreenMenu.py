from FractionalKnapSack import FractionalKnapSack
from IOKnapSack import IOKnapSack
from ReadData import ReadData
class HomeScreenMenu:

    def __init__(self, choice):
        self.choice = choice
        self.menu_sub = {
                    "1": "A",
                    "2": "B",
                    "3": "C",
                    "4": "D",
                }
        self.menu_choices = {
            "1": {
                "1": self.menu_sub,
                "2": self.menu_sub
            },
            "2": "C",
            "3": False,
        }
        # self.menu()

    # 1 - The type of Knapsack(Fractional - I / 0)
    # 2 - The cost function based on(Maximum Profit - Minimum Weight - Maximum Profit / Weight - All)
    # 3 - Update the objects and the maximum weight of the knapsack(constraint)
    # 4 - Close the program

    def menu(self):
        if self.choice in self.menu_choices:
            if self.choice == "1":
                function_choice = input("1- Fractional Knapsack\n2- I/O Knapsack\n")
                if function_choice in ["1", "2"]:
                    choice = input("1- Maximum Profit\n2- Minimum Weight\n3- Maximum Profit / Weight\n4- All\n")
                    if choice in self.menu_sub:
                        pass
                    else:
                        print("Entered a wrong choice please try again.")
                        return True
                else:
                    print("Entered a wrong choice please try again.")
                    return True
            else:
                return self.menu_choices[self.choice]
        else:
            print("Entered a wrong choice please try again.")
            return True