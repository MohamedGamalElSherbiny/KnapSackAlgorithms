class FractionalKnapSack:

    @staticmethod
    def get_max_profit(df, capacity):
        total_value = 0
        df.sort_values(by='Value', ascending=False)
        for _ in df:
            if capacity - df['Weight'] >= 0:
                total_value += df['Value']
            else:
                fraction = capacity / df['Weight']
                total_value += df['Value'] * fraction
                break
        return total_value

    @staticmethod
    def get_minimum_weight(df, capacity):
        total_value = 0
        df.sort_values(by='Weight')
        for _ in df:
            if capacity - df['Weight'] >= 0:
                total_value += df['Value']
            else:
                fraction = capacity / df['Weight']
                total_value += df['Value'] * fraction
                break
        return total_value

    @staticmethod
    def get_maximum_profit_over_weight(df, capacity):
        total_value = 0
        df.sort_values(by='Value Per Weight')
        for _ in df:
            if capacity - df['Weight'] >= 0:
                total_value += df['Value']
            else:
                fraction = capacity / df['Weight']
                total_value += df['Value'] * fraction
                break
        return total_value