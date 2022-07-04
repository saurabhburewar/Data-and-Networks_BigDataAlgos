import random as rnd
from tqdm import tqdm


with open("numbers", 'w') as f:
    no_of_element = rnd.randint(900000000, 1000000000)
    for i in tqdm(range(no_of_element)):
        r = rnd.randint(1000, 10000)
        f.write("{0}\n".format(rnd.randint(1, r)))


# with open("numbers_short", 'w') as f:
#     no_of_element = rnd.randint(90000, 100000)
#     for i in tqdm(range(no_of_element)):
#         r = rnd.randint(1000, 10000)
#         f.write("{0}\n".format(rnd.randint(1, r)))
