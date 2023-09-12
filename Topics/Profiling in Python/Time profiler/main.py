from time import time


def catalan(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n - i - 1)
    return res


# start the timer
start = time()

for i in range(16):
    catalan(i)

# end the timer
end = time()

# save the message
message = f"It took {end - start} seconds."
