from not_pip_tex_table_image_generation import get_tex_table, get_tex_image

table_data = [
    ["Programming Language", "Experience", "Color"],
    ["C++", 30, "Blue"],
    ["Python", 25, "Green"],
    ["Java", 35, "Orange"]
]

image_path = "artifacts/cat.png"

tex_table = get_tex_table(table_data)
tex_image = get_tex_image(image_path)

tex_header = '''\\documentclass{article}
\\usepackage{graphicx}
\\begin{document}
\\section{Table Example}
This is an example table.
'''

with open("artifacts/table_image_tex_example.tex", "w") as f:
    f.write(tex_header)
    f.write(tex_table)
    f.write('\\section{Image Example}\nThis is an example image.\n')
    f.write(tex_image)
    f.write("\\end{document}\n")
