import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


class Morris():
    def __init__(self):
        self.x = 0

    def inc(self):
        # d = 1 / ((2**(self.x+1) - 1) - (2**(self.x) - 1))
        # r = np.random.uniform(0, 1)
        d = 2**(-self.x)
        r = np.random.rand()

        if r < d:
            self.x += 1

        return self.x

    def est(self):
        return 2**(self.x) - 1

    def counterValue(self):
        return self.x


class Morrisplus():
    def __init__(self, num=2):
        self.x = [Morris()] * num
        self.num = num

    def inc(self):
        for model in self.x:
            model.inc()

    def est(self):
        val = 0
        for model in self.x:
            val += model.est()

        return val/self.num

    def counterValue(self):
        return self.x[0].counterValue()


# items = []
counter = Morrisplus()
n = 0
with open("numbers", 'r') as f:
    for row in tqdm(f):
        n += 1
        counter.inc()
        # items.append((n, counter.est()))

X = counter.counterValue()

print("\nActual count: ", n, "\nApproximate count: ",
      counter.est(), "\nCounter value: ", X)

# plt.plot([x[0] for x in items], label="n")
# plt.plot([x[1] for x in items], label="v")
# plt.xlabel('')
# plt.ylabel('Count')
# plt.legend()
# plt.savefig("Q2_2.png")
