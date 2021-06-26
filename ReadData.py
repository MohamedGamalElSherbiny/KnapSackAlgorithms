import pandas as pd
class ReadData:

    def __init__(self):
        self.weight = []
        self.value = []
        self.capacity = 0.0
        self.value_per_weight = [self.value[i] / self.weight[i] for i in range(len(self.weight))]

    def create_dataframe(self):
        print(self.weight)
        print(self.value)
        print(self.capacity)
        items = {"Weight": self.weight,
                 "Value": self.value,
                 "Value Per Weight": self.value_per_weight
                 }
        return pd.DataFrame.from_dict(items)

    def create_weight_value(self, count):
        for i in range(count):
            user_input = float(input("Please enter your weight number: \n"))
            self.weight.append(user_input)
            print(self.weight)
            user_input = float(input("Please enter the value: \n"))
            self.value.append(user_input)
            print(self.value)
        on = True
        while on:
            self.capacity = float(input("Please enter the capacity: \n"))
            if self.capacity == 0.0:
                print("Wrong capacity")
            else:
                on = False