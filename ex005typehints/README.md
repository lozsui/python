# TODO

Merge notes here into a_solved_knot/README.md

# Notes About Code Samples

Make sure you are in directory ex005typehints:

> (.venv) PS C:\Temp\python\ex005typehints>

To check type safty do something like:

```
(.venv) PS C:\Temp\python\ex005typehints> mypy .\boundary.py
boundary.py:44: error: Argument 1 to "concat_cars" has incompatible type "list[Bicycle]"; expected "list[Car]"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```

mypy can also be run on a complete project like `mypy my_source_folder`. In ex005typehints it can be done like shown below.

> (.venv) PS C:\Temp\python\ex005typehints> mypy .

# Puzzles

I puzzles me that mypy does not complain about type error in method 'test_parse_token_error'.

```
(.venv) PS C:\Temp\python\ex005typehints> mypy .\test_main.py
main.py:26: error: Argument 1 to "parse_token" has incompatible type "Animal"; expected "str"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```
