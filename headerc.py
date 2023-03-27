#!/usr/bin/env python3

import sys
import re
import os

def line_to_prototype(line):
    if "{" in line:
        line = line[:line.index("{")] + ";"
    else:
        line += ";"
    return line + '\n'
def line_is_function(line):
    if re.search(r"\w+\s+(\*{6,12})\s*\w+\s*\(", line):
        print("You may want to talk to your doctor about your excessive use of pointers")
        sys.exit(1)
    bad_patterns = [r"if\s*\(", r"else\s*\(", r"while\s*\(", r"for\s*\(", r"switch\s*\(", r"case\s*\(", r"return\s*\(", r"main\s*\("]
    good_patterns = [r"\w+\s*(\*{1,5})\s*\w+\s*\(", r"long\s+long\s*(\*{1,5})\s*\w+\s*\(", r"\w+\s+\w+\s*\(", r"long\s+long\s+\w+\s*\(" ]  
    for pattern in bad_patterns:
        if re.search(pattern, line):
            return False
    for pattern in good_patterns:
        if re.search(pattern, line):
            return True
    
    return False

def extract_function_name(prototype_string):
    name = re.search(r'\w+(?=\()', prototype_string).group()
    print(name)
    return name
def update_header(header, filename):
    fun_set = set()
    h_lines = []
    with open(header, "r") as h:
        lines = h.readlines()
        for line in lines:
            h_lines.append(line)
            if line_is_function(line):
                fun_set.add(extract_function_name(line))
    fun_map = {}
    with open(filename, "r") as f:
        f_lines = f.readlines()
        for line in f_lines:
            if line_is_function(line):
                fun_map[extract_function_name(line)] = line_to_prototype(line)

    with open(header, "w") as h:
        for line in h_lines:
            if line_is_function(line):
                if extract_function_name(line) in fun_map:
                    h.write(fun_map[extract_function_name(line)])
                    fun_set.add(extract_function_name(line))
            else:
                h.write(line)
        for line in f_lines:
            if line_is_function(line):
                if extract_function_name(line) not in fun_set:
                    h.write(line_to_prototype(line))

def rewrite_header(header, filename):
    with open(header, "w") as h:
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line_is_function(line):
                    h.write(line_to_prototype(line))


def main():
    if len(sys.argv) < 2:
        print("usage: headerc filename.c -args")
        sys.exit(1)
    filename = sys.argv[1]
    sys.argv.remove(sys.argv[0])
    if filename[-2:] != ".c":
        print("usage: headerc filename.c -args")
        sys.exit(1)
    if(not os.path.exists(filename)):
        print("file", filename, "doesnt exist")
        sys.exit(1)
    if "-o" in sys.argv:
        header = sys.argv[sys.argv.index("-o") + 1]
        sys.argv.remove("-o")
        sys.argv.remove(header)
    else:
        header = filename[:-2] + ".h"
    for arg in sys.argv:
        if arg != "-r" and arg != "-u" and arg != filename:
            print("error: invalid argument", arg)
            sys.exit(1)
    if "-r" in sys.argv and "-u" in sys.argv:
        print("error: -r and -u are mutually exclusive")
        sys.exit(1)
    if(not os.path.exists(header) or "-r" in sys.argv):
        rewrite_header(header, filename)
    else:
        update_header(header, filename)


if __name__ == "__main__":
    main()
