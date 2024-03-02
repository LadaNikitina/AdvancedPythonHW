import sys

def my_tail(lines, num_strings = 10):
    return lines[- min(len(lines), num_strings) : ]

def my_tail_main_func(args):
    if len(args) > 1:
        # несколько файлов
        
        for i, file_name in enumerate(args[1 : ]):
            try:
                with open(file_name, 'r', encoding = 'utf-8') as file:
                    if i != 0:
                        print()
                        
                    if len(args) > 2:
                        print(f"==> {file_name} <==")
                    
                    lines = file.readlines()
                    print("".join(my_tail(lines)), end = "")
            
            except FileNotFoundError:
                print(f"tail: cannot open '{file_name}' for reading: No such file or directory", file = sys.stderr)
                continue
                
    else:
        # нет файлов
        lines = sys.stdin.readlines()
        print("".join(my_tail(lines, 17)), end = "")

    
args = sys.argv
my_tail_main_func(args)