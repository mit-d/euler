def Score(name):
    score = 0
    for letter in name:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        score = score + 1 + alphabet.find(letter)
    return score


if __name__ == "__main__":
    names = []

    for line in open("022.in"):
        for i in line.split(","):
            names.append(i.strip('"'))
    names.sort()

    tot = 0
    for i in range(len(names)):
        tot = tot + (i + 1) * Score(names[i])
    print(tot)
