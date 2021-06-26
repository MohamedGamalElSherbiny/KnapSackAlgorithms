from ReadData import ReadData
from HomeScreenMenu import HomeScreenMenu

data_in = True
while data_in:
    user_choice = input("1- Input your data using csv.\n"
                        "2- Input your data as a list.\n")
    if user_choice in ["1", "2"]:
        if user_choice == "1":
            count = int(input("Please enter the amount of numbers to enter: "))
            ReadData().create_weight_value(count=count)
        elif user_choice == "2":
            path = input("Please enter the full file path: \n")
        on = True
    else:
        on = False
    print(on)
    while on:
        user_choice = input("1- Fractional Knapsack OR I/O Knapsack\n"
                            "2- Update input Data\n"
                            "3- Exit the application\n")
        on, data_in = HomeScreenMenu(user_choice).on, HomeScreenMenu(user_choice).data_in
        print(on, data_in)
    on = True

# weight = [10, 40, 20, 30]
# value = [60, 40, 100, 120]
