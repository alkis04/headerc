#!/usr/bin/env python3

# q: where I should put an executable in linux so that it can be run from anywhere?
# a: /usr/local/bin

# python program that takes as an argument a .c file then finds all the functions in the file and creates a header file with the prototypes of the functions
# the header file will be named the same as the .c file but with a .h extension
# it should also change the last "{" to a ";"
# the propgram should be able to recognize int, float, char, void and string functions and even functions that return a pointer
# and double pointers

import sys
import re

def main():
    if len(sys.argv) != 2:
        print("usage: headerc filename.c")
        sys.exit(1)
    else:
        filename = sys.argv[1]
        if filename[-2:] != ".c":
            print("usage: python headerc.py filename.c")
            sys.exit(1)
        else:
            with open(filename, "r") as f:
                lines = f.readlines()
                header = filename[:-2] + ".h"
                with open(header, "w") as h:
                    for line in lines:
                        if re.search(r"int\s+\w+\s*\(", line):
                            h.write(line.replace("{", ";"))
                        elif re.search(r"float\s+\w+\s*\(", line):
                            h.write(line.replace("{", ";"))
                        elif re.search(r"char\s+\w+\s*\(", line):
                            h.write(line.replace("{", ";"))
                        elif re.search(r"void\s+\w+\s*\(", line):
                            h.write(line.replace("{", ";"))
                        elif re.search(r"string\s+\w+\s*\(", line):
                            h.write(line.replace("{", ";"))
                        elif re.search(r"int\s+\*\w+\s*\(", line):
                            h.write(line.replace("{", ";"))
                        elif re.search(r"float\s+\*\w+\s*\(", line):
                            h.write(line.replace("{", ";"))
                        elif re.search(r"char\s+\*\w+\s*\(", line):
                            h.write(line.replace("{", ";"))
                        elif re.search(r"string\s+\*\w+\s*\(", line):
                            h.write(line.replace("{", ";"))
                        elif re.search(r"int\s+\*\*\w+\s*\(", line):
                            h.write(line.replace("{", ";"))
                        elif re.search(r"float\s+\*\*\w+\s*\(", line):
                            h.write(line.replace("{", ";"))
                        elif re.search(r"char\s+\*\*\w+\s*\(", line):
                            h.write(line.replace("{", ";"))
                        elif re.search(r"string\s+\*\*\w+\s*\(", line):
                            h.write(line.replace("{", ";"))

# q: how can I do this with every possible type of function?
# a: use regex
# q: how can I use regex?
# a: use re.search() and re.match() and re.findall()
# q: what is the difference between re.search() and re.match()?
# a: re.search() searches for a match anywhere in the string
#    re.match() only matches if the string is at the beginning of the line
# q: what is the difference between re.findall() and re.search()?
# a: re.findall() returns a list of all the matches
#    re.search() returns the first match
# q: how can I use regex to find a function?
# a: use re.search(r"int\s+\w+\s*\(", line)
# q: what does r"int\s+\w+\s*\(" mean?
# a: r means raw string
#    int means the function returns an int
#    \s+ means one or more spaces
#    \w+ means one or more alphanumeric characters
#    \s* means zero or more spaces
#    \( means the function starts with a (
# how can I write the generic type of function in re.search()?
# a: use \w+ instead of int, float, char, void, string, int*, float*, char*, string*, int**, float**, char**, string**

if __name__ == "__main__":
    main()
