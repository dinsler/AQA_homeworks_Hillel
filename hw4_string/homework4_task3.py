"""
    Task3.there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
    Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: quro}
"""
data_amanda = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
if __name__ == '__main__':
    result_dict = {}
    for pair in data_amanda.split("&"):
        pair = pair.strip()
        if not pair:
            continue
        key, value = pair.split("=", 1)
        if "=" in value:
            index_of_eq = value.index("=")
            value = value.replace(value[index_of_eq:], "")
        result_dict[key] = value
    print(result_dict)
