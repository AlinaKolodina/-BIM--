# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
strings = 50
symb = 25
disk_1_symb = 4
disk = 1.44
disk_bytes = disk * 1024 ** 2

count = round(disk_bytes / (pages * strings * symb * disk_1_symb))
store_mb = 1024*1024*disk
print("Количество книг, помещающихся на дискету:", count)
