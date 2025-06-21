def generate_numbers(a, b):
    for n in range(a, b + 1):
        yield n + n - a + 1


for number in generate_numbers(3, 6):
    print(number)
