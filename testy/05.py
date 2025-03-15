file = open("test.txt", "r")
file.close()
content = file.read()  # ValueError: pokus o čítanie zatvoreného súboru
