different_types = [(-1 + 0j), 1, 1.2, True, None, 'string', [0, 8], (2, 3), {'one': 1, 'two': 2}, {1, 2, 3},
                   frozenset(), range(1, 10), b'four', bytearray(b'twenty'), TypeError]

for i, item in enumerate(different_types, 1):
    print(f'{i} - {item}:type -> {type(item)}')
