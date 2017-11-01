funcmap = {
    '>': lambda out_file: out_file.write('ptr++;\n'),
    '<': lambda out_file: out_file.write('ptr--;\n'),
    '+': lambda out_file: out_file.write('array[ptr]++;\n'),
    '-': lambda out_file: out_file.write('array[ptr]--;\n'),
    '.': lambda out_file: out_file.write('putchar(array[ptr]);\n'),
    ',': lambda out_file: out_file.write('getchar(array[ptr]);\n'),
    '[': lambda out_file: out_file.write('while (array[ptr]) {\n\t'),
    ']': lambda out_file: out_file.write('}'),
}

def parse_bf(symbol, out_file):
    if symbol in funcmap:
        funcmap[symbol](out_file)
