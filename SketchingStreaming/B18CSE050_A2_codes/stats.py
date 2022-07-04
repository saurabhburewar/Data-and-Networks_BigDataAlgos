from tqdm import tqdm


items = {}
n = 0
t = 0
with open("numbers", 'r') as f:
    for row in tqdm(f):
        n += 1
        actual_value = int(row.strip())
        if actual_value in items:
            items[actual_value] += 1
        else:
            items[actual_value] = 1
            t += 1


print("Frequency of integers: ", items)
print("Total integers: ", n)
print("Unique integers: ", t)
