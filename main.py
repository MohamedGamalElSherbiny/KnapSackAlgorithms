from ReadData import ReadData
from HomeScreenMenu import HomeScreenMenu

on = True
while on:
    user_choice = input("1- Fractional Knapsack OR I/O Knapsack\n"
                        "2- Update input Data\n"
                        "3- Exit\n")
    on = HomeScreenMenu(user_choice).menu()
