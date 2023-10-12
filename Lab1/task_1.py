numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_numbers = sum(numbers[:4] + numbers[5:])
count_numbers = len(numbers)
numbers[4] = sum_numbers / count_numbers
print("Измененный список:", numbers)
