#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""

import sys
import re
import argparse


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    names = []
    names_dict = {}

    with open(filename) as f:
        source_file = f.read()
        pattern = re.compile(r'Popularity in')
        matches = pattern.finditer(source_file)
        for match in matches:
            year = match.span()
            names.append(source_file[year[1]:][1:5])

    with open(filename) as l:
        for line in l:
            rank_name = re.findall(
                r'"right"><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>', line)
            for name in rank_name:
                if not name[1] in names_dict:
                    names_dict[name[1]] = name[0]
                if not name[2] in names_dict:
                    names_dict[name[2]] = name[0]
    for key in sorted(names_dict):
        names.append(key + " " + names_dict[key])

    return names

    #  dict_boys = {}
    #   dict_girls = {}

    # boy ranks
    #    for rank_b in baby_names:
    #         dict_boys[rank_b[1]] = rank_b[0]
    # girl ranks
    # for rank_g in baby_names:
    #     dict_girls[rank_g[2]] = rank_g[0]

    # for key, value in sorted(dict_boys.items()):
    #     print(value, '', key)

    # for key, value in sorted(dict_girls.items()):
    #     print(value, '', key)

    # combined_dict = dict(dict_boys, **dict_girls)

    # print(dict_boys)

    # for key, value in combined_dict.items():
    #     print(key, value)

    # my_char = " "
    # names = [(item[0] + my_char + item[1])
    #          for item in combined_dict.items()]
    # names.insert(0, year)

    # return names


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)
    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    # For each filename, call `extract_names()` with that single file.
    # Format the resulting list as a vertical list (separated by newline \n).
    # Use the create_summary flag to decide whether to print the list
    # or to write the list to a summary file (e.g. `baby1990.html.summary`).

    for each in file_list:
        each_file = extract_names(each)
        each_file = "\n".join(each_file)
        if not create_summary:
            print(each_file)
        else:
            new_file = each + ".summary"
            f = open(new_file, "w")
            f.write(str(each_file))

    # text = '\n'.join(name_output)
    # with open(file + ".summary", 'w+') as f:
    #     f.write(text)


if __name__ == '__main__':
    main(sys.argv[1:])
