import time
from tqdm import tqdm


start = time.time()

items = []
t = 0
with open("numbers", 'r') as f:
    for row in tqdm(f):
        actual_value = int(row.strip())
        if actual_value in items:
            continue
        else:
            items.append(actual_value)
            t += 1

print("Distinct elements: ", t)
print("Time taken: ", time.time() - start)
