n = input().upper()
word = list()
c = 0
list_p1 = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"]
list_p2 = ["D", "G", "Д", "К", "Л", "М", "П", "У"]
list_p3 = ["B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"]
list_p4 = ["F", "H", "V", "W", "Y", "Й", "Ы"]
list_p5 = ["K", "Ж", "З", "Х", "Ц", "Ч"]
list_p8 = ["J", "X", "Ш", "Э", "Ю"]
list_p10 = ["Q", "Z", "Ф", "Щ", "Ъ"]
for i in n:
    word.append(i)
for i in word:
    if i in list_p1:
        c = c + 1
    elif i in list_p2:
        c = c + 2
    elif i in list_p3:
        c = c + 3
    elif i in list_p4:
        c = c + 4
    elif i in list_p5:
        c = c + 5
    elif i in list_p8:
        c = c + 8
    elif i in list_p10:
        c = c + 10
print(c)
