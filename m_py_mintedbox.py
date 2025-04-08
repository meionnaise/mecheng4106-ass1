filenames = "q1/q1.m", "q2/q2.m", "q3/q3.m", "q4/q4.m"

for filename in filenames:
    with open(filename) as f:
        data = f.read()
        f.close()

    new_data = "\\begin{mintedbox}{matlab}\n" + data + "\n\\end{mintedbox}"
    new_filename = f"{filename[:-2]}_code.tex"

    with open(new_filename, mode="w") as f:
        f.write(new_data)
        f.close()