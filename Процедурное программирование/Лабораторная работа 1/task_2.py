size_of_diskette = 1.44

count_pages = 100
count_of_lines = 50
count_of_chars = 25
size_of_single_char = 4
size_of_single_char = (size_of_single_char / 1024) / 1024
size_of_one_book = size_of_single_char * count_of_chars * count_of_lines * count_pages

print("Количество книг, помещающихся на дискету:", int(size_of_diskette / size_of_one_book))