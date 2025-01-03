artist = ""
artwork = ""
year = ""
description = ""
conservation_statement = ""
iteration_table = f"1 &  2022-10-1 & venue and something else \\\\\\hline"

identity_report_latex=f"""
\\documentclass[a4paper,12pt]{{article}}
\\usepackage{{graphicx}} 
\\usepackage[utf8]{{inputenc}}
\\usepackage{{longtable}}
\\usepackage{{booktabs}}

\\begin{{document}}
\\title{{Identity Report}}
\\maketitle
\\noindent
\\begin{{minipage}}{{0.5\\textwidth}}
    \\large\\textbf{{Artist:}} {artist}\\newline
    \\large\\textbf{{Title:}}  {artwork}\\newline
    \\large\\textbf{{Year:}}  {year}\\newline
\\end{{minipage}}
\\hfill
\\begin{{minipage}}{{0.48\\textwidth}} 
    \\centering
    \\includegraphics[width=\\textwidth]{{}}
\\end{{minipage}}

\\section*{{Description}}
{description}

\\section*{{Conservation statement}}
{conservation_statement}

\\section*{{Exhibition and Iteration History}}
\\begin{{longtable}}{{|p{{0.1\\textwidth}}|p{{0.3\\textwidth}}|p{{0.5\\textwidth}}|}} 
\\hline
\\textbf{{N}} & \\textbf{{Date}} & \\textbf{{Venue - title}} \\\\ 
\\hline
\\endfirsthead
{iteration_table}

\\end{{longtable}}
\\end{{document}}
"""

with open("neo4j_data.tex", "w") as f:
    f.write(identity_report_latex)

print("LaTeX file generated successfully.")