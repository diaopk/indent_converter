#!/usr/bin/env python
# Define some functions used by indent_convertor.py

def get_arg(args):
    """ This function returns 5 arguments

        They have default values in case of missing input arguments
    """
    obj = None
    indent = 4
    target = 2
    start = 0
    end = 0

    if len(args) > 1 and len(args) <= 6:
        try:
            obj = args[1]
        except:
            print "- Forgot to input a text file"
            print_program_info()
            exit()
        else:
            try:
                f = open(obj, "r")
            except:
                print "- Enter a correct path to that text file"
                exit()
            else:
                content = f.readlines()
                name = f.name
                script = "python" if name[-3:] == ".py" else None

                # Initlise a end again
                end = len(content)

                # Close the text file
                f.close()
                
                if script == "python":
                    if len(args[2:]) == 2: # make sure 2 arguments entered
                        for arg in args[2:]:
                            last_char = arg[-1]
                            if arg.startswith("--start="):
                                start = int(last_char)-1
                            elif arg.startswith("--end="):
                                end = int(last_char)-1
                            else:
                                print_program_info(script="python")
                                exit()

                else: 
                    for arg in args[2:]:
                        last_char = arg[-1]
                    
                        if last_char.isdigit:
                            if arg.startswith("--start="):
                                start = int(last_char)-1
                            elif arg.startswith("--end="):
                                end = int(last_char)-1
                            elif arg.startswith("--indent="):
                                indent = int(last_char)
                            elif arg.startswith("--target="):
                                target = int(last_char)
                            else:
                                print_program_info()
                                exit()

                        else:
                            print_program_info()
                            exit()

                print "indent: " + str(indent)
                print "target: " + str(target)
                print "start: " + str(start)
                print "end: " + str(end)
                print "filename: " + name[:-3]
                print "extension: " + name[-3:]
                # Finally Return args
                return script, name, content, indent, target, start, end
    else:
        exit()

# Method to print out program info
def print_program_info(script=None):
    """ This function prints out program info for uses. """
    
    if script is None:
        print 'This program takes at least one text file as an argument to process the program'
        print '- Accepted syntaxs:(note that the order of args entered does not mater)'
        print '- ./indent_converter source_file --start/end=num'
        print '-                              --indent=num1 --target=num2'
        print '-                              --start=line1 --end=line2'
        print '-                              --indent=num1 --target=num2 --start/end=line'
        print '-                              --indent=num1 --target=num2 --start=line1 --end=line2'
    elif script == "python":
        print "The program got python script but not acceptable arguments"
        print "- Acceptable arguments:"
        print "- ./indent_converter.py python_scirpt.py --start=line1 --end=line2"
        print "-                                        --end=line1 --start=line2"

# Method to return Boolean value to indicate the condition if a passed
# line startswith a specific number of indents and if the string behind
# the specific number of indents is equlvaent to the raw string
def subconverter(line, original_indent, raw):
    if line.startswith(original_indent) and line[len(original_indent):] == raw:
        return True
    else:
        return False

# Method to convert each line passed to this program into new line if 
# requirement is met
def converter(line, int_indent, int_target_indent, case_indent=None):
    """ This function parses the passed line and converts it 

        Depend upon what in_indent, int_target_indent and case_indent are,
        this function is going to convert the passed line and return it
    """

    if case_indent != None and py is False:
        # Convert them into whitespaces
        indent = ' ' * int_indent
        target_indent = ' ' * int_target_indent
        line = str(line)
        raw_string = line.lstrip()

        if subconverter(line, indent, raw_string): # line with 8 spaces
            #print 'After the if original:'+line
            #print 'After the if raw string:'+raw_string
            return target_indent+raw_string

        elif subconverter(line, indent+case_indent, raw_string):
            #print 'indent+case_indent'
            return target_indent+case_indent+raw_string

        elif subconverter(line, indent+case_indent*2, raw_string):
            return target_indent+case_indent*3+raw_string
        
        elif subconverter(line, indent*2, raw_string):
            #print 'indent*2'
            return target_indent*2+raw_string

        elif subconverter(line, indent*2+case_indent, raw_string):
            #print 'indent*2+case_indent'
            return target_indent*2+case_indent+raw_string

        elif subconverter(line, indent*2+case_indent*2, raw_string):
            return target_indent*2+case_indent*2+raw_string

        elif subconverter(line, indent*3, raw_string):
            #print 'indent*3'
            return target_indent*3+raw_string

        elif subconverter(line, indent*3+case_indent, raw_string):
            #print 'indent*3+case_indent'
            return target_indent*3+case_indent+raw_string

        elif subconverter(line, indent*3+case_indent*2, raw_string):
            return target_indent*3+case_indent*2+raw_string

        elif subconverter(line, indent*3+case_indent*3, raw_string):
            return target_indent*3+case_indent*3+raw_string

        else: # the rest of cases
            return line
    else:
        return 'haha'

# Method to convert python script
def converter(content):
    result = ""
    tab = "    " # 4 spaces width

    for index in range(len(content)):
        # The current line
        line = content[index]

        if line[-2] == ":":
            # Convert rest of the line and return
            def _converter(index, subcontent, result, times):
                if index > len(subcontent)-1:
                    return result 
                elif subcontent[index][-2] == ":":
                    times += 1
                    return _converter(index+1, subcontent, result+times*tab+subcontent[index], times)
                else:
                    return _converter(index+1, subcontent, result+times*tab+subcontent[index], times) 

            # Add a tab for rest of the line and return
            result = _converter(index+1, content[index:], result+line, 1)
            break
        else:
            result += line
            pass
    return result

# Method to check text file type and return a new filename
def check_type(f):
    if f[-3:] == ".py":
        # python script
        extension = ".py"
        name = f[:-3]
        return name + "_copy" + extension
    elif f[-4:] == ".txt":
        # normal text file
        extension = ".txt"
        name = f[:-4]
        return name + "_copy" + extension
    else:
        return f
