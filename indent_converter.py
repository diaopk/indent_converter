#!/usr/local/bin/python
# THIS PROGRAM WILL OVERRIDE THE SOURCE FILE
# This program supports two main festures to convert indentation.
# ----------- First feature -----------------
# The process of converting indents can be based on the number of 
# whitespaces that ONE TAB occupies.
# For example
# (indent_converter source_file 8 4) will convert from 8 
# whitespaces into 4 whitespaces for each line. If a line doesn't 
# start with a tab, then This line would not change

# ------------ Second feature --------------
# The process of converting indents can add a number of 
# whitespaces to the head of each line. This is not my original 
# feature to support but when I come to deeper programing in it, 
# I found this feature is neccessary.

import sys
# import argparse # someone says to use this module
import indent_converter_header as h
import subprocess as p
import io
import argcomplete, argparse

#num_args = len(sys.argv) # the number of argunments entered
#args = {} # Dictionary object to store arguments entered
result = '' # result to be returned
case_indent = '  ' # my case
args1 = sys.argv
content, indent, target, start, end = h.get_arg(args1)
"""
# Obtain parameters
# ----------------START text file obtain------------
try:
    obj = str(sys.argv[1]) # file-object variable
except:
    print '- You forget to input a file'
    h.print_program_info()
    exit()
else:
    try:
        f = open(obj, 'r')
    except:
        print '- Please enter a correct path to that text file'
        exit()
    else:
        content = f.readlines()

        # Define some default settings and arguments
        indent = 8
        target = 4
        startfrom = 0
        endwith = len(content)

        # Then close the file
        f.close()
# ----------------End text file obtain----------------

# ----------------Start optional arguments obtain-----
if num_args == 3: # if 1 optional arugment entered
    arg2 = h.arg_parser(sys.argv[2])
    
    try:
        # Store the arg object to args dictionary object
        args.update({arg2.name: arg2.value})
    except:
        # If arg2 is not the Arg object then print error and exit the program
        print arg2
        exit()
    else:
        try:
            # Try to store the arg2's value to startfrom or endwith
            startfrom = args.get('startfrom')
        except:
            try:
                endwith = args.get('endwith')
            except:
                print '- syntax error'
                print '- Please type -h or --help for more informtaion'
                exit() 

elif num_args == 4: # If 2 optional arguments entered
    arg2 = h.arg_parser(sys.argv[2])
    arg3 = h.arg_parser(sys.argv[3])

    try: 
        # Store arg2 and arg3 objects to args dictinary object
        # If those are Arg objects then go ahead
        # Otherwise print errors and exit the program
        args.update({arg2.name: arg2.value, arg3.name: arg3.value})
    except:
        # Print whichever is the type of string
        for error in [arg2, arg3]:
            print error
        exit()
    else:
        if args.has_key('startfrom') and args.has_key('endwith'):
            startfrom = args.get('startfrom')
            endwith = args.get('endwith')
        
        elif args.has_key('indent') and args.has_key('target'):
            indent = args.get('indent')
            target = args.get('target')

        else:
            print '- syntax error'
            print '- Please type -h or --help for more information'
            exit()

elif num_args == 5: # If 3 optional arguments entered
    arg2 = h.arg_parser(sys.argv[2])
    arg3 = h.arg_parser(sys.argv[3])
    arg4 = h.arg_parser(sys.argv[4])

    try:
        args.update({arg2.name: arg2.value, arg3.name: arg3.value, arg4.name: arg4.value})

    except:
        for error in [arg2, arg3, arg4]:
            print error

        exit()

    else:
        if args.has_key('indent') and args.has_key('target') and args.has_key('startfrom'):
            indent = args.get('indent')
            target = args.get('target')
            startfrom = args.get('startfrom')

        elif args.has_key('indent') and args.has_key('target') and args.has_key('endwith'):
            indent = args.get('indent')
            target = args.ge('target')
            endwith = args.get('endwith')

        else:
            print '- syntax error'
            print '- Please type -h or --help for more information'
            exit()

elif num_args == 6: # If 4 optional arguments entered
    arg2 = h.arg_parser(sys.argv[2])
    arg3 = h.arg_parser(sys.argv[3])
    arg4 = h.arg_parser(sys.argv[4])
    arg5 = h.arg_parser(sys.argv[5])

    try:
        args.update({arg2.name: arg2.value, arg3.name: arg3.value, arg4.name: arg4.value, arg5.name: arg5.value})

    except:
        for error in [arg2, arg3, arg4, arg5]:
            print error

        exit()

    else:
        if args.has_key('indent') and args.has_key('target') and args.has_key('startfrom') and args.has_key('endwith'):
            indent = args.get('indent')
            target = args.get('target')
            startfrom = args.get('startfrom')
            endwith = args.get('endwith')

        else:
            print '- syntax error'
            print '- Please type -h or --help for more information'
            exit()

elif num_args > 6: # If more than 4 arguments entered
    print '- syntax error: too many arguments entered'
# -----------End optional arguments obtain----------
"""

# ---------- START Program process -----------------
# process lines without needs to be converted from the head
for line in content[0:start]:
    result += line

# The statements below are only for my case to use this program
# These statements are based on the number of times I tab to 
# indent a line If 1 tab occupies 8 whitespaces, then 
# (indent_converter source_file 8 4 will convert each indent space# from 8 whitespaces into 4 whitespaces
for line in content[start:end]:
    line = h.converter(line, indent, target, case_indent=case_indent) # convert it into a new line 
    result += line

# process lines without needs to be converted from the end
for line in content[endwith:]:
    result += line
# ------------------- END Porgram process----------------


print 'The following is the result: '
print '|'
print '|'
print '|'
print result # check the result to be inputed later, do not have to

if result != content:
    n = 1
    filename = f.name+'_copy'
    # The following writes a new file
    while p.os.path.exists(filename+str(n)) == True:
        n += 1
        filename += str(n)
    
    # Make sure there is no files with the same filename
    # Then create a new file and store the result in it
    with io.FileIO(filename, 'w') as new_file:
        new_file.write(result)
else:
    print '- Nothing changed'
