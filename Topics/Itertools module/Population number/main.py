count = 0

for country in countries:
    if country["population_mil"] > 100:
        count += 1

print(count)
