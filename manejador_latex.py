import os

class Procedimiento:
    tabla_operadores = {
        "+": "+",
        "-": "-",
        "*": "\\times",
        "/": "\\div",
        "=": "=",
        "=>": "\\\Longrightarrow",
        "<=>": "\\\Longleftrightarrow",
    }

    def __init__(self, var1, operador, var2):
        self.var1 = var1
        self.operador = operador
        self.var2 = var2
    
    def __repr__(self) -> str:
        return f"$\\textit{{{self.var1}}} $ {self.tabla_operadores[self.operador]} $ \\textit{{{self.var2}}}$"

class Paso:
    def __init__(self, nombre, desc, procedimientos):
        self.nombre = nombre
        self.desc = desc
        self.procedimientos = procedimientos
    
    def __repr__(self) -> str:
        texto = f"""\\begin{{frame}}
\\frametitle{{{self.nombre}}}
{self.desc}
\\begin{{itemize}}
"""
        for proc in self.procedimientos:
            texto += f"""\\item ${proc}$
"""
        texto += """\\end{itemize}
\\note{Notas}
\end{frame}
"""
        return texto

def informacion_curso_latex():
    return """\\title{Diseños Lógicos}
\\author{Johanel, Fabrizio, Jeaustin}
\institute{Tecnológico de Costa Rica}
\date{Semestre I de 2023}
"""

def crear_documento_latex(nombre_archivo, pasos):
    with open(f"{nombre_archivo}.tex", "w") as f:
        f.write("""\\documentclass{beamer}
\\usepackage{amsmath}
\\usepackage{amssymb}

"""+ informacion_curso_latex() +"""

\\begin{document}
""" + "".join([repr(paso) for paso in pasos]) + """
\\begin{frame}
\maketitle
\\note{Notas}
\end{frame}
\end{document}""")

def crear_pdf_latex(nombre_archivo):
    os.system(f"pdflatex {nombre_archivo}.tex")
    os.system(f"rm {nombre_archivo}.aux {nombre_archivo}.log {nombre_archivo}.out {nombre_archivo}.nav {nombre_archivo}.snm {nombre_archivo}.toc")