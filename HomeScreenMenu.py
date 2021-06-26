from FractionalKnapSack import FractionalKnapSack
from IOKnapSack import IOKnapSack
from ReadData import ReadData
class HomeScreenMenu:

    def __init__(self, choice):
        self.df = ReadData().create_dataframe()
        self.data_in = True
        self.on = True
        self.choice = choice
        self.capacity = ReadData().capacity
        self.knapsack = [FractionalKnapSack(self.df, self.capacity), IOKnapSack(self.df, self.capacity)]
        self.function_choice = 0
        self.menu()

    def menu(self):
        if self.choice in ["1", "2", "3"]:
            if self.choice == "1":
                self.function_choice = input("1- Fractional Knapsack\n2- I/O Knapsack\n")
                if self.function_choice in ["1", "2"]:
                    choice = input("1- Maximum Profit\n2- Minimum Weight\n3- Maximum Profit / Weight\n")
                    if choice in ["1", "2", "3"]:
                        total_value = self.knapsack[int(self.function_choice) - 1].choose_type(choice)
                        print(f"Total value after adding is : {total_value}")
                        return True
                    else:
                        print("Entered a wrong choice please try again.")
                        return True
                else:
                    print("Entered a wrong choice please try again.")
                    return True
            elif self.choice == "2":
                self.on = False
                return
            elif self.choice == "3":
                self.data_in = False
                self.on = False
                return
        else:
            print("Entered a wrong choice please try again.")
            return True