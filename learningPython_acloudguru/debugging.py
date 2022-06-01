def mapper(func, values):
    output_values = []
    index = 0
    while index < len(values):
        breakpoint()
        output_values.append(func(values[index]))
        index += 1
    return output_values


def add_one(val):
    return val+1


print(mapper(add_one, list(range(10))))

