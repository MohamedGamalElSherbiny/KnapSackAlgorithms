import pandas as pd
class ReadData:

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.value_per_weight = [self.value[i] / self.weight[i] for i in range(len(self.weight))]

    def create_dataframe(self):
        items = {"Weight": self.weight,
                 "Value": self.value,
                 "Value Per Weight": self.value_per_weight
                 }
        return pd.DataFrame.from_dict(items)