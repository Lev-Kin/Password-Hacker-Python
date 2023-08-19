for i in range(1, 11):
    filename = f'file{i}.txt'
    with open(filename, 'w') as f:
        f.write(str(i))
