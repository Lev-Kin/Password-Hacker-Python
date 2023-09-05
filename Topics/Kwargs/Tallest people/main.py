def tallest_people(**kwargs):
    people = {}

    for name, height in kwargs.items():
        people[name] = height

    max_height = max(people.values())

    tallest_names = [name for name, height in people.items() if height == max_height]

    tallest_names.sort()

    for name in tallest_names:
        print(f"{name} : {max_height}")


