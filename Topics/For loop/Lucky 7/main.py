def lucky_7():

    num_of_inputs = int(input())

    for i in range(num_of_inputs):
        input_number = int(input())

        if input_number % 7 == 0:
            print(input_number ** 2)


if __name__ == "__main__":
    lucky_7()
