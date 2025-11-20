def load_data(filename):
    try:
        f = open(filename, "r")
    except:
        return []

    lines = f.read().splitlines()
    f.close()

    data = []
    for line in lines:
        if line.strip() == "":
            continue
        data.append(line.split("|"))
    return data

def save_data(filename, data):
    f = open(filename, "w")
    for row in data:
        f.write("|".join(row) + "\n")
    f.close()