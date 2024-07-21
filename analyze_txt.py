import numpy as np

with open("res_o2_subject1.txt", "r") as f:
    data = f.read().strip()

data = [(line.split(":")[0], line.split(":")[1].split(" ->")[0], line.split(": ")[1].split(
    " |")[0], line.split(": ")[2]) for line in data.split("\n")]

data = [[int(s), int(e), int(k), float(a)] for s, e, k, a in data]

data = np.array(data)

i = data.argmax(axis=0)[3]

print(
    f"Start: {data[i, 0]} | End: {data[i, 1]} | K: {data[i, 2]} | Acc: {data[i, 3]}")
