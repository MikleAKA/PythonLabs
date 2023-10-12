# TODO Найдите количество книг, которое можно разместить на дискете
disk_free_size = 1.44 * 1024 * 1024
pages_of_book = 100
strings_of_page = 50
chars_of_string = 25
bites_of_char = 4
bites_of_book = pages_of_book * strings_of_page * chars_of_string * bites_of_char
books = disk_free_size // bites_of_book
print("Количество книг, помещающихся на дискету:", int(books))
