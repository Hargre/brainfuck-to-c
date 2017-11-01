def parse_bf(symbol, out_file):
    if symbol == '>':
        out_file.write('ptr++;\n')
    elif symbol == '<':
        out_file.write('ptr--;\n')
    elif symbol == '+':
        out_file.write('array[ptr]++;\n')
    elif symbol == '-':
        out_file.write('array[ptr]--;\n')
    elif symbol == '.':
        out_file.write('putchar(array[ptr]);\n')
    elif symbol == ',':
        out_file.write('getchar(array[ptr]);\n')
    elif symbol == '[':
        out_file.write('while (array[ptr]) {\n\t')
    elif symbol == ']':
        out_file.write('}')
    else:
        raise ValueError("Invalid character!")