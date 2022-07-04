import numpy as np
from tqdm import tqdm


class CountminSketch():
    def __init__(self, t, k):
        self.t = t
        self.k = k
        self.S = np.zeros((t, k))

    def update(self, value):
        for i in range(self.t):
            self.S[i][(hash(i + value) % self.k)
                      ] = self.S[i][(hash(i + value) % self.k)] + 1

    def est(self, entry):
        flist = [self.S[i][(hash(i + entry) % k)] for i in range(t)]
        return min(flist)


k = 5
t = 20
sketch = CountminSketch(t, k)
countlist = {}

with open("numbers", 'r') as f:
    for row in tqdm(f):
        actual_value = int(row.strip())
        if actual_value not in countlist:
            countlist[actual_value] = 0
        if len(countlist) == 15:
            break


with open("numbers", 'r') as f:
    for row in tqdm(f):
        actual_value = int(row.strip())
        if actual_value in countlist:
            sketch.update(actual_value)


for entry in countlist:
    countlist[entry] = sketch.est(entry)

print(countlist)
