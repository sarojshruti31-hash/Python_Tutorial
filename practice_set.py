data = True
with open("practice.txt", "r") as f:
    while data:
        data = f.readline()
        if ("Python" in data):
            print("Word found")
            break
        print(data)