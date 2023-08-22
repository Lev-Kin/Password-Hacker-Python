try:
    a = float(input())
    b = float(input())

    result = a / b

    print(result)
except ZeroDivisionError:
    print("The Error!")