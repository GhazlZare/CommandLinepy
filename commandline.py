import argparse
import sys
import datetime
import os

def setup():
    parser = argparse.ArgumentParser(description="CLI")
    parser.add_argument("command", help="ls, cd, mkdir, rmdir, rm, rm-r, cp, mv, find, cat, show_logs")  
    parser.add_argument("path", type=str, nargs="?", default=".", help="Path for commands")
    parser.add_argument("file", nargs="?", default=".", help="file for commands")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to remove")
    parser.add_argument("source", nargs="?", help="Source for commands")
    parser.add_argument("destination", nargs="?", help="Destination for commands")
    parser.add_argument("--pattern", help="Search for files or directory for find command")
    parser.add_argument("-r", nargs="?", help="Remove the directory at directory recursive")
    parser.add_argument("--show-logs",action="store_true", help="show all logs of the program")
    return parser

def ls(path="."):
    try:
        contents = os.listdir(path)
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
    except PermissionError:
        print(f"Error: permission denied for accessing '{path}'.")
    except Exception as e:
        print(f"Error: {e}")

def change_directory(path):
    os.chdir(path)
    print(f"directory changed to {path}")

parser = setup()
args = parser.parse_args()
if args.command == "ls":
    ls(args.path)
elif args.command == "cd":
    change_directory(args.path)
elif args.command == "mkdir":
    pass
elif args.command == "rmdir":
    pass
elif args.command == "rm":
    pass
elif args.command == "rm-r":
    pass
elif args.command == "cp":
    pass
elif args.command == "mv":
    pass
elif args.command == "find":
    pass
elif args.command == "cat":
    pass
