import argparse
import sys
import re
from pathlib import Path


def parse_args(function_obj: object, args: str) -> list:
    """
    set the type of the arguments of the function,
    dynamically from function annotations.
    """

    # * get the function annotations types by input args order.
    typed_args = []  # * return list of typed arguments.
    for cur_type in function_obj.__annotations__.values():
        # * iterate over the function annotations types.
        if cur_type is str:
            # * parse the string argument.
            cur_arg = args.split(",", 1)[0].strip()[1:-1]
            typed_args.append(cur_arg)
            args = args.split(",", 1)[1] if len(args.split(",", 1)) > 1 else ""
        elif cur_type is int:
            # * parse the int argument.
            cur_arg = args.split(",", 1)[0]
            typed_args.append(int(cur_arg))
            args = args.split(",", 1)[1] if len(args.split(",", 1)) > 1 else ""
        elif cur_type is list:
            # * parse the list argument. (list of strings)
            cur_arg = re.findall(r"\[(.*?)\]", args)[0]
            typed_args.append(cur_arg.split(","))
            args = args.split("]", 1)[1][1:]
    return typed_args


def main(path: str | None = None):
    """
    path: - the path to of the file to read. If the file does not exists or None, read from stdin.

    read the file/stdin line by line, set types of the arguments, execute the function, and print the output.
    """
    if path and Path(path).is_file():
        f = Path(path).open("r")
    else:
        f = sys.stdin

    FUNCTIONS_MODULE_NAME = "functions"
    functions_module = __import__(FUNCTIONS_MODULE_NAME)

    with f:
        while True:
            try:
                raw_line = f.readline()
                # * check for new line.
                if raw_line:
                    line = raw_line.strip()
                    # * check for empty line.
                    if line:
                        # * split the line into function name and arguments.
                        spt_line = line.split(",", 1)
                        str_function_name, args = spt_line[0], spt_line[1]

                        # * get the function object by name from from functions module attributes.
                        try:
                            function_obj = getattr(functions_module, str_function_name)
                        except AttributeError:
                            print("Invalid function name")
                        else:
                            # * When function object found, parse the arguments and execute the function.
                            typed_args = parse_args(function_obj, args)
                            print(function_obj(*typed_args))

                else:
                    # * when no more lines, break the loop.
                    break
            except KeyboardInterrupt:
                # * Ctrl-C (SIGINT) causes KeyboardInterrupt to be raised.
                break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""A system in Python that receives a text as an input from file or stdin, 
        and for each line it execute the function with the given parameters.""",
        epilog="""
        Example: python app.py input_file.txt""",
    )
    parser.add_argument(
        "INFILE",
        type=str,
        nargs="?",  # * nargs="?" means that the argument is optional.
        help="""Optional input file. 
        The text file contains lines in the following format: [function name], [comma separated list of arguments]
        If not provided, the program will read from stdin. To exit, press Ctrl-C (SIGINT).""",
    )
    args = parser.parse_args()
    main(args.INFILE)
