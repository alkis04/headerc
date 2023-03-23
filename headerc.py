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
    if re.search(r"\w+\s+\w+\s*\(", line): 
        return True
    if(re.search(r"\w+\s+\*\w+\s*\(", line)):
        return True
    if(re.search(r"\w+\s+\*\*\w+\s*\(", line)):
        return True
    if(re.search(r"\w+\s+\*\*\*\w+\s*\(", line)):
        return True
    if(re.search(r"\w+\s+\*\*\*\*\w+\s*\(", line)):
        return True
    if(re.search(r"\w+\s+long\s+long\s+\w+\s*\(", line)):
        return True
    if(re.search(r"\w+\s+long\s+long\s+\*\w+\s*\(", line)):
        return True
    if(re.search(r"\w+\s+long\s+long\s+\*\*\w+\s*\(", line)):
        return True
    if(re.search(r"\w+\s+long\s+long\s+\*\*\*\w+\s*\(", line)):
        return True
    if(re.search(r"\w+\s+long\s+long\s+\*\*\*\*\w+\s*\(", line)):
        return True
    return False

def extract_function_name(line):
    return line.split("(")[0].split()[-1]

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
    if filename[-2:] != ".c":
        print("usage: headerc filename.c -args")
        sys.exit(1)
    if(not os.path.exists(filename)):
        print("file", filename, "doesnt exist")
        sys.exit(1)
    if "-o" in sys.argv:
        header = sys.argv[sys.argv.index("-o") + 1]
    else:
        header = filename[:-2] + ".h"
    if len(sys.argv) == 2:
        update_header(header, filename)

    elif "-r" in sys.argv:
        rewrite_header(header, filename)
    elif "-u" in sys.argv:
        update_header(header, filename)
    else:
        print("unkown arguments")

if __name__ == "__main__":
    main()
