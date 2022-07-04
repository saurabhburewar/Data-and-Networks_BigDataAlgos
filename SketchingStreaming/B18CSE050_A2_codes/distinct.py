from tqdm import tqdm


class Distinct():
    def __init__(self):
        self.X = 0

    def fit(self, value):
        val = bin((1*value + 6) % 32)[2:]
        sum = 0

        for j in range(len(val)-1, 0, -1):
            if val[j] == '0':
                sum += 1
            else:
                break

        if sum > self.X:
            self.X = sum

    def est(self):
        return 2**self.X

    def counterValue(self):
        return self.X


model = Distinct()
t = 10000

with open("numbers", 'r') as f:
    for row in tqdm(f):
        actual_value = int(row.strip())
        model.fit(actual_value)

print("\nActual count: ", t, "\nApproximate count: ",
      model.est(), "\nCounter value: ", model.counterValue())
