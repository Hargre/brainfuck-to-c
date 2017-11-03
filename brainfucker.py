from sys import argv
import os

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

file_name, bf_source, output_command, output_file = argv

def compile(bf_source, output_file):
		in_file = open(bf_source, "r")
		out_file = open(output_file, "w")
		in_code = in_file.read()
		setup(out_file)

		for x in in_code:
			parse_bf(x, out_file)

		finish(out_file)

def setup(out_file):
		out_file.write('#include <stdio.h>\n#include<stdlib.h>\n\nint main(){\n')
		out_file.write('int array[10000];\n');
		out_file.write('int ptr=0;\n')

def parse_bf(symbol, out_file):
    if symbol in funcmap:
        funcmap[symbol](out_file)

def finish(out_file):
		out_file.write('return 0;\n}\n')



compile(bf_source, output_file)
