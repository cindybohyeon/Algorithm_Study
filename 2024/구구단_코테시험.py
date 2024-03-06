for i in range(1, 10):
    if i % 4 == 0:
        continue
    for j in range(1, 5):
        print(f"{j + 1} * {i} = {i * (j + 1)}", end="\t")
    print()

print()
for i in range(1, 10):
    if i % 4 == 0:
        continue
    for j in range(5, 9):
        if i % 4 == 0:
            continue
        print(f"{j + 1} * {i} = {i * (j + 1)}", end="\t")
    print()
