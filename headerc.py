#!/usr/bin/env python3

# how to chmod in order to make it savalbe again in the terminal
# chmod +x headerc.py

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
            print("usage: headerc.py filename.c")
            sys.exit(1)
        if(not os.path.exists(filename)):
            print("file", filename, "doesnt exist")
        else:
            with open(filename, "r") as f:
                lines = f.readlines()
                header = filename[:-2] + ".h"
                oper = "w"
                if(os.path.exists(header)):
                    print("file exists")
                    print("do you want to overwrite or append it or create a new one? (o/a/c)")
                    answer = input()
                    if(answer == "c"):
                        print("enter a new file name (without .h extension): ")
                        header = input()
                        header += ".h"
                        if(header == ""):
                            print("You didn't enter a file name")
                            print("aborting")
                            sys.exit(1)
                        
                    elif(answer == "o"):
                        print("overwriting file: " + header)
                    elif(answer == "a"):
                        oper = "a"
                
                with open(header, oper) as h:
                    for line in lines:
                        if re.search(r"\w+\s+\w+\s*\(", line): 
                            h.write(line.replace("{", ";"))
                        if(re.search(r"\w+\s+\*\w+\s*\(", line)):
                            h.write(line.replace("{", ";"))
                        if(re.search(r"\w+\s+\*\*\w+\s*\(", line)):
                            h.write(line.replace("{", ";"))
                        if(re.search(r"\w+\s+\*\*\*\w+\s*\(", line)):
                            h.write(line.replace("{", ";"))
                        if(re.search(r"\w+\s+\*\*\*\*\w+\s*\(", line)):
                            h.write(line.replace("{", ";"))

if __name__ == "__main__":
    main()
