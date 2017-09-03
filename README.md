# indent_converter
A simple python script taking text file, python script ... and converting each line of the file into new line with required indentation.

# Use
```
./indent_converter source_file --indent=num1 --target=num2 --start=num3 --end=num4
```

There are 4 numbers passed to the script.
- indent takes the number of white spaces as the old indentation that you want it to be converted. 4 by default.
- target takes the number of white spaces as the new indentation that you want to relace. 4 by default.
- start takes the line number where the script starts. first line by default.
- end takes the line number where the script ends. the last line by default.

Any of these arguments have default value so no need to pass all of them.

CONTIUNED...
