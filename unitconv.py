import json

def unit_selector(unidad, data):
    for key in data.keys():
        if key == unidad:
            val = data[key]
            break
    return val


def open_json(parameter):
    address = '.\\data\\unit.json'
    with open(address, 'r') as fp:
        data = json.load(fp)
    return data[parameter]


def conversion(value, unit, unit_to_converter, parameter,decimal):
    data = open_json(parameter)
    a = unit_selector(unit_to_converter, data)
    b = unit_selector(unit, data)
    converted_value = round(value*a/b,decimal)
    return converted_value


""" if __name__ == '__main__':
    conversion(4, "m", "m", "leng",2) """

