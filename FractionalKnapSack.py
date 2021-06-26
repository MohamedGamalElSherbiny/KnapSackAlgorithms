class FractionalKnapSack:

    def __init__(self, df, capacity):
        self.df = df
        self.capacity = capacity

    def choose_type(self, output_type):
        if output_type == "1":
            self.df = self.df.sort_values(by='Value', ascending=False)
        elif output_type == "2":
            self.df = self.df.sort_values(by='Weight')
        elif output_type == "3":
            self.df = self.df.sort_values(by='Value Per Weight')
        return self.apply_fractional_knapsack()

    def apply_fractional_knapsack(self):
        total_value = 0
        i = 0
        while self.capacity > 0:
            print('Capacity = ', self.capacity)
            if self.capacity - self.df['Weight'].iloc[i] >= 0:
                total_value += self.df['Value'].iloc[i]
                self.capacity -= self.df['Weight'].iloc[i]
            else:
                fraction = self.capacity / self.df['Weight'].iloc[i]
                total_value += self.df['Value'].iloc[i] * fraction
                self.capacity -= self.df['Weight'].iloc[i] * fraction
                print(self.capacity)
                break
            i += 1
        print(total_value)
        return total_value