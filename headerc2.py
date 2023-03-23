#!/usr/bin/env python3


# python program that takes as an argument a .c file then finds all the functions in the file and creates a header file with the prototypes of the functions
# the header file will be named the same as the .c file but with a .h extension
# it should also change the last "{" to a ";"
# the propgram should be able to recognize int, float, char, void and string functions and even functions that return a pointer
# and double pointers

import sys
import re
import os

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
                # checking  if file exists and ask if you want to overwrite it
                # if file exists and user doesn't want to overwrite it, offer to use a different name

                # q: how can I check if a file exists?
                # a: use os.path.exists()
                # q: can I do that with sys?
                # a: yes, use sys.path.exists()
                #
                if(os.path.exists(header)):
                    print("file exists")
                    print("do you want to overwrite it? (y/n)")
                    answer = input()
                    if(answer == "n"):
                        print("enter a new file name (without .h extension): ")
                        header = input()
                        if(header == ""):
                            print("You didn't enter a file name")
                            print("aborting")
                            sys.exit(1)
                        header += ".h"
                    else:
                        print("overwriting file: " + header)

                with open(header, "w") as h:
                    for line in lines:
                        if re.search(r"\w+\s+\w+\s*\(", line): #q: what doew r mean? a: raw string q: what is a raw string? a: a string that doesn't interpret escape characters
                            h.write(line.replace("{", ";"))
                        if(re.search(r"\w+\s+\*\w+\s*\(", line)):
                            h.write(line.replace("{", ";"))
                        if(re.search(r"\w+\s+\*\*\w+\s*\(", line)):
                            h.write(line.replace("{", ";"))
                        if(re.search(r"\w+\s+\*\*\*\w+\s*\(", line)):
                            h.write(line.replace("{", ";"))
                        if(re.search(r"\w+\s+\*\*\*\*\w+\s*\(", line)):
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
# q: what does \w+ mean?
# a: \w+ means one or more alphanumeric characters

if __name__ == "__main__":
    main()
