import math


def logarithmic_value(x, base):
    if base < 0 or base == 0 or base == 1:
        return round(math.log(x), 2)
    else:
        return round(math.log(x) / math.log(base), 2)


if __name__ == "__main__":
    x = int(input())
    base = int(input())

    print(logarithmic_value(x, base))
