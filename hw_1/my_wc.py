import sys

def my_wc(lines):
    num_lines = 0
    num_words = 0
    num_bytes = 0

    for line in lines:
        num_words += len(line.split())
        num_bytes += len(line.encode('utf-8'))
        num_lines += 1
        
    return num_lines, num_words, num_bytes
    
def my_wc_main_func(args):
    all_num_lines, all_num_words, all_num_bytes = 0, 0, 0

    if len(args) > 1:
        # несколько файлов
               
        for i, file_name in enumerate(args[1 : ]):
            try:
                with open(file_name, 'r', encoding = 'utf-8') as file:                                          
                    lines = file.readlines()
                    num_lines, num_words, num_bytes = my_wc(lines)
                    print(f"{num_lines : > 3}{num_words : > 4}{num_bytes : > 4} {file_name}")
                    
                    all_num_lines += num_lines
                    all_num_words += num_words
                    all_num_bytes += num_bytes                    
            
            except FileNotFoundError:
                print(f"wc: {file_name}: No such file or directory", file = sys.stderr)
                continue
        if len(args[1 : ]) > 1:
            print(f"{all_num_lines : > 3}{all_num_words : > 4}{all_num_bytes : > 4} total")
                
    else:
        # нет файлов
        lines = sys.stdin.readlines()
        all_num_lines, all_num_words, all_num_bytes = my_wc(lines)
        
        print(f"{all_num_lines : > 3}{all_num_words : > 4}{all_num_bytes : > 4}")

    
args = sys.argv
my_wc_main_func(args)