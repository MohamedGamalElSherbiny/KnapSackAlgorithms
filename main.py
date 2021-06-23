from ReadData import ReadData
from HomeScreenMenu import HomeScreenMenu

weight = [1, 2, 3, 4, 5, 6, 7, 8]
value = [1, 2, 3, 4, 5, 6, 7, 8]
read_data = ReadData(weight, value)
print(read_data.create_dataframe())

on = True
while on:
    user_choice = input("1- Fractional Knapsack OR I/O Knapsack\n"
                        "2- Update input Data\n"
                        "3- Exit\n")
    on = HomeScreenMenu(user_choice).menu()