import random

def generate_unique_random_numbers(num_numbers, min_range, max_range):
    if max_range - min_range < num_numbers:
        raise ValueError("Range is smaller than the number of unique numbers requested")

    numbers = set()
    while len(numbers) < num_numbers:
        numbers.add(random.randint(min_range, max_range))

    return list(numbers)

if __name__ == "__main__":
    num_numbers = 600
    min_range = 1
    max_range = 9380

    unique_numbers = generate_unique_random_numbers(num_numbers, min_range, max_range)
    print(unique_numbers)


