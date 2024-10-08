numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index_of_none = 4

new_numbers = [2, -93, -2, 8, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
new_number = sum(new_numbers) / len(numbers)
numbers[index_of_none] = new_number

print("Измененный список:", numbers)