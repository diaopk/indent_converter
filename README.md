# indent_converter
A simple python script taking text file, python script ... and converting each line of the file into new line with required indentation. This script is personally used by myself for talking note and writing python scripts.

# Use
```
./indent_converter source_file --indent=num1 --target=num2 --start=num3 --end=num4
```

There are 4 numbers passed to the script.
- indent takes the number of white spaces as the old indentation that you want it to be converted. 4 by default.
- target takes the number of white spaces as the new indentation that you want to replace. 4 by default.
- start takes the line number where the script starts. First line by default.
- end takes the line number where the script ends. The last line by default.

Any of these arguments have default value so no need to pass all of them.

The script can also convert python script but ```start``` and ```end``` need to be filled in. Because it doesn't know which function or what part of code is the subfunction or subpart of the outer function or code.

```
./indent_converter python_script.py --start=num1 --end=num2
```

CONTIUNED...
