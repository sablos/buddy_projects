import requests
import json
import sys

# globals
url = "https://ghibliapi.herokuapp.com/films"
films = requests.get(url).json()

help_msg = """
Run from shell environment with any of the following options:
 -d Show director for each film
 -p Show producer
 -y Year released
 -h Show this help message
"""


def help():
    print(help_msg)

def title(film):
    print(f"Title: {film['title']}")

def director(film):
    print(f"Directed by: {film['director']}")

def producer(film):
    print(f"Produced by: {film['producer']}")

def year(film):
    print(f"Year released: {film['release_date']}")

def add_call(arg):
    # opt_list = ["-d", "-p", "-y"]
    # return string that contains a valid function call, or return false if any option is invalid
    if arg == "-d":
        return "\ndirector(f)"
    elif arg == "-p":
        return "\nproducer(f)"
    elif arg == "-y":
        return "\nyear(f)"
    else:
        return False

def show_results(command):
    for i, f in enumerate(films):
        print()
        print(i + 1)
        title(f)
        exec(command)
    if command == "":
        print("\nRun this script in the shell environment with -h for additional display options")

# main program
# check command line for args
help_only = False

# if not run from shell environment
if len(sys.argv) == 0:
    help_only = True

options = []
if len(sys.argv) > 1:
    options = sys.argv[1:]

# construct a list of function calls in the order of valid args
calls = ""

if "-h" in options:
    help_only = True
else:
    for op in options:
        if not add_call(op):
            help_only = True
            break
        else:
            calls += add_call(op)

# program output
if help_only:
    help()
else:
    show_results(calls)
