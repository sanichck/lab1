# TODO Найдите количество книг, которое можно разместить на дискете

disk = float(1.44)
page = 100
str = 50
symv = 25
weight = 4
mb = 1024
disk_byte = disk * mb * mb
byteinbook = symv * str * page * weight
booksalot = int(disk_byte / byteinbook)
print("Количество книг, помещающихся на дискету:", booksalot)

