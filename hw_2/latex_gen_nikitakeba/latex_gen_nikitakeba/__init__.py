def generate_table(data):
    if not data:
        return ""
    
    cols = len(data[0])
    col_format = "|" + "c|" * cols
    
    lines = []
    lines.append("\\begin{tabular}{" + col_format + "}")
    lines.append("\\hline")
    
    for row in data:
        row_str = " & ".join(str(cell) for cell in row)
        lines.append(row_str + " \\\\")
        lines.append("\\hline")
    
    lines.append("\\end{tabular}")
    
    return "\n".join(lines)


def generate_image(path):
    lines = []
    lines.append("\\begin{figure}[h]")
    lines.append("\\centering")
    lines.append("\\includegraphics[width=0.8\\textwidth]{" + path + "}")
    lines.append("\\end{figure}")
    return "\n".join(lines)

