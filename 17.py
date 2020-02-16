Term = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}
Tens = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}


def English(a):
    n = len(str(a))
    if str(a) == "1000":
        return "one thousand"
    if n == 1:
        return Term[a]
    if n == 2:
        if a[0] == "0":  # ends in '0#'
            return English(a[1])
        if int(a[0]) < 2:
            return Term[a]
        else:
            x = "-" + English(a[1]) if English(a[1]) != "zero" else ""
            return Tens[a[0]] + x
        pass
    if n == 3:
        x = "and " + English(a[1:]) if English(a[1:]) != "zero" else ""
        return English(a[0]) + " hundred " + x
        pass


if __name__ == "__main__":
    sz = 0
    for i in range(1, 1001):
        sz += len(English(str(i)).replace(" ", "").replace("-", ""))
    print(sz)
