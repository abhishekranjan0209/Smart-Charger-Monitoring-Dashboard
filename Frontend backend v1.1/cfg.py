dbc_file = None
bit_rate = None
project = None
bus_type = None

def new_print(value1, value2, value3, value4):
    global dbc_file
    dbc_file = value1
    print(value1)
    global bit_rate
    bit_rate = value2
    print(value2)
    global project
    project = value3
    print(value3)
    global bus_type
    bus_type = value4
    print(value4)