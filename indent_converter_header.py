#!/usr/local/bin/python
# Define some functions used by indent_convertor.py

# Define argument names:
arg_names = ['--indent', '--target', '--startfrom', '--endwith']

# Define a class for argument object
class Arg:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# method to print program information and how the program use
def print_program_info():
    print 'This program takes at least one text file to process the program'
    print '- Accepted syntaxs:(note that the order of args entered does not mater)'
    print '- indent_converter source_file --startfrom/endwith'
    print '-                              --indent=num1 --target=num2'
    print '-                              --starfrom=line1 --endwith=line2'
    print '-                              --indent=num1 --target=num2 --starfrom/endwith=line'
    print '-                              --indent=num1 --target=num2 --startfrom=line1 --endwith=line2'
    print '- first source_file: file-like object'
    print '- optional arg indent: the original indent to be replaced with'
    print '- optional arg target: the number of indent to replace with the original one'
    print '- optional arg startfrom: the line number that a program starts from'
    print '- optional arg endwith: the line number that a program ends with'

# Method to return Boolean value to indicate the condition of if a passed
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
    if case_indent != None:
        #print ''
        #print 'int_indent: '+str(int_indent)
        #print 'int_target_indent: '+str(int_target_indent)
        # Convert them into whitespaces
        indent = ''.ljust(int_indent, ' ')
        target_indent = ''.ljust(int_target_indent, ' ')
        line = str(line)
        raw_string = line.lstrip()
        #print "indent:'%s'"%indent
        #print "target_indent:'%s'"%target_indent
        #print 'Before the loop line:'+line
        #print 'Before the loop raw string:'+raw_string
        #print 'test:'+line[len(indent):]
        #print line[len(indent):] == raw_string

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

# Method to show error(s) message
def errors_info():
    print ''

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