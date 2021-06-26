class IOKnapSack:

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
        return self.apply_io_knapsack()

    def apply_io_knapsack(self):
        total_value = 0
        i = 0
        while self.capacity > 0:
            try:
                print('Capacity = ', self.capacity)
                if self.capacity - self.df['Weight'].iloc[i] >= 0:
                    total_value += self.df['Value'].iloc[i]
                    self.capacity -= self.df['Weight'].iloc[i]
                i += 1
            except IndexError:
                break
        print(self.capacity)
        return total_value