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
                                start = int(last_char)
                            elif arg.startswith("--end="):
                                end = int(last_char)
                            else:
                                print_program_info(script="python")
                                exit()

                else: 
                    for arg in args[2:]:
                        last_char = arg[-1]
                    
                        if last_char.isdigit:
                            if arg.startswith("--start="):
                                start = int(last_char)
                            elif arg.startswith("--end="):
                                end = int(last_char)
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
                print "filename: " + name
                print "extension: " + name[-3:]
                # Finally Return args
                return script, content, indent, target, start, end
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
        print '-                              --starfrom=line1 --endwith=line2'
        print '-                              --indent=num1 --target=num2 --starfrom/endwith=line'
        print '-                              --indent=num1 --target=num2 --startfrom=line1 --endwith=line2'
    elif script == "python":
        print "The program got python script but not acceptable arguments"
        print "- Acceptable arguments:"
        print "- ./indent_converter.py python_scirpt.py --start=num1 --end=num2"
        print "-                                        --end=num1 --start=num2"

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
    for line in content:
        if line[-1] == "\n" and line[-2] == ":":
            result += line
            print "yea"
        else:
            result += line
            pass
    return result

"""
# Method to parse the passed argument and return an Agr object if argument
# is correct otherwise return a error message
def arg_parser(arg):
    arg = str(arg) # Make arg as a string
    if arg.count('=') == 1: # check '=' exist and the number
        # Store the argument and data
        arg_name = arg[0:arg.find('=')] 
        arg_value = arg[arg.find('=')+1:]
        
        #print arg_name + ': ' + arg_value
        # check argment name if it is in the defined argment names or not
        if arg_name in arg_names:
            if arg_value.isdigit():

                # Make arg_name and arg_value formal to be then returned
                arg_name = str(arg_name[2:])
                arg_value = int(arg_value)

                # Everything get well return a dict object
                return Arg(arg_name, arg_value)
            else:
                return '- syntax error: argument value '+str(arg_value)
        else:
            return '- syntax error: argument name '+str(arg_name)
    
    elif arg.count('-') == 1: # If enter a -d-like argument
        if arg.find('-') == 0 and arg[arg.find('-')+1:].isalpha():
            arg_name = 'default'
            arg_value = arg[arg.find('-')+1:]

            # Everything get well return a dict object
            return {arg_name: arg_value}

        else:
            return '- syntax error: only accept -d'

    else:
        return '- syntax error: invaild arguement entered'

# Method that passing argument'svalue to the variable (startfrom, endwith
# , indent or target) on indent_convertor.py if var is the same as arg's
# key, which means that, for example variable startfrom matchs the argument
# arg's key('startfrom').
# arg should be the dict object returned by arg_check() method.
# var is the variable name(in string) among indent, target, startfrom and 
# endwith used in indent_convertor.py script.
# default is the default value passed to the variable if var does not match
# the arg
def argval_passto_var(arg, var, default):
    if isinstance(arg, type({})): # If the argument passed is dict object
        if arg.keys()[0] == var:
            return int(arg.get(var)) # Returns the value from arg dict if arg's key matchs var
        else:
            return default # otherwise returns the default value
    else: # If arg is the string this means the arg_check() returns error
        return arg # Returns an error message to variable then print it out
        """
