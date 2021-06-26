import pandas as pd
class ReadData:

    def __init__(self):
        self.weight = []
        self.value = []
        self.capacity = 0.0
        self.value_per_weight = [self.value[i] / self.weight[i] for i in range(len(self.weight))]

    @staticmethod
    def create_dataframe(weight, value, value_per_weight):
        items = {"Weight": weight,
                 "Value": value,
                 "Value Per Weight": value_per_weight
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
        return self.weight, self.value, self.capacity