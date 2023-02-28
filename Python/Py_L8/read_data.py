def read_data():
    lst_name = []
    with open('name.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_name.append(temp)
        print(lst_name)
    lst_address = []
    with open('address.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_address.append(temp)
        print(lst_address)

    lst_class = []
    with open('class.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_class.append(temp)
        print(lst_class)

    lst = []
    for i in range(len(lst_name)):
        lst.append([lst_name[i][0], lst_name[i][1], lst_name[i][2], lst_name[i][3],
                    lst_class[i][1], lst_class[i][2],
                    lst_address[i][1], lst_address[i][2], lst_address[i][3], lst_address[i][4], lst_address[i][5]])
    return lst
