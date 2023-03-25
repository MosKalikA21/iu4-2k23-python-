import argparse
import json
import re
import sys
from typing import List


def parse_function_header(header_str: str) -> dict:
    """Parses a function header and returns a dictionary with its attributes."""
    try:
        name, return_type, args_str = re.match(r"^\s*(\w+)\s+(\w+)\s*\((.*)\)\s*;", header_str).groups()
        args = []
        for arg in args_str.split(","):
            arg = arg.strip()
            if arg:
                arg_name, arg_type = arg.split()
                args.append({"name": arg_name, "type": arg_type})
        return {"name": name, "return_type": return_type, "args": args}
    except AttributeError:
        return {}


def parse_struct(header_lines: List[str]) -> dict:
    """Parses a struct definition and returns a dictionary with its attributes."""
    struct = {}
    try:
        struct_name = re.match(r"^\s*struct\s+(\w+)\s*\{", header_lines[0]).groups()[0]
        struct_fields = []
        for line in header_lines[1:]:
            line = line.strip()
            if not line:
                continue
            if line == "}":
                break
            field_match = re.match(r"^\s*(\w+)\s+(\w+)\s*;", line)
            if not field_match:
                return {}
            field_type, field_name = field_match.groups()
            struct_fields.append({"name": field_name, "type": field_type})
        struct = {"name": struct_name, "fields": struct_fields}
    except AttributeError:
        pass
    return struct


def parse_headers(header_str: str) -> dict:
    """Parses header string and returns a dictionary with its functions and structs."""
    functions = []
    structs = []
    current_header_lines = []
    for line in header_str.splitlines():
        line = line.strip()
        if not line:
            continue
        current_header_lines.append(line)
        if line.endswith(";"):
            function = parse_function_header(" ".join(current_header_lines))
            if function:
                functions.append(function)
            current_header_lines = []
        elif line.startswith("struct"):
            struct = parse_struct(current_header_lines)
            if struct:
                structs.append(struct)
            current_header_lines = []
    return {"functions": functions, "structs": structs}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", help="output JSON file")
    args = parser.parse_args()

    input_str = sys.stdin.read()
    parsed_headers = parse_headers(input_str)

    if args.json:
        with open(args.json, "w") as f:
            json.dump(parsed_headers, f, indent=4)
    else:
        print(json.dumps(parsed_headers, indent=4))


if __name__ == "__main__":
    main()

#python parser.py --json output.json < input_file.h
