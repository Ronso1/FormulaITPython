numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index = 4

sum_numbers = sum(numbers[:index]) + sum(numbers[index + 1:])
cnt_numbers = len(numbers)
average_of_numbers = sum_numbers / cnt_numbers

numbers[index] = average_of_numbers
print("Измененный список:", numbers)