                        if re.search(r"\w+\s+\w+\s*\(", line): 
                            s = line.replace("{", ";")
                            if not s in lines_set:
                                h.write(s)
                        if(re.search(r"\w+\s+\*\w+\s*\(", line)):
                            s = line.replace("{", ";")
                            if not s in lines_set:
                                h.write(s)
                        if(re.search(r"\w+\s+\*\*\w+\s*\(", line)):
                            s = line.replace("{", ";")
                            if not s in lines_set:
                                h.write(s)
                        if(re.search(r"\w+\s+\*\*\*\w+\s*\(", line)):
                            s = line.replace("{", ";")
                            if not s in lines_set:
                                h.write(s)
                        if(re.search(r"\w+\s+\*\*\*\*\w+\s*\(", line)):
                            s = line.replace("{", ";")
                            if not s in lines_set:
                                h.write(s)


                                if(os.path.exists(header)):
            print("file exists")
            print("do you want to overwrite or append it or create a new one? (o/a/c/u)")
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
            elif(answer == "a" or answer == "u"):
                oper = "a