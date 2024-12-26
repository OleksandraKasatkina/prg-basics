class Statistics:
    def __init__(self):
        self.numbers = []
        
    def add_number(self, number):
        self.numbers.append(number)

    def display_numbers(self):
        print("Numbers:", *self.numbers)

    def get_max(self):
        return max(self.numbers)
    
    def get_min(self):
        return min(self.numbers)
    
    def get_mean(self):
        return sum(self.numbers)/len(self.numbers)
    
    def get_median(self):
        sorted_numbers = sorted(self.numbers)
        length = len(sorted_numbers)
        if length % 2 == 0:
            # If even, the median is the average of the two middle numbers
            return (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2
        else:
            # If odd, the median is the middle number
            return sorted_numbers[length // 2]
        
    def print_statistics(self):
        print(f"Minimum: {self.get_min()}")
        print(f"Maximum: {self.get_max()}")
        print(f"Mean: {self.get_mean()}")
        print(f"Median: {self.get_median()}")