from input_data import input_data
from write_data import write_data


def push_data():
    dct = input_data()
    write_data([dct.get("id"), dct.get("surname"), dct.get("name"), dct.get("class")], "name.csv")
    write_data([dct["id"], dct["city"], dct["street"], dct["house"], dct["apartment"], dct["other"]], "address.csv")
    write_data([dct["id"], dct["row"], dct["col"]], "class.csv")
