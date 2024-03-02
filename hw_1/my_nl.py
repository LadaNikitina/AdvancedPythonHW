import sys

# max_width - размер отступа
def my_nl(args, max_width = 6):
    if len(args) > 2:
        print("Error! Too much arguments!")
        return
    
    if len(args) > 1:
        file_name = args[1]
        
        try:
            with open(file_name, 'r', encoding = 'utf-8') as file:
                lines = file.readlines()
        except FileNotFoundError:
            # nl: artifacts/aaa: No such file or directory
            print(f"nl: {file_name}: No such file or directory", file = sys.stderr)
            return
    else:
        lines = sys.stdin.readlines()
    
    for i, line in enumerate(lines):
        print(f"{i + 1 : > {max_width}}\t{line[: -1]}")

if __name__ == '__main__':   
    args = sys.argv
    my_nl(args)