import argparse
import sys
import datetime
import os
import shutil

def setup():
    parser = argparse.ArgumentParser(description="CLI")
    parser.add_argument("command", help="ls, cd, mkdir, rmdir, rm, rm-r, cp, mv, find, cat, show_logs")  
    parser.add_argument("path", type=str, nargs="?", default=".", help="Path for commands")
    parser.add_argument("file", nargs="?", default=".", help="file for commands")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to remove")
    parser.add_argument("source",  help="Source for commands")
    parser.add_argument("destination", help="Destination for commands")
    parser.add_argument("pattern", type=str, help="Search for files or directory for find command")
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

def make_directory(path):
    directory = "new_directory"
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory '{directory}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def rmdir(path, recursive=False):
    try:
        if recursive:
            for root, dirs, files in os.walk(path, topdown=False):
                for file in files: 
                    os.remove(os.path.join(root, file))
                    for dir in dirs:
                        os.rmdir(os.path.join(root, dir))
                        os.rmdir(path)
                        print(f"directory '{path}' and its contents removed successfully. ")
                    else:
                        os.rmdir(path)
                        print(f"Empty directory '{path}' removed successfully. ")
    except FileNotFoundError:
      print(f"Error: directory '{path}' not found. ")
    except OSError:
        print(f"Error: directory '{path}' is not empty or cannot be removed. ")

def copy(source, destination, recursive, force):
    if os.path.isdir(source):
        if recursive:
            shutil.copytree(source, destination, dirs_exist_ok=force)
        else:
            print("Use -r to copy directories.")
    elif os.path.isfile(source):
        if os.path.exists(destination) and not force:
            print("File already exists ---> Use -f to overwrite.")
        else:
            shutil.copy2(source, destination)
    else:
        print("Invalid command.")

def mv(source, destination):
    try:
        os.rename(source, destination)
        print(f"moved '{source}' to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"Error: source file or directory '{source}' not found. ")
    except PermissionError:
        print(f"Error: permission denied for moving '{source}' to '{destination}'. ")

def find_pattern(path, pattern):
    exts = list()
    for dirpath, dirs, files in os.walk(path):
        for f in files:
            ext = f.split(".")[-1]
            if ext == pattern:
                exts.append(os.path.join(dirpath, f))
    if exts:
        print("Files found:")
        for file in exts:
            print(file)
    else:
        print(f"No files matching pattern '{pattern}' found.")
    
parser = setup()
args = parser.parse_args()
if args.command == "ls":
    ls(args.path)
elif args.command == "cd":
    try:
        change_directory(args.path)
    except Exception as e:
        print(e)
elif args.command == "mkdir":
    make_directory(args.path)
elif args.command == "rmdir":
        if args.path:
            rmdir(args.path, args.recursive)
        else:
            print("Error: 'rmdir' requires a directory path.")
elif args.command == "rm":
    pass
elif args.command == "rm-r":
    pass
elif args.command == "cp":
    copy(args.source, args.destination, args.recursive, args.force)
elif args.command == "mv":
    mv(args.source, args.destination)
elif args.command == "find":
    find_pattern(args.path, args.pattern)
elif args.command == "cat":
    pass
