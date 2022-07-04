import time
from tqdm import tqdm
import random


class FM():
    def __init__(self):
        self.minhash = 1
        self.salt = 17

    def naivehash(self, e):
        return random.Random(e+self.salt).random()

    def add(self, e):
        self.minhash = min(self.minhash, self.naivehash(e))

    def est(self):
        return 1/self.minhash

    def counterValue(self):
        return self.minhash


start = time.time()

# items = []
fm = FM()
t = 0
t = 10000
with open("numbers", 'r') as f:
    for row in tqdm(f):
        actual_value = int(row.strip())
        # if actual_value in items:
        #     continue
        # else:
        #     items.append(actual_value)
        #     t += 1

        fm.add(actual_value)

print("\nActual count: ", t, "\nApproximate count: ",
      round(fm.est()), "\nCounter value: ", fm.counterValue())
