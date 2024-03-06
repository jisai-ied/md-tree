#!/usr/bin/env python3
import subprocess, argparse

def get_tree(level: int = 3, ignore_list: list[str] = None) -> str:
    if ignore_list:
        tree = subprocess.run(["tree", ".", "-L", str(level), "-I", "|".join(ignore_list)], capture_output=True).stdout.decode("utf-8")
    else:
        tree = subprocess.run(["tree", ".", "-L", str(level)], capture_output=True).stdout.decode("utf-8")
    
    if tree != ".\n\n0 directories, 0 files\n":
        return tree
    return ""

def replace_content(filename: str, new_content: str):
    with open(filename, 'r') as file:
        content = file.read()

    start_index = content.find('<!-- _TREE_ -->') + len('<!-- _TREE_ -->')
    end_index = content.find('<!-- _ENDTREE_ -->')

    if start_index == -1 or end_index == -1:
        print("Tree space not found")
    else:
        new_content = content[:start_index] + '\n```tree\n' + new_content + '\n```\n' + content[end_index:]
        
        with open(filename, 'w') as file:
            file.write(new_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--filename', type=str, help='The name of the file to modify')
    parser.add_argument('--level', type=int, help='The level of the directory tree')
    parser.add_argument('--ignore_list', type=str, help='A comma-separated list of directories to ignore')
    args = parser.parse_args()

    new_content = get_tree(
        level=args.level if args.level else 3, 
        ignore_list=args.ignore_list.split(",") if args.ignore_list else None
    )
    replace_content(args.filename, new_content)