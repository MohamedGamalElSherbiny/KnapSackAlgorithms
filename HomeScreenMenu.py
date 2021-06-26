from FractionalKnapSack import FractionalKnapSack
from IOKnapSack import IOKnapSack
from ReadData import ReadData
CAPACITY = 50
class HomeScreenMenu:

    def __init__(self, choice):
        weight = [10, 40, 20, 30]
        value = [60, 40, 100, 120]
        self.df = ReadData(weight, value).create_dataframe()
        self.choice = choice
        self.capacity = 50
        self.knapsack = [FractionalKnapSack(self.df, CAPACITY), IOKnapSack(self.df, CAPACITY)]
        self.function_choice = 0

    def menu(self):
        global CAPACITY
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
                CAPACITY = int(input("Please enter the new capacity value: "))
                return True
            elif self.choice == "3":
                return False
        else:
            print("Entered a wrong choice please try again.")
            return True