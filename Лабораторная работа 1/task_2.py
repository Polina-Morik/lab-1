# TODO Найдите количество книг, которое можно разместить на дискете
volume_disk = 1.44  # мбайта
count_page = 100
count_str_on_page = 50
count_symv = 25
one_symv = 4  # байта

volume_disk_b = 1.44 * 1024 * 1024  # размер диска в байтах
symv_in_one_book = count_symv * count_str_on_page * count_page  # количество символов в 1 книге
volume_one_book = one_symv * symv_in_one_book  # объем одной книги в байтах
result = round(volume_disk_b / volume_one_book)

print("Количество книг, помещающихся на дискету:", result)
