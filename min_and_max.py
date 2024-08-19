def calculate_statistics(numbers):
    if not numbers:
        return None

    max_number = max(numbers)
    min_number = min(numbers)
    sum_numbers = sum(numbers)
    average_number = sum_numbers / len(numbers)

    return {
        'max': max_number,
        'min': min_number,
        'sum': sum_numbers,
        'average': average_number
    }

numbers = [1, 2, 3, 4, 5]
statistics = calculate_statistics(numbers)
print(statistics)