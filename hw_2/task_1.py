from latex_gen_nikitakeba import generate_table

data = [
    ["Name", "Age", "City"],
    ["Nikita", 22, "Moscow"],
    ["Clark Kent", 30, "Metropolis"],
]

latex_code = generate_table(data)

with open("artifacts/table.tex", "w") as f:
    f.write(latex_code)

print(latex_code)

