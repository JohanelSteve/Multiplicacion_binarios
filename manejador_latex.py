import os

class Procedimiento:
    """Guarda información de un procedimiento en LaTeX."""
    tabla_operadores = {
        "+": "+",
        "-": "-",
        "*": "\\times",
        "/": "\\div",
        "=": "=",
        "=>": "\\Longrightarrow",
        "<=>": "\\Longleftrightarrow",
        "<<": "\\ll",
        "^": "^"
    }

    def __init__(self, var1, operador, var2):
        self.var1 = var1
        self.operador = operador
        self.var2 = var2
    
    def __repr__(self) -> str:
        """Devuelve la información del procedimiento en LaTeX."""
        var1 = self.var1
        if type(var1) != Procedimiento:
            var1 = f"\\text{{{var1}}}"
        var2 = self.var2
        if type(var2) != Procedimiento:
            var2 = f"\\text{{{var2}}}"
        return f"{var1}{self.tabla_operadores[self.operador]}" + ('{' if self.operador == '^' else '') + f"{var2}" + ('}' if self.operador == '^' else '')

class Paso:
    """Guarda información de un paso de la multiplicación binaria."""
    def __init__(self, nombre, desc, procedimientos):
        self.nombre = nombre
        self.desc = desc
        self.procedimientos = procedimientos
    
    def __repr__(self) -> str:
        """Devuelve la información del paso en LaTeX."""
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
    """Devuelve la información del curso en LaTeX."""

    return """\\title{Diseños Lógicos}
\\author{Johanel, Fabrizio, Jeaustin}
\institute{Tecnológico de Costa Rica}
\date{Semestre I de 2023}
"""

def crear_documento_latex(nombre_archivo, pasos):
    """Crea un archivo LaTeX a partir de una lista de pasos."""
    with open(f"{nombre_archivo}.tex", "w") as f:
        f.write("""\\documentclass{beamer}
\\usepackage{amsmath}
\\usepackage{amssymb}
\\usepackage[utf8]{inputenc}

"""+ informacion_curso_latex() +"""

\\begin{document}
""" + "".join([repr(paso) for paso in pasos]) + """
\\begin{frame}
\maketitle
\\note{Notas}
\end{frame}
\end{document}""")

def crear_pdf_latex(nombre_archivo):
    """Crea un archivo PDF a partir de un archivo LaTeX."""
    os.system(f"pdflatex {nombre_archivo}.tex")
    import platform
    if platform.system() == "Windows":
        os.system(f"del {nombre_archivo}.aux {nombre_archivo}.log {nombre_archivo}.out {nombre_archivo}.nav {nombre_archivo}.snm {nombre_archivo}.toc")
    else:
        os.system(f"rm {nombre_archivo}.aux {nombre_archivo}.log {nombre_archivo}.out {nombre_archivo}.nav {nombre_archivo}.snm {nombre_archivo}.toc")