from latex_gen_nikitakeba import generate_table, generate_image
import subprocess

data = [
    ["Name", "Age", "City"],
    ["Nikita", 22, "Moscow"],
    ["Clark Kent", 30, "Metropolis"],
]

table = generate_table(data)
image = generate_image("superman.png")

doc = """\\documentclass{article}
\\usepackage{graphicx}
\\begin{document}

""" + table + """

\\vspace{1cm}

""" + image + """

\\end{document}
"""

with open("artifacts/document.tex", "w") as f:
    f.write(doc)

subprocess.run(["pdflatex", "-output-directory=artifacts", "artifacts/document.tex"])

