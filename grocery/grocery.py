dict = {}
while True:
    try:
        item = input().strip().upper()
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] += 1

    except EOFError:
        print("\n")
        break

for item in sorted(dict):
    print(dict[item], item)
