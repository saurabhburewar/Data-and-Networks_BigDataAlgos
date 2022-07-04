import os
from zipfile import ZipFile


directory = 'graphs'
vis1 = [0] * 1000
vis2 = [0] * 1000
adjlist1 = {}
adjlist2 = {}
queries = 0


def dfs1(x):
    global queries
    queries += 1
    vis1[x] = True
    if x not in adjlist1:
        adjlist1[x] = {}

    for i in adjlist1[x]:
        if not vis1[i]:
            dfs1(i)


def dfs2(x):
    global queries
    queries += 1
    vis2[x] = True
    if x not in adjlist2:
        adjlist2[x] = {}

    for i in adjlist2[x]:
        if not vis2[i]:
            dfs2(i)


def checkConnectivity():

    n = len(adjlist1)
    global vis1
    global vis2

    vis1 = [False] * n
    dfs1(1)
    vis2 = [False] * n
    dfs2(1)

    for i in range(1, n + 1):
        if (not vis1[i] and not vis2[i]):
            return False

    return True


def main():
    if not os.path.exists(directory + '.zip'):
        print('ERROR: Cannot find the graphs. Please check if "graphs.zip" exists in the same directory.')
        return

    with ZipFile(directory + '.zip', 'r') as zip:
        zip.extractall()

    for file in os.listdir(directory):
        filename = os.path.join(directory, file)

        global queries
        global adjlist1
        global adjlist2
        queries = 0

        f = open(filename, 'r')
        for row in f:
            if '#' in row:
                continue
            else:
                row = row.strip().split(" ")
                values = [int(i) for i in row[1:]]
                adjlist1[int(row[0])] = values
                for node in row[1:]:
                    if node not in adjlist2:
                        adjlist2[int(node)] = []

                    adjlist2[int(node)].append(int(row[0]))

                for i in range(100):
                    if i not in adjlist2:
                        adjlist2[i] = []

        adjlist1 = dict(sorted(adjlist1.items(), key=lambda x: x[0]))
        adjlist2 = dict(sorted(adjlist2.items(), key=lambda x: x[0]))

        if checkConnectivity():
            print(filename, "- Connected, Queries - ", queries)
        else:
            print(filename, "- Not Connected, Queries - ", queries)

        f.close()


if __name__ == "__main__":
    main()
