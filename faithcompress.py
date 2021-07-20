size = 100000000


def write_to_file(file_name, data):
    with open(file_name, 'wb') as out_file:
        out_file.write(str(data).encode('utf8'))


def read_from_file(file_name):
    data = None
    with open(file_name, 'rb') as in_file:
        data = in_file.read()
    return data.decode('utf8')


def f(x):
    return (2 * x + 5) % 37


def compress(a):
    return list(a)[1]


def uncompress(a):
    current = int(a)
    res = [current]
    for _ in range(size):
        current = f(current)
        res.append(current)
    return res


def generate_file(file_length):
    current = 1
    for _ in range(file_length):
        yield current
        current = f(current)


a = list(generate_file(size))


write_to_file('movie.mpeg.txt', a)


b = compress(a)


write_to_file('movie.mpeg.faith.txt', b)
