import argparse
from .generators import (
    generate_readme,
    generate_license,
    generate_gitignore,
)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")

    args = parser.parse_args()

    if args.command == "readme":
        generate_readme()

    elif args.command == "license":
        generate_license()

    elif args.command == "gitignore":
        generate_gitignore()

    else:
        print("Unknown command.")
