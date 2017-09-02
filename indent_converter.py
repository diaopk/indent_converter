#!/usr/bin/env python

import sys
import header as h
import subprocess as p
import io

result = '' # result to be returned
case_indent = '  ' # my case
args = sys.argv # A list of arguments entered
script, content, indent, target, start, end = h.get_arg(args)

if __name__ == "__main__":
    # ---------- START Program process -----------------
    # Append lines that do not need to be converted
    for line in content[0:start]:
       result += line

    # The statements below are only for my case to use this program
    # These statements are based on the number of times I tab to 
    # indent a line If 1 tab occupies 8 whitespaces, then 
    # (indent_converter source_file 8 4 will convert each indent space# from 8 whitespaces into 4 whitespaces
    if script is None:
        for line in content[start:end]:
            # Convert it into a new line
            line = h.converter(line, indent, target, case_indent)
            result += line
    else: # processing python script
        result += h.converter(content[start: end+1])
    
    # Append lines that do not need to be converted
    for line in content[end+1:]:
        result += line
    # ------------------- END Porgram process----------------


    print 'The following is the result: '
    print "\n"
    print result
"""
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
    """
