from ReadData import ReadData
from HomeScreenMenu import HomeScreenMenu

data_in = True
while data_in:
    user_choice = input("1- Input your data using csv.\n"
                        "2- Input your data as a list.\n")
    if user_choice in "2":
        if user_choice == "2":
            count = int(input("Please enter the amount of numbers to enter: "))
            data = ReadData().create_weight_value(count=count)
        elif user_choice == "1":
            path = input("Please enter the full file path: \n")
            ## I didn't implement the csv reading
        on = True
    else:
        on = False
    while on:
        user_choice = input("1- Fractional Knapsack OR I/O Knapsack\n"
                            "2- Update input Data\n"
                            "3- Exit the application\n")
        on, data_in = HomeScreenMenu(user_choice, data).on, HomeScreenMenu(user_choice, data).data_in
    on = True

# weight = [10, 40, 20, 30]
# value = [60, 40, 100, 120]
# capacity = 70
